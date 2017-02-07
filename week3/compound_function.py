from math import sin, cos
from random import random

def f1(x):
    """
        f1(...)

        Return 3.*x**2 + 2.*x + 4
    """
    return 3.*x**2 + 2.*x + 4

def f2(x):
    return 54.*sin(x) + 2.*sin(x)**2

def f3(x):
    return sin(x) + sin(x)*cos(x)

def add_funcs(f1, f2, x):
    return f1(x) + f2(x)

if __name__ == '__main__':
    help(f1)

    x = random()*10

    print('f1({}) = {}'.format(x, f1(x)))
    print('f2({}) + f3({}) = {}'.format(x, x, add_funcs(f2, f3, x)))

    """
    or we can...
    """

    print(f1.__name__, '=', f1(x))