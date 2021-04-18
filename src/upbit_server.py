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
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging
import requests
import grpc
from google.protobuf.json_format import Parse
import sys; sys.path.append("pb")
from pb.upbit_pb2 import *
from pb.upbit_pb2_grpc import *



def log(str_val):
    print(str_val)

class UpbitApi:
    URL = "https://api.upbit.com/v1/"
    LIST_URL = "market/all"
    CANDLE_URL = "candles/"
    TICKER_URL = "ticker"

    def __init__(self):
        pass
    def list_market(self):
        url = self.URL + self.LIST_URL

        querystring = {"isDetails":"false"}
        response = requests.request("GET", url, params=querystring)

        if (response.status_code == 200):
            return response.json()
        else:
            log("서버 응답 실패 "  + response.text)
            return None

    def candle(self, market, to=None, count=200, time_type="m", time_val="1"):
        url = self.URL + self.CANDLE_URL

        if (count > 200):
            log("200 개 이상 캔들 요청 불가")
            return None

        if (time_type == "m"): #분
            url += "minutes"
        elif(time_type == "d"): #시
            url += "days"
        elif(time_type == "w"): #주
            url += "weeks"
        elif(time_type == "y"): #월
            url += "months"
        else:
            log("잘못된 시간 형식")
            return None

        url += "/" + time_val

        querystring = {
            "market" : market,
            "to" : to,
            "count" : count
        }
        response = requests.request("GET", url, params=querystring)
        if (response.status_code == 200):
            return response.json()
        else:
            log("서버 응답 실패 " + response.text)
            return None

    def ticker(self, markets):
        url = self.URL + self.TICKER_URL
        
        querystring = {"markets": markets}
        response = requests.request("GET", url, params=querystring)
        if (response.status_code == 200):
            return response.json()
        else:
            log("서버 응답 실패 " + response.text)
            return None

class GrpcUpbit(UpbitApiServerServicer, UpbitApi):
    def Ping(self, request, context):
        print("Ping %s" % request.text)
        return PingReply(message='Ping %s!' % request.text)

    def ListCoin(self, request, context):
        print("ListCoin")
        markets = self.list_market()
        reply = ListCoinReply()
        for m in markets:
            coin = reply.coins.add()
            coin.market = m['market']
            coin.korean_name = m['korean_name']
            coin.english_name = m['english_name']
        return reply

    def TickerCoin(self, request, context):
        print("TickerCoin " + request.markets)
        tickers = self.ticker(request.markets)
        reply = TickerCoinReply()
        for t in tickers:
            coin = reply.coins.add()
            coin.market = t['market']
            coin.trade_date = t['trade_date']
            coin.trade_time = t['trade_time']
            coin.trade_date_kst = t['trade_date_kst']
            coin.trade_time_kst = t['trade_time_kst']
            coin.opening_price = t['opening_price']
            coin.high_price = t['high_price']
            coin.low_price = t['low_price']
            coin.trade_price = t['trade_price']
            coin.prev_closing_price = t['prev_closing_price']
            coin.change = t['change']
            coin.change_price = t['change_price']
            coin.change_rate = t['change_rate']
            coin.signed_change_price = t['signed_change_price']
            coin.signed_change_rate = t['signed_change_rate']
            coin.trade_volume = t['trade_volume']
            coin.acc_trade_price = t['acc_trade_price']
            coin.acc_trade_price_24h = t['acc_trade_price_24h']
            coin.acc_trade_volume = t['acc_trade_volume']
            coin.acc_trade_volume_24h = t['acc_trade_volume_24h']
            coin.highest_52_week_price = t['highest_52_week_price']
            coin.highest_52_week_date = t['highest_52_week_date']
            coin.lowest_52_week_price = t['lowest_52_week_price']
            coin.lowest_52_week_date = t['lowest_52_week_date']
            coin.timestamp = t['timestamp']
        return reply


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_UpbitApiServerServicer_to_server(GrpcUpbit(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
