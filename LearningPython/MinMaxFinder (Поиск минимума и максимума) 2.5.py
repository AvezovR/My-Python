nums_list = []

N = int(input('Кол-во чисел в списке: '))

for _ in range(N):
    num = int(input('Очередное число: '))

    nums_list.append(num)
    print(nums_list)

    maximum = nums_list[0]
    minimum = nums_list[0]

for num in nums_list:
    print(num)

    if num > maximum:
        maximum = num

    if num < minimum:
        minimum = num


print('Максимальное число в списке:', maximum)

print('Минимальное число в списке:', minimum)
