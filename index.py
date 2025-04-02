import time
from PriceCoinStockExchange import coinSum
from spredCoin import spred
from SendSpred import sp
from newJSONFile import NJ

def main():
    i = 0
    while True:
        time.sleep(10)
        i += 1
        print(i)
        coinSum()
        spred()
        if i == 1:
            # print(time)
            sp()
            time.sleep(5)
            NJ()
            i = 0
main()