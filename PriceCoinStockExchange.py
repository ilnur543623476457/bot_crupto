import json
import requests

coinSelection = 'USDT'

def coinSum():
    try:
    # Bybit
        response = requests.get('https://api.bybit.com/v5/market/tickers?category=spot')
        result = response.json()
        with open('coinBybit.txt', "w") as file:
            for i in result['result']['list']:
                symbol = i['symbol']
                bid_price = i['bid1Price']
                ask_price = i['ask1Price']
                if coinSelection in symbol:
                    coin = f'{symbol} green {bid_price} red {ask_price} Bybit'
                    file.write(coin + '\n')


        # Binance
        # response = requests.get('https://api.binance.com/api/v3/ticker/bookTicker')
        # result = response.json()
        # symb = []
        # for i in result:
        #     symbol = i['symbol']
        #     bid_price = i['bidPrice']
        #     ask_price = i['askPrice']
        #     if coinSelection in symbol:
        #         coin = f'{symbol} green {bid_price} red {ask_price} Binance'
        #         symb.append(coin)
        #
        # with open('coinBinance.txt', "w") as file:
        #     with open('CoinSort.json', 'r') as rfile:
        #         fl = json.load(rfile)
        #         for i in fl['coinBinance']:
        #             for u in symb:
        #                 if u.split(' ')[0] == i:
        #                     file.write(u + '\n')



        # Bitget
        # response = requests.get('https://api.bitget.com/api/spot/v1/market/tickers')
        # result = response.json()
        # symb = []
        # for i in result['data']:
        #     symbol = i['symbol']
        #     bid_price = i['buyOne']
        #     ask_price = i['sellOne']
        #     if coinSelection in symbol:
        #         coin = f'{symbol} green {bid_price} red {ask_price} Bitget'
        #         symb.append(coin)
        #
        # with open('coinBitget.txt', "w") as file:
        #     with open('CoinSort.json', 'r') as rfile:
        #         fl = json.load(rfile)
        #         for i in fl['coinBitget']:
        #             for u in symb:
        #                 if u.split(' ')[0] == i:
        #                     file.write(u + '\n')


        # OKX
        # response = requests.get('https://www.okx.cab//api/v5/market/tickers?instType=SPOT')
        # result = response.json()
        # symb = []
        # for i in result['data']:
        #     symbol = i['instId']
        #     bid_price = i['bidPx']
        #     ask_price = i['askPx']
        #     if coinSelection in symbol:
        #         coin = f'{symbol.replace('-', '')} green {bid_price} red {ask_price} OKX'
        #         symb.append(coin)
        #
        # with open('coinOKX.txt', "w") as file:
        #     with open('CoinSort.json', 'r') as rfile:
        #         fl = json.load(rfile)
        #         for i in fl['coinOKX']:
        #             for u in symb:
        #                 if u.split(' ')[0] == i:
        #                     file.write(u + '\n')

        # KuCoin
        # response = requests.get('https://api.kucoin.com/api/v1/market/allTickers')
        # result = response.json()
        # symb = []
        # for i in result['data']['ticker']:
        #     symbol = i['symbol']
        #     bid_price = i['buy']
        #     ask_price = i['sell']
        #     if coinSelection in symbol:
        #         coin = f'{symbol.replace('-', '')} green {bid_price} red {ask_price} KuCoin'
        #         symb.append(coin)
        #
        # with open('coinKuCoin.txt', "w") as file:
        #     with open('CoinSort.json', 'r') as rfile:
        #         fl = json.load(rfile)
        #         for i in fl['coinKuCoin']:
        #             for u in symb:
        #                 if u.split(' ')[0] == i:
        #                     file.write(u + '\n')
        #

        # Mexc
        response = requests.get('https://api.mexc.com/api/v3/ticker/bookTicker')
        result = response.json()
        symb = []
        for i in result:
            symbol = i['symbol']
            bid_price = i['bidPrice']
            ask_price = i['askPrice']
            if coinSelection in symbol:
                coin = f'{symbol} green {bid_price} red {ask_price} Mexc'
                symb.append(coin)

        with open('coinMexc.txt', "w") as file:
            with open('CoinSort.json', 'r') as rfile:
                fl = json.load(rfile)
                for i in fl['coinMexc']:
                    for u in symb:
                        if u.split(' ')[0] == i:
                            file.write(u + '\n')


        # Kraken
        # response = requests.get('https://api.kraken.com/0/public/Ticker')
        # result = response.json()
        # a=[]
        # for i in result['result']:
        #     symbol = i
        #     if coinSelection in symbol:
        #         a.append(symbol)
        # lenarr = len(a)
        # symb = []
        # for i in range(lenarr):
        #     symbol = a[i]
        #     bid_price = result['result'][f'{a[i]}']['a'][0]
        #     ask_price = result['result'][f'{a[i]}']['b'][0]
        #     coin = f'{symbol} green {bid_price} red {ask_price} Kraken'
        #     symb.append(coin)
        #
        # with open('coinKraken.txt', "w") as file:
        #     with open('CoinSort.json', 'r') as rfile:
        #         fl = json.load(rfile)
        #         for i in fl['coinKraken']:
        #             for u in symb:
        #                 if u.split(' ')[0] == i:
        #                     file.write(u + '\n')
    except:
        print('не собрал')
        coinSum()
