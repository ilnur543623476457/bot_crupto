import json
import requests
# from apiAuto import torgapi


TOKEN = "8190004571:AAElpcr78xHH9Wgppygb8DqkLrCwR_LyguU"
chat_id = "-4728759230"

def sp():
    with open('SpredCoin.json', 'r') as file:
        fl = json.load(file)
        src = []
        for i in fl:
            if len(fl[i]) >= 1: # колличство спреда
                coin = fl[i][0]
                # url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={coin}"
                # requests.get(url)
                print(coin)
                src.append(coin)

        try:
            # print(src)
            srcarr = []
            for i in src:
                srcarr.append(i.split(' ')[4])
            # print(srcarr)
            src_max = max(srcarr)
            dest = [src_max for i in range(srcarr.count(src_max))]

            # print(dest)

            for i in src:
                # print(i)
                if i.split(' ')[4] == dest[0]:
                    # print(i)
                    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={i}"
                    requests.get(url)
                    if i.split(' ')[1] == 'Bybit':
                        coin = i.split(' ')[0]
                        # i = coin.replace('USDT', '')
                        print('Bybit ->', coin)
                        # torgapi(coin)
                    if i.split(' ')[1] == 'Mexc':
                        coin = i.split(' ')[0]
                        # i = coin.replace('USDT', '')
                        print('Mexc ->', coin)
                        # torgapi(coin)
        except:
            pass


