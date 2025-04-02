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
with open('coinOKX.txt', "r") as file:
    arrOkx = []
    for coin in file:
        coin = coin.split('\n')[0]
        arrOkx.append(coin)
with open('coinBinance.txt', "r") as file:
    arrBinance = []
    for coin in file:
        coin = coin.split('\n')[0]
        arrBinance.append(coin)
with open('coinBitget.txt', "r") as file:
    arrBitget = []
    for coin in file:
        coin = coin.split('\n')[0]
        arrBitget.append(coin)
with open('coinKraken.txt', "r") as file:
    arrKraken = []
    for coin in file:
        coin = coin.split('\n')[0]
        arrKraken.append(coin)
with open('coinKuCoin.txt', "r") as file:
    arrKuCoin = []
    for coin in file:
        coin = coin.split('\n')[0]
        arrKuCoin.append(coin)



arrBybit_arrMexc = []
for i in arrBybit:
    for u in arrKuCoin:
        if i.split(' ')[0] == u.split(' ')[0]:
            arrBybit_arrMexc.append(u.split(' ')[0])
print(arrBybit_arrMexc)


# arrBybit_arrMexc = list(set(arrBybit) & set(arrMexc))
# arrBybit_arrOkx = list(set(arrBybit) & set(arrOkx))
# arrBybit_arrBinance = list(set(arrBybit) & set(arrBinance))
# arrBybit_arrBitget = list(set(arrBybit) & set(arrBitget))
# arrBybit_arrKraken = list(set(arrBybit) & set(arrKraken))
# arrBybit_arrKuCoin = list(set(arrBybit) & set(arrKuCoin))
#
#
# print(arrBybit_arrMexc)
# print(arrBybit_arrOkx)
# print(arrBybit_arrBinance)
# print(arrBybit_arrBitget)
# print(arrBybit_arrKraken)
# print(arrBybit_arrKuCoin)

