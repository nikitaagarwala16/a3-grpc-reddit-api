import sys
sys.path.insert(1,'/Users/nikitaagarwala/Desktop/Mini2/API/assign/a3-grpc-reddit-api')
import reddit_pb2;
import reddit_pb2_grpc;
import grpc;
from google.protobuf.timestamp_pb2 import Timestamp
import sqlite3;
import argparse;
from concurrent import futures

class RedditServiceServicer(reddit_pb2_grpc.RedditServiceServicer):

    def CreatePost(self, request, context):
        conn = sqlite3.connect('server/reddit.db')
        cursor = conn.cursor()
        publication_date = request.publication_date.ToDatetime()
        publication_date_str = publication_date.strftime('%Y-%m-%d %H:%M:%S')

        video_link_url = None
        image_link_url = None
        if request.WhichOneof('medialink') == 'video_url':
            video_link_url= request.video_url
        elif request.WhichOneof('medialink') == 'image_url':
            image_link_url= request.image_url
        if video_link_url is not None:   
            insert_query = '''INSERT INTO Posts (AuthorID, Title, Content, VideoURL, Score, State, PublicationDate, SubredditID)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
            cursor.execute(insert_query, (request.author.id, request.title, request.content, request.video_url, 0, 0, publication_date_str, request.subreddit_attached_to.id))
        elif image_link_url is not None:
            insert_query = '''INSERT INTO Posts (AuthorID, Title, Content, ImageURL, Score, State, PublicationDate, SubredditID)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
            cursor.execute(insert_query, (request.author.id, request.title, request.content, request.image_url, 0, 0, publication_date_str, request.subreddit_attached_to.id))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        # Create and return the response
        response = reddit_pb2.CreatePostResponse()
        response.post.id = cursor.lastrowid 
        response.post.author.id = request.author.id
        response.post.title = request.title 
        return response
    
    def VoteOnPost(self, request, context):
        conn = sqlite3.connect('server/reddit.db')
        cursor = conn.cursor()
        if request.upvote:
            cursor.execute("UPDATE Posts SET Score = Score + 1 WHERE PostID = ?", (request.post.id,))
        else:
            cursor.execute("UPDATE Posts SET Score = Score - 1 WHERE PostID = ?", (request.post.id,))

        cursor.execute("SELECT Score FROM Posts WHERE PostID = ?", (request.post.id,))
        new_score = cursor.fetchone()[0]
        conn.commit()
        conn.close()

        response = reddit_pb2.VoteOnPostResponse()
        response.post.score = new_score
        return response
    
    def RetrievePost(self, request, context):
        conn = sqlite3.connect('server/reddit.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Posts WHERE PostID = ?", (request.post_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            post_message = reddit_pb2.Post()
            post_message.id = row[0]
            post_message.title = row[2]
            post_message.content = row[3]
            post_message.video_url = row[4]
            post_message.image_url = row[5]
            post_message.score = row[6]
            post_message.post_state = row[7]
            return reddit_pb2.RetrievePostResponse(post=post_message)
        else :
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Post not found')
            return reddit_pb2.RetrievePostResponse()
        
    def CreateComment(self, request, context):
        conn = sqlite3.connect('server/reddit.db')
        cursor = conn.cursor()

        # Convert the publication date from Timestamp to a datetime string
        publication_date = request.publication_date.ToDatetime()
        publication_date_str = publication_date.strftime('%Y-%m-%d %H:%M:%S')

        # Determine if the comment is attached to a post or another comment
        attached_post_id = None
        attached_comment_id = None
        if request.WhichOneof('attached_to') == 'post_attached_to_id':
            attached_post_id = request.post_attached_to_id
        elif request.WhichOneof('attached_to') == 'comment_attached_to_id':
            attached_comment_id = request.comment_attached_to_id

        # Insert the new comment into the Comments table
        if attached_post_id is not None:
            insert_query = '''INSERT INTO Comments (AuthorID, PostID, Content, Score, State, PublicationDate)
                            VALUES (?, ?, ?, ?, ?, ?)'''
            cursor.execute(insert_query, (request.author.id, attached_post_id, request.content, 0, 0, publication_date_str))
        elif attached_comment_id is not None:
            insert_query = '''INSERT INTO Comments (AuthorID, ParentCommentID, Content, Score, State, PublicationDate)
                            VALUES (?, ?, ?, ?, ?, ?)'''
            cursor.execute(insert_query, (request.author.id, attached_comment_id, request.content, 0, 0, publication_date_str))

        # Retrieve the ID of the newly created comment
        new_comment_id = cursor.lastrowid

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        # Construct the response
        response = reddit_pb2.CreateCommentResponse()
        response.comment.id = new_comment_id
        response.comment.author.CopyFrom(request.author)
        response.comment.content = request.content
        response.comment.publication_date.CopyFrom(request.publication_date)

        # Return the response
        return response

    def VoteOnComment(self, request, context):
        conn = sqlite3.connect('server/reddit.db')
        cursor = conn.cursor()
        if request.upvote:
            cursor.execute("UPDATE Comments SET Score = Score + 1 WHERE CommentID = ?", (request.comment_id,))
        else:
            cursor.execute("UPDATE Comments SET Score = Score - 1 WHERE CommentID = ?", (request.comment_id,))

        cursor.execute("SELECT Score FROM Comments WHERE CommentID = ?", (request.comment_id,))
        new_score = cursor.fetchone()[0]
        conn.commit()
        conn.close()

        response = reddit_pb2.VoteOnCommentResponse()
        response.updated_score = new_score
        return response
    
    def GetMostUpvotedCommentsOnPost(self, request, context):
        conn = sqlite3.connect('server/reddit.db')
        cursor = conn.cursor()
        query = '''SELECT CommentID, AuthorID, Content, Score, State
                   FROM Comments
                   WHERE PostID = ?
                   ORDER BY Score DESC
                   LIMIT ?'''
        cursor.execute(query, (request.post_id, request.n))
        rows = cursor.fetchall()
        response = reddit_pb2.GetMostUpvotedCommentsOnPostResponse()
        for row in rows:
            # Check if the comment has replies
            cursor.execute("SELECT COUNT(*) FROM Comments WHERE ParentCommentID = ?", (row[0],))
            has_replies = cursor.fetchone()[0] > 0
            comment_with_replies = reddit_pb2.CommentHasReplies()
            comment_with_replies.comment.id = row[0]
            comment_with_replies.comment.content = row[2]
            comment_with_replies.comment.score = row[3]
            comment_with_replies.comment.comment_state = row[4]
            comment_with_replies.has_replies =has_replies
            author_message = reddit_pb2.User(id=row[1]) 
            comment_with_replies.comment.author.CopyFrom(author_message)
            response.comments.append(comment_with_replies)

        conn.close()
        return response
    
    def GetMostUpvotedCommentsOnComment(self, request, context):
        conn = sqlite3.connect('server/reddit.db')
        cursor = conn.cursor()

        def fetch_top_comments(parent_id, limit):
            query = '''SELECT CommentID, AuthorID, Content, Score, State, PublicationDate
                    FROM Comments
                    WHERE ParentCommentID = ?
                    ORDER BY Score DESC
                    LIMIT ?'''
            cursor.execute(query, (parent_id, limit))
            return cursor.fetchall()
  
        top_comments = fetch_top_comments(request.comment_id, request.n)

        response = reddit_pb2.GetMostUpvotedCommentsOnCommentResponse()

        for comment_row in top_comments:
            # Create a Comment message for the top-level comment
            top_comment = reddit_pb2.Comment(
                id=comment_row[0],
                author=reddit_pb2.User(id=comment_row[1]),
                content=comment_row[2],
                score=comment_row[3],
                
            )

            
            comment_with_replies = reddit_pb2.CommentWithReplies(comment=top_comment)

            
            top_replies = fetch_top_comments(comment_row[0], request.n)
            for reply_row in top_replies:
                reply = reddit_pb2.Comment(
                    id=reply_row[0],
                    author=reddit_pb2.User(id=reply_row[1]),
                    content=reply_row[2],
                    score=reply_row[3],
                   
                )
                comment_with_replies.replies.append(reply)

            response.comment.append(comment_with_replies)

        conn.close()
        return response
        


def serve(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    reddit_pb2_grpc.add_RedditServiceServicer_to_server(RedditServiceServicer(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    print(f"Server running on port {port}")
    server.wait_for_termination()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='gRPC Reddit-like API Server')
    # configurable port, by default it will start on port 50051 
    parser.add_argument('--port', type=int, default=50051, help='The port on which to run the server')
    args = parser.parse_args()
    serve(args.port)