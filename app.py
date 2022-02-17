import json
import argparse

# get input form command line, use -part1 and -part2 flags to choose challenge 1 or 2  
parser = argparse.ArgumentParser()

parser.add_argument("-part1", "--p1", help="Part 1 - Calculate the total value of a stock portfolio")
parser.add_argument("-bonus", "--b1", help="Part 2 - Maximize profits")
args = parser.parse_args()

if args.b1 is None:
    #Part 1 - Calculate the total value of a stock portfolio
    f = open('stocks.json')
    datas = json.load(f)

    stocks = args.p1.split(',')
    total = 0
    for stock in stocks:
        name = stock.split(':')[0]
        for data in datas:
            if data['ticker'] == name:
                price = data['close']
        total += price * float(stock.split(':')[1])

    print(total)
    f.close()
else:
    #Part 2 - Maximize profits
    prices = args.b1.split(',')
    object = map(int, prices)
    price_list = list(object) # map string to int list

    length = len(price_list)
    res = 0
    minPriceSoFar = price_list[0]
    for i in range(1, length):
        res = max(res, price_list[i] - minPriceSoFar)
        minPriceSoFar = min(minPriceSoFar, price_list[i])

    print(res)





