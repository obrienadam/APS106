"""
Note: you're not expected to know this for exams/labs. It's just for interest/fun! This will return any stock symbol
in the format used in the other exercise, ie a dictionary of lists containing relevant info.
"""
from datetime import datetime
from urllib import request

def get_quotes(symbol, start, end, interval='d'):
    """
    (str, str, str, str) -> dict
    Gets the price data for a specified stock symbol between start and end at a specified interfal, and returns
    a dictionary containing that data.
    """
    start = datetime.strptime(start, '%Y-%m-%d')
    end = datetime.strptime(end, '%Y-%m-%d')
    data = str(request.urlopen('http://chart.finance.yahoo.com/table.csv?s={}&a={}&b={}&c={}&d={}&e={}&f={}&g={}&ignore=.csv'.format(symbol,
                           start.month - 1, start.day, start.year,
                           end.month - 1, end.day, end.year,
                           interval)).read(), encoding='utf-8').split('\n')

    prices = {}
    headers = data.pop(0).strip().split(',')

    for header in headers:
        prices[header] = []

    for line in data:
        if not line: # line may be empty
            continue

        line = line.strip().split(',')
        for i in range(len(headers)):
            try:
                prices[headers[i]].append(float(line[i]))
            except ValueError:
                prices[headers[i]].append(line[i])

    return prices

def write_to_file(symbol, prices):
    """
    (str, dict) -> None
    Takes data for a stock symbol as a dict and writes it to a file. Always names the file {symbol}.csv
    """
    headers = prices.keys()
    data = prices.values()

    with open(symbol.upper() + '.csv', 'w') as f:
        f.write(','.join(headers) + '\n')

        for vals in zip(*data):
            f.write(','.join(map(str, vals)) + '\n')

if __name__ == '__main__':
    symbol = 'aapl'
    prices = get_quotes(symbol, '2016-03-05', '2017-03-05', 'd')
    write_to_file(symbol, prices)