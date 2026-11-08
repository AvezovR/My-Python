user_input = input("Введите строку: ")
nums = []
for x in user_input:
    if '0'<=x<='9':
        nums.append(x)
sum_nums = set(nums)

print(f'Различные цифры строки: {''.join(sorted(sum_nums))}')

