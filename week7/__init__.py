from random import randint

nums = []
for i in range(0, randint(1, 50)):
    nums.append(randint(1, 10))

numset = set(nums)

print('The list', nums, 'has', len(nums) - len(numset), 'duplicate values!')

keys = {('a', 13), 'b'}

