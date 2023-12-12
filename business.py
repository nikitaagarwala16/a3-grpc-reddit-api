def retrieve_post(client, post_id):
    post_response = client.retrieve_post(post_id)
    if not post_response or not post_response.post:
        return None  # Post not found
    return post_response.post
def retrieve_most_upvoted_comments_under_post(client, post_id):
    post = retrieve_post(client, post_id)
    if not post:
        return None, None  # Post not found, return None for both post and comments

    comments_response = client.retrieve_most_upvoted_comments_on_a_post(post_id, n=5)
    if not comments_response or not comments_response.comments:
        return post, None  # Comments not found

    return post, comments_response.comments
def retrieve_most_upvoted_comments_under_comment(client, post_id):
    post, comments = retrieve_most_upvoted_comments_under_post(client, post_id)
    if not comments:
        return post, None, None  # No comments to expand

    most_upvoted_comment = comments[0]
    expanded_comment = client.retrieve_most_upvoted_comments_on_a_comment(most_upvoted_comment.comment.id, n=1)
    return post, most_upvoted_comment, expanded_comment

def retrieve_most_upvoted_reply_under_comment(client, post_id):
    post, comments = retrieve_most_upvoted_comments_under_post(client, post_id)
    if not comments:
        return post, None, None  # No comments to expand

    most_upvoted_comment = comments[0]
    expanded_comment = client.retrieve_most_upvoted_comments_on_a_comment(most_upvoted_comment.comment.id, n=1)

    if not expanded_comment or not expanded_comment.comment or not expanded_comment.comment[0].replies:
        return post, most_upvoted_comment, None  # No replies found

    most_upvoted_reply = expanded_comment.comment[0].replies[0]
    return post, most_upvoted_comment, most_upvoted_reply

