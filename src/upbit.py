import requests


def log(str_val):
    print(str_val) 

class upbitApi:
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


if __name__ == "__main__":
    upbit = upbitApi()
    market_lsit = upbit.list_market()

    market = market_lsit[0]["market"]
    print(market) # KRW-BTC
    print(upbit.ticker(market))
    #print(upbit.candle(market))