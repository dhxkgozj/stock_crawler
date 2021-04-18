# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function
import logging
import json
import grpc
from google.protobuf.json_format import MessageToJson

import sys; sys.path.append("pb")
from pb.upbit_pb2 import *
from pb.upbit_pb2_grpc import *


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = UpbitApiServerStub(channel)
        response = stub.ListCoin(ListCoinRequest())
        result = json.loads(MessageToJson(response))
        print("client received")
        print(result["coins"][0])
        response = stub.TickerCoin(TickerCoinRequest(markets=result["coins"][0]['market']))
        result = json.loads(MessageToJson(response))
        print(result)


if __name__ == '__main__':
    logging.basicConfig()
    run()
