import random

def change(nums):
    nums = list(nums)
    index = random.randint(0, len(nums)-1)
    value = random.randint(100, 1000)
    nums[index] = value
    return tuple(nums), value


my_nums = 1, 2, 3, 4, 5
sum_rand_val = 0
for i in range(2):
    new_nums, rand_val = change(my_nums)
    sum_rand_val += rand_val
    print(new_nums, rand_val)
print(sum_rand_val)

