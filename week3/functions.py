def func(x):
    return 3*x**2

def pow(x, y):
    if y == 0:
        return 1.
    else:
        return pow(x, y - 1)*x

if __name__ == '__main__':
    print(func(432))
    print(pow(3, 32))

    y = func

    print(y)
    print(type(y))

    print(y(3))

    #print(pow(y, 3))

    import urllib.request

    web_page = urllib.request.urlopen('https://www.google.ca').read()

    print(web_page)