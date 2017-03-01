from primes import PRIMES

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

    return terms

def fibonacci_primes(num_terms):

    terms = set(fibonacci(num_terms))

    if max(terms) > max(PRIMES):
        print('Warning: the primes set is not large enough!')

    return terms.intersection(PRIMES)

if __name__ == '__main__':
    num_terms = int(input('How many fibonacci terms do you wish to check?: '))
    print('Primes found:', fibonacci_primes(num_terms))