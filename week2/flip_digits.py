number = int(input('Enter a 3 digit integer: '))

d1 = number//100
number %= 100

d2 = number//10
number %= 10

d3 = number

print(d3*100 + d2*10 + d1)