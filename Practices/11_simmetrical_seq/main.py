# TODO здесь писать код
subsequence = []
count_of_numbers = int(input('Количество чисел: '))

for i in range(count_of_numbers):
    print('Число: ', end='')
    number = int(input())
    subsequence.append(number)
print('Последовательность:', subsequence)

need_numbers = 0
required_numbers = []

if subsequence == subsequence[::-1]:
    print('Последовательность симметрична')
else:
    for i in range(count_of_numbers):
        if subsequence == subsequence[::-1]:
            break
        else:
            subsequence.insert(len(subsequence)-i, subsequence[i])
            need_numbers += 1
            required_numbers.insert(-len(subsequence), subsequence[i])
    print('Нужно приписать чисел:', need_numbers)
    print('Сами числа:', required_numbers)

