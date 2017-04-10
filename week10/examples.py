def factorial(n):
    if n == 0:
        return 1 # Sometimes referred to as the "base case", which terminates the recursion
    else:
        return n*factorial(n - 1)

print(factorial(4))

def power(x, n):
    if n == 0:
        return 1
    else:
        return x*pow(x, n - 1)

print('6! =', factorial(6))
print('2^6 =', power(2, 6))

phrase = 'To be or not to be, that is the question.'
print(phrase.replace(',', '...')) # For dramatic effect

class Terminator:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return "I am {}.".format(self.name)

    def say_something_cool(self):
        return "I'll be back."

t_100 = Terminator('Arnold Schwarzenegger')
print(t_100.introduce())
