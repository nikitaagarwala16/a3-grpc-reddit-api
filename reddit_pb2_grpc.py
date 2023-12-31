# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import reddit_pb2 as reddit__pb2


class RedditServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreatePost = channel.unary_unary(
                '/redditapi.RedditService/CreatePost',
                request_serializer=reddit__pb2.CreatePostRequest.SerializeToString,
                response_deserializer=reddit__pb2.CreatePostResponse.FromString,
                )
        self.VoteOnPost = channel.unary_unary(
                '/redditapi.RedditService/VoteOnPost',
                request_serializer=reddit__pb2.VoteOnPostRequest.SerializeToString,
                response_deserializer=reddit__pb2.VoteOnPostResponse.FromString,
                )
        self.RetrievePost = channel.unary_unary(
                '/redditapi.RedditService/RetrievePost',
                request_serializer=reddit__pb2.RetrivePostRequest.SerializeToString,
                response_deserializer=reddit__pb2.RetrievePostResponse.FromString,
                )
        self.CreateComment = channel.unary_unary(
                '/redditapi.RedditService/CreateComment',
                request_serializer=reddit__pb2.CreateCommentRequest.SerializeToString,
                response_deserializer=reddit__pb2.CreateCommentResponse.FromString,
                )
        self.VoteOnComment = channel.unary_unary(
                '/redditapi.RedditService/VoteOnComment',
                request_serializer=reddit__pb2.VoteOnCommentRequest.SerializeToString,
                response_deserializer=reddit__pb2.VoteOnCommentResponse.FromString,
                )
        self.GetMostUpvotedCommentsOnPost = channel.unary_unary(
                '/redditapi.RedditService/GetMostUpvotedCommentsOnPost',
                request_serializer=reddit__pb2.GetMostUpvotedCommentsOnPostRequest.SerializeToString,
                response_deserializer=reddit__pb2.GetMostUpvotedCommentsOnPostResponse.FromString,
                )
        self.GetMostUpvotedCommentsOnComment = channel.unary_unary(
                '/redditapi.RedditService/GetMostUpvotedCommentsOnComment',
                request_serializer=reddit__pb2.GetMostUpvotedCommentsOnCommentRequest.SerializeToString,
                response_deserializer=reddit__pb2.GetMostUpvotedCommentsOnCommentResponse.FromString,
                )
        self.MonitorPost = channel.unary_unary(
                '/redditapi.RedditService/MonitorPost',
                request_serializer=reddit__pb2.MonitorPostRequest.SerializeToString,
                response_deserializer=reddit__pb2.MonitorPostResponse.FromString,
                )


class RedditServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreatePost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VoteOnPost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RetrievePost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateComment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VoteOnComment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMostUpvotedCommentsOnPost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMostUpvotedCommentsOnComment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MonitorPost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RedditServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreatePost': grpc.unary_unary_rpc_method_handler(
                    servicer.CreatePost,
                    request_deserializer=reddit__pb2.CreatePostRequest.FromString,
                    response_serializer=reddit__pb2.CreatePostResponse.SerializeToString,
            ),
            'VoteOnPost': grpc.unary_unary_rpc_method_handler(
                    servicer.VoteOnPost,
                    request_deserializer=reddit__pb2.VoteOnPostRequest.FromString,
                    response_serializer=reddit__pb2.VoteOnPostResponse.SerializeToString,
            ),
            'RetrievePost': grpc.unary_unary_rpc_method_handler(
                    servicer.RetrievePost,
                    request_deserializer=reddit__pb2.RetrivePostRequest.FromString,
                    response_serializer=reddit__pb2.RetrievePostResponse.SerializeToString,
            ),
            'CreateComment': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateComment,
                    request_deserializer=reddit__pb2.CreateCommentRequest.FromString,
                    response_serializer=reddit__pb2.CreateCommentResponse.SerializeToString,
            ),
            'VoteOnComment': grpc.unary_unary_rpc_method_handler(
                    servicer.VoteOnComment,
                    request_deserializer=reddit__pb2.VoteOnCommentRequest.FromString,
                    response_serializer=reddit__pb2.VoteOnCommentResponse.SerializeToString,
            ),
            'GetMostUpvotedCommentsOnPost': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMostUpvotedCommentsOnPost,
                    request_deserializer=reddit__pb2.GetMostUpvotedCommentsOnPostRequest.FromString,
                    response_serializer=reddit__pb2.GetMostUpvotedCommentsOnPostResponse.SerializeToString,
            ),
            'GetMostUpvotedCommentsOnComment': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMostUpvotedCommentsOnComment,
                    request_deserializer=reddit__pb2.GetMostUpvotedCommentsOnCommentRequest.FromString,
                    response_serializer=reddit__pb2.GetMostUpvotedCommentsOnCommentResponse.SerializeToString,
            ),
            'MonitorPost': grpc.unary_unary_rpc_method_handler(
                    servicer.MonitorPost,
                    request_deserializer=reddit__pb2.MonitorPostRequest.FromString,
                    response_serializer=reddit__pb2.MonitorPostResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'redditapi.RedditService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RedditService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreatePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/redditapi.RedditService/CreatePost',
            reddit__pb2.CreatePostRequest.SerializeToString,
            reddit__pb2.CreatePostResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VoteOnPost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/redditapi.RedditService/VoteOnPost',
            reddit__pb2.VoteOnPostRequest.SerializeToString,
            reddit__pb2.VoteOnPostResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RetrievePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/redditapi.RedditService/RetrievePost',
            reddit__pb2.RetrivePostRequest.SerializeToString,
            reddit__pb2.RetrievePostResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateComment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/redditapi.RedditService/CreateComment',
            reddit__pb2.CreateCommentRequest.SerializeToString,
            reddit__pb2.CreateCommentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VoteOnComment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/redditapi.RedditService/VoteOnComment',
            reddit__pb2.VoteOnCommentRequest.SerializeToString,
            reddit__pb2.VoteOnCommentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMostUpvotedCommentsOnPost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/redditapi.RedditService/GetMostUpvotedCommentsOnPost',
            reddit__pb2.GetMostUpvotedCommentsOnPostRequest.SerializeToString,
            reddit__pb2.GetMostUpvotedCommentsOnPostResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMostUpvotedCommentsOnComment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/redditapi.RedditService/GetMostUpvotedCommentsOnComment',
            reddit__pb2.GetMostUpvotedCommentsOnCommentRequest.SerializeToString,
            reddit__pb2.GetMostUpvotedCommentsOnCommentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MonitorPost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/redditapi.RedditService/MonitorPost',
            reddit__pb2.MonitorPostRequest.SerializeToString,
            reddit__pb2.MonitorPostResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
