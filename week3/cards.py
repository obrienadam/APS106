from random import randint

def card():
    return randint(1, 13), randint(1, 4)

if __name__ == '__main__':
    print(card())