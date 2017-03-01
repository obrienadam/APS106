from math import cos, sin, tan, cos

# bisection search
def bisection(a, b, f):
    for i in range(0, 100):
        x = (a + b)/2

        if abs(f(x)) < 1e-6:
            break

        if f(a) < f(b): # must know which way function is going
            if f(x) < 0.:
                a = x
            else:
                b = x
        else:
            if f(x) > 0.:
                a = x
            else:
                b = x

    return x, i

# approximate newton search
def approx_newton(x, h, f):
    for i in range(0, 100):
        x = x - h*f(x)/(f(x + h) - f(x))

        if abs(f(x)) < 1e-6:
            break

    return x, i

if __name__ == '__main__':
    """
    Note: since trig functions have multiple roots, care is needed when choosing search intervals/initial guesses
    """

    # Should be pi
    print(bisection(1, 4, sin))
    print(approx_newton(2, 0.0001, sin))

    # Should be 3pi/2
    print(bisection(4, 6, cos))
    print(approx_newton(5, 0.0001, cos))

    # Should be pi
    print(bisection(2, 4, tan))
    print(approx_newton(2, 0.0001, tan))