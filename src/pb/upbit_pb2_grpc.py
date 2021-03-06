# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import upbit_pb2 as upbit__pb2


class UpbitApiServerStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Ping = channel.unary_unary(
                '/upbitapiserver.UpbitApiServer/Ping',
                request_serializer=upbit__pb2.PingRequest.SerializeToString,
                response_deserializer=upbit__pb2.PingReply.FromString,
                )
        self.ListCoin = channel.unary_unary(
                '/upbitapiserver.UpbitApiServer/ListCoin',
                request_serializer=upbit__pb2.ListCoinRequest.SerializeToString,
                response_deserializer=upbit__pb2.ListCoinReply.FromString,
                )
        self.TickerCoin = channel.unary_unary(
                '/upbitapiserver.UpbitApiServer/TickerCoin',
                request_serializer=upbit__pb2.TickerCoinRequest.SerializeToString,
                response_deserializer=upbit__pb2.TickerCoinReply.FromString,
                )


class UpbitApiServerServicer(object):
    """The greeting service definition.
    """

    def Ping(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCoin(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TickerCoin(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UpbitApiServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Ping': grpc.unary_unary_rpc_method_handler(
                    servicer.Ping,
                    request_deserializer=upbit__pb2.PingRequest.FromString,
                    response_serializer=upbit__pb2.PingReply.SerializeToString,
            ),
            'ListCoin': grpc.unary_unary_rpc_method_handler(
                    servicer.ListCoin,
                    request_deserializer=upbit__pb2.ListCoinRequest.FromString,
                    response_serializer=upbit__pb2.ListCoinReply.SerializeToString,
            ),
            'TickerCoin': grpc.unary_unary_rpc_method_handler(
                    servicer.TickerCoin,
                    request_deserializer=upbit__pb2.TickerCoinRequest.FromString,
                    response_serializer=upbit__pb2.TickerCoinReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'upbitapiserver.UpbitApiServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UpbitApiServer(object):
    """The greeting service definition.
    """

    @staticmethod
    def Ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/upbitapiserver.UpbitApiServer/Ping',
            upbit__pb2.PingRequest.SerializeToString,
            upbit__pb2.PingReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListCoin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/upbitapiserver.UpbitApiServer/ListCoin',
            upbit__pb2.ListCoinRequest.SerializeToString,
            upbit__pb2.ListCoinReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TickerCoin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/upbitapiserver.UpbitApiServer/TickerCoin',
            upbit__pb2.TickerCoinRequest.SerializeToString,
            upbit__pb2.TickerCoinReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
