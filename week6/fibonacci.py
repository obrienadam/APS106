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

if __name__ == '__main__':
    terms = fibonacci(int(input("Enter number of terms: ")))
    print(terms)