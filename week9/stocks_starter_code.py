"""
This is starter code, you'll need to fill in most of it. You can take a look at some of the given code for clues as to
how dictionaries and files work.
"""

def get_prices(filename):
    """
    (str)-> dict
    Takes in a filename, returns the price dictionary (assuming that file exists).
    """
    prices = {}

    # Return the prices dictionary
    return prices

def get_lowest_low(prices):
    """
    (dict)-> tuple(str, float)
    Takes in the price dictionary, returns a tuple containing the date on which the minimum closing price occurred, and the
    minimum closing price.
    """

def get_highest_high(prices):
    """
    (dict)-> tuple(str, float)
    Takes in the price dictionary, returns a tuple containing the date on which the maximum closing price occurred, and the
    maximum closing price.
    """

def get_range_stats(prices):
    """
    (dict)-> tuple(float, float)
    Takes in the price dictionary, returns a tuple containing average absolute price range (|close - open|), and the
    standard deviation of that trading range.
    """
    range = []
    for open, close in zip(prices['Open'], prices['Close']): # Constructs a list containing the trading ranges (don't modify this loop)
        range.append(abs(close - open))

if __name__ == '__main__':
    symbol = input('Enter symbol: ').upper()
    prices = get_prices(symbol + '.csv')

    print('\nSymbol:', symbol)
    print('-'*96)
    print('Lowest low was ${:.2f}, and occurred on {}.'.format(*get_lowest_low(prices)[::-1]))
    print('Highest high was ${:.2f}, and occurred on {}.'.format(*get_highest_high(prices)[::-1]))
    print('Average trading range is ${:.2f}, with a standard deviation of ${:.2f}.'.format(*get_range_stats(prices)))