import unittest
from unittest.mock import Mock

from business import retrieve_most_upvoted_comments_under_post,retrieve_most_upvoted_comments_under_comment, retrieve_most_upvoted_reply_under_comment, retrieve_post
#test class to test the business logic for the api
class TestRedditClientFunctions(unittest.TestCase):
    def setUp(self):
        self.mock_client = Mock()
        self.mock_client.retrieve_post.return_value = MockPostResponse()
        self.mock_client.retrieve_most_upvoted_comments_on_a_post.return_value = MockCommentsResponse(comments=[MockCommentWithReplies(comment=MockComment(id=1))])
        self.mock_client.retrieve_most_upvoted_comments_on_a_comment.return_value = MockExpandedCommentResponse(comment=[MockCommentWithReplies(replies=[MockComment(id=2)])])

    def test_retrieve_post(self):
        result = retrieve_post(self.mock_client, post_id=1)
        self.assertIsNotNone(result)
        #asserting the right post is fetched
        self.assertEqual(result.id, 1)
        self.assertEqual(result.title, "Mock Post Title")
        self.assertEqual(result.content, "Mock content")

    def test_get_most_upvoted_comments(self):
        post, comments = retrieve_most_upvoted_comments_under_post(self.mock_client, post_id=1)
        #  asserting that none of the returned items are None
        self.assertIsNotNone(post)
        self.assertIsNotNone(comments)
        self.assertEqual(len(comments), 1)
        #asserting the right comment is fetched
        self.assertEqual(comments[0].comment.id, 1)
        self.assertEqual(comments[0].comment.content, "Mock comment content")
        self.assertEqual(comments[0].comment.score, 10)

    def test_get_most_upvoted_comments_under_comment(self):
        post, most_upvoted_comment, expanded_comment = retrieve_most_upvoted_comments_under_comment(self.mock_client, post_id=1)
        # Assert that none of the returned items are None
        self.assertIsNotNone(post)
        self.assertIsNotNone(most_upvoted_comment)
        self.assertIsNotNone(expanded_comment)

        # Checking if the most_upvoted_comment is a MockCommentWithReplies instance
        self.assertIsInstance(most_upvoted_comment, MockCommentWithReplies)
        # Assert the ID of the comment within most_upvoted_comment
        self.assertEqual(most_upvoted_comment.comment.id, 1)

        # Checking if expanded_comment's 'comment' attribute is a list and has at least one comment
        self.assertGreaterEqual(len(expanded_comment.comment), 1)
        # aaserting if the right comment was returned
        self.assertEqual(expanded_comment.comment[0].comment.id, 1)

    def test_get_most_upvoted_reply(self):
        post, most_upvoted_comment, most_upvoted_reply = retrieve_most_upvoted_reply_under_comment(self.mock_client, post_id=1)
        # Assert that none of the returned items are None
        self.assertIsNotNone(post)
        self.assertIsNotNone(most_upvoted_comment)
        self.assertIsNotNone(most_upvoted_reply)
        # Asserting that the ID of the most upvoted reply is as expected
        self.assertEqual(most_upvoted_reply.id, 2)

# Mock classes
class MockPost:
    def __init__(self, id=1, title="Mock Post Title", content="Mock content"):
        self.id = id
        self.title = title
        self.content = content

class MockComment:
    def __init__(self, id=1, content="Mock comment content", score=10):
        self.id = id
        self.content = content
        self.score = score

class MockCommentWithReplies:
    def __init__(self, comment=None, replies=[]):
        self.comment = comment if comment else MockComment()
        self.replies = replies

class MockPostResponse:
    def __init__(self, post=None):
        self.post = post if post else MockPost()

class MockCommentsResponse:
    def __init__(self, comments=[]):
        self.comments = comments

class MockExpandedCommentResponse:
    def __init__(self, comment=[]):
        self.comment = comment

if __name__ == '__main__':
    unittest.main()
