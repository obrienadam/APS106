def fibonacci(num_terms):

    terms = []

    if num_terms > 0:
        terms.append(0)

    if num_terms > 1:
        terms.append(1)
    else:
        return terms

    for i in range(2, num_terms):
        terms.append(terms[-2] + terms[-1])

    return set(terms)

primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67}
print(fibonacci(100).intersection(primes))


iterable = fibonacci(10)

for item in iterable:
    print(item)

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21]
items = ['stimpack', 'duct tape', 'radaway', ['eggs', 13]]

items = tuple(items)[2:3]

item = ('eggs', 13)
item, quantity = item