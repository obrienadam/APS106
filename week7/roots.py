from math import sqrt

def func(f):
    return 0.03 - f/(1. - f)*sqrt(7./(2. + f))

def secant(x, h, f):
    for i in range(0, 100):
        x = x - h*f(x)/(f(x) - f(x + h))

if __name__ == '__main__':
    print(secant(0.3, 0.00001, func))