from random import randint

def pow(x, y):
    if y == 0:
        return 1

    return x*pow(x, y - 1)

def factorial(x):
    if x == 0:
        return 1

    return x*factorial(x - 1)

if __name__ == '__main__':
    x = randint(1, 9)
    y = randint(0, 9)

    print('{}^{} = {}'.format(x, y, pow(x, y)))

    x = randint(1, 20)

    print('{}! = {}'.format(x, factorial(x)))