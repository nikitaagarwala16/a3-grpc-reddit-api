import sys
sys.path.insert(1,'/Users/nikitaagarwala/Desktop/Mini2/API/assign/a3-grpc-reddit-api')
import logging
import grpc
import reddit_pb2
import reddit_pb2_grpc
from google.protobuf.timestamp_pb2 import Timestamp
import datetime

def create_post(stub, author_id, title, content,subreddit_id,publication_date,attached_video_url=None,attached_image_url=None):
    # CreatePostRequest
    post_request = reddit_pb2.CreatePostRequest(
        author=reddit_pb2.User(id=author_id),
        title=title,
        content=content,
        subreddit_attached_to = reddit_pb2.Subreddit(id=subreddit_id),
        publication_date = publication_date
    )

    if attached_video_url is not None:
        post_request.video_url = attached_video_url
    elif attached_image_url is not None:
        post_request.image_url = attached_image_url

    # Send the request to the server and get the response
    response = stub.CreatePost(post_request)
    return response

def vote_on_post(stub, post_id, upvote):
    # Create a VoteOnPostRequest
    request = reddit_pb2.VoteOnPostRequest(
        post=reddit_pb2.Post(id=post_id), 
        upvote=upvote)

    # Send the request to the server and get the response
    response = stub.VoteOnPost(request)

    return response

def retrieve_post(stub,post_id):
    # Create a RetrievePostRequest
    request = reddit_pb2.RetrivePostRequest(post_id=post_id)
    try:
        response = stub.RetrievePost(request)
        return response
    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.NOT_FOUND:
            print(e.details())
        else:
            print("Post with the given POST ID not found")

def create_comment(stub, author_id, content, post_id=None, comment_id=None):
    # Create a User message for the author
    author = reddit_pb2.User(id=author_id)

    # Create a Timestamp for the current time
    current_time = Timestamp()
    current_time.FromDatetime(datetime.datetime.now())

    # Create a CreateCommentRequest
    comment_request = reddit_pb2.CreateCommentRequest(
        author=author,
        content=content,
        publication_date=current_time
    )

    # Set the appropriate attached_to field based on whether it's a post or a comment
    if post_id is not None:
        comment_request.post_attached_to_id = post_id
    elif comment_id is not None:
        comment_request.comment_attached_to_id = comment_id

    # Send the request to the server and get the response
    response = stub.CreateComment(comment_request)
    return response
def vote_on_comment(stub, com_id, upvote):
    # Create a VoteOnPostRequest
    request = reddit_pb2.VoteOnCommentRequest(
        comment_id=com_id, 
        upvote=upvote)

    # Send the request to the server and get the response
    response = stub.VoteOnComment(request)

    return response

def retrieve_most_upvoted_comments_on_a_post(stub ,post_id,n):
    request = reddit_pb2.GetMostUpvotedCommentsOnPostRequest(
        post_id = post_id,
        n = n
    )
    response = stub.GetMostUpvotedCommentsOnPost(request)
    return response
def retrieve_most_upvoted_comments_on_a_comment(stub ,comment_id,n):
    request = reddit_pb2.GetMostUpvotedCommentsOnCommentRequest (
        comment_id = comment_id,
        n = n
    )
    response = stub.GetMostUpvotedCommentsOnComment(request)
    return response

def run():
    # Assuming the server is running on localhost and port 50051
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = reddit_pb2_grpc.RedditServiceStub(channel)

        # Prepare publication date
        current_time = Timestamp()
        current_time.FromDatetime(datetime.datetime.now())

        response = create_post(
            stub,
            author_id=123,  # Example author ID
            title="Example Post Title",
            content="This is an example post",
            attached_video_url="http://example.com/image.jpg",
            subreddit_id =1,  # Example subreddit ID
            publication_date = current_time
        )

        print("Post created with ID:", response.post.id)

        response = vote_on_post(stub, post_id=1, upvote=True)
        print(f"Post with ID {response.post.id} upvoted. New score: {response.post.score}")
        response = vote_on_post(stub, post_id=1, upvote=False)
        print(f"Post with ID {response.post.id} downvoted. New score: {response.post.score}")

        response = retrieve_post(stub, post_id=1)
        if response:
            print(f"Post ID: {response.post.id}\nTitle: {response.post.title}\nContent: {response.post.content}")

        # Example usage: create a comment attached to a post
        response = create_comment(stub, author_id=123, content="This is a comment", post_id=1)
        print(f"Created comment with id {response.comment.id} ")
        response = create_comment(stub, author_id=12, content="This is a comment for a comment ", comment_id=2)
        print(f"Created comment with id {response.comment.id}")

        response = vote_on_comment(stub, com_id=1, upvote=True)
        print(f"New score: {response.updated_score}")
        response = vote_on_comment(stub, com_id=1, upvote=False)
        print(f"New score: {response.updated_score}")

        response = retrieve_most_upvoted_comments_on_a_post(stub, post_id=1, n=5)
        
        # Process and display the response
        for comment_with_replies in response.comments:
            comment = comment_with_replies.comment
            print(f"Comment ID: {comment.id}")
            print(f"Author ID: {comment.author.id}")
            print(f"Score: {comment.score}")
            print(f"Content: {comment.content}")
            print(f"Has Replies: {'Yes' if comment_with_replies.has_replies else 'No'}")
            print("---")

        response = retrieve_most_upvoted_comments_on_a_comment(stub, 1, 2)

        # Process and display the response
        for comment_with_replies in response.comment:
            print(f"Comment ID: {comment_with_replies.comment.id}")
            print(f"Content: {comment_with_replies.comment.content}")
            print(f"Score: {comment_with_replies.comment.score}")
            print("Replies:")
            for reply in comment_with_replies.replies:
                print(f"  Reply ID: {reply.id}, Content: {reply.content}, Score: {reply.score}")
            print("---")

if __name__ == '__main__':
    run()