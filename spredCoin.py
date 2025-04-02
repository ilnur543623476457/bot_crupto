import json

def spred():

    with open('coinBybit.txt', "r") as file:
        arrBybit = []
        for coin in file:
            coin = coin.split('\n')[0]
            arrBybit.append(coin)
    with open('coinMexc.txt', "r") as file:
        arrMexc = []
        for coin in file:
            coin = coin.split('\n')[0]
            arrMexc.append(coin)
    # with open('coinOKX.txt', "r") as file:
    #     arrOkx = []
    #     for coin in file:
    #         coin = coin.split('\n')[0]
    #         arrOkx.append(coin)
    # with open('coinBinance.txt', "r") as file:
    #     arrBinance = []
    #     for coin in file:
    #         coin = coin.split('\n')[0]
    #         arrBinance.append(coin)
    # with open('coinBitget.txt', "r") as file:
    #     arrBitget = []
    #     for coin in file:
    #         coin = coin.split('\n')[0]
    #         arrBitget.append(coin)
    # with open('coinKraken.txt', "r") as file:
    #     arrKraken = []
    #     for coin in file:
    #         coin = coin.split('\n')[0]
    #         arrKraken.append(coin)
    # with open('coinKuCoin.txt', "r") as file:
    #     arrKuCoin = []
    #     for coin in file:
    #         coin = coin.split('\n')[0]
    #         arrKuCoin.append(coin)

    a = [
        arrBybit,
        arrMexc,
        # arrOkx,
        # arrBinance,
        # arrBitget,
        # # arrKraken,
        # arrKuCoin
    ]
    b = [
        arrBybit,
        arrMexc,
        # arrOkx,
        # arrBinance,
        # arrBitget,
        # # arrKraken,
        # arrKuCoin
    ]

    for i in a:
        for u in b:
            if i == u:
                pass
            else:
                for v1 in i:
                    for v2 in u:
                        if v1.split(' ')[0] == v2.split(' ')[0]:

                            spredTo = 101.4
                            comis = 0.1
                            capital = 100

                            nameCryptoBirja1 = v1.split(' ')[5]
                            nameCryptoBirja2 = v2.split(' ')[5]
                            nameCoin = v1.split(' ')[0]


                            arjsonspred = f'{nameCoin}/{nameCryptoBirja1} -> {nameCryptoBirja2}'

                            try:
                                pocupcaOne = float(v1.split(' ')[4])  # green
                                prodajaOne = float(v2.split(' ')[2])  # red

                                formula_bin_byb = (capital / pocupcaOne) * prodajaOne - comis - comis - comis
                            except:
                                continue

                            if formula_bin_byb > spredTo:
                                coinex = f'{nameCoin} {nameCryptoBirja1} -> {nameCryptoBirja2} {formula_bin_byb} red {pocupcaOne} green {prodajaOne}'
                                print(coinex)
                                with open('SpredCoin.json', 'r') as file:
                                    fl = json.load(file)
                                    fl[arjsonspred] += [coinex]
                                with open('SpredCoin.json', 'w') as file:
                                    json.dump(fl, file, indent=3)
