from random import randint

def shuffle(items):
    items = items[:]
    shuffled_items = []

    while len(items) > 0:
        index = randint(0, len(items) - 1)
        shuffled_items.append(items.pop(index))

    return shuffled_items

if __name__ == '__main__':
    cards = list(range(52))
    print(shuffle(cards))