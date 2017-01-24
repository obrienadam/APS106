amount = float(input('Enter amount: '))

loonies = amount//1.
amount -= loonies

quarters = amount//.25
amount -= quarters*.25

dimes = amount//.1
amount -= dimes*.1

nickels = amount//0.05
amount -= nickels*.05

print(loonies, quarters, dimes, nickels, amount)