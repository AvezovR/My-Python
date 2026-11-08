nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]

print(nums[:5])
print(nums[:(len(nums)-2)])
nums1 = [x for x in nums if x % 2 == 0]
print(nums1)
print(nums[::2])
print(nums[1::2])
print(nums[::-1])
print(nums[::-2])