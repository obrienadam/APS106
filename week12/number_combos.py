class Node:
    def __init__(self, num, nums, sum=0):
        self.num = num
        self.nums = nums
        self.sum = sum + self.num

        if nums:
            self.plus = Node(nums[0], nums[1:], self.sum)
            self.minus = Node(-nums[0], nums[1:], self.sum)

    def get_combos(self, num, combo=[]):
        combo = combo + [self.num]

        if not self.nums and self.sum == num:
            return [combo]
        elif not self.nums:
            return []
        elif self.sum + sum(self.nums[:]) < num: # If either of the next two conditions is true, this combo can't possibly be a solution
            return []
        elif self.sum - sum(self.nums[:]) > num:
            return []
        else:
            return self.plus.get_combos(num, combo) + self.minus.get_combos(num, combo)

if __name__ == '__main__':
    nums = list(range(2, 10))
    tree = Node(1, nums)

    num = int(input('Enter a number: '))

    print('The following combos sum to the number {}.'.format(num))
    for combo in tree.get_combos(num):
        print(str(combo)[1:-1].replace(', -', ' - ').replace(', ', ' + '), '=', 3)
