def get_prices(filename):
    """
    (str)-> dict
    Takes in a filename, returns the price dictionary (assuming that file exists).
    """
    with open(filename, 'r') as f:
        headers = f.readline().strip().split(',')

        prices = {}
        for header in headers:
            prices[header] = []

        for line in f:
            line = line.strip().split(',')

            for i in range(len(line)):
                try:
                    prices[headers[i]].append(float(line[i]))
                except ValueError:
                    prices[headers[i]].append(line[i])

    return prices

def get_lowest_low(prices):
    """
    (dict)-> tuple(str, float)
    Takes in the price dictionary, returns a tuple containing the date on which the minimum closing price occurred, and the
    minimum closing price.
    """
    min_price = '', float('inf')
    for date, price in zip(prices['Date'], prices['Close']):
        if price < min_price[1]:
            min_price = date, price

    return min_price

def get_highest_high(prices):
    """
    (dict)-> tuple(str, float)
    Takes in the price dictionary, returns a tuple containing the date on which the maximum closing price occurred, and the
    maximum closing price.
    """
    max_price = '', 0.
    for date, price in zip(prices['Date'], prices['Close']):
        if price > max_price[1]:
            max_price = date, price

    return max_price

def get_range_stats(prices):
    """
    (dict)-> tuple(float, float)
    Takes in the price dictionary, returns a tuple containing average absolute price range (|close - open|), and the
    standard deviation of that trading range.
    """
    range = []

    for open, close in zip(prices['Open'], prices['Close']):
        range.append(abs(close - open))

    mean = sum(range)/len(range)

    var = 0.
    for r in range:
        var += (r - mean)**2

    var /= len(range)

    return mean, var**0.5

if __name__ == '__main__':
    symbol = input('Enter symbol: ').upper()
    prices = get_prices(symbol + '.csv')

    print('\nSymbol:', symbol)
    print('-'*96)
    print('Lowest low was ${:.2f}, and occurred on {}.'.format(*get_lowest_low(prices)[::-1]))
    print('Highest high was ${:.2f}, and occurred on {}.'.format(*get_highest_high(prices)[::-1]))
    print('Average trading range is ${:.2f}, with a standard deviation of ${:.2f}.'.format(*get_range_stats(prices)))
