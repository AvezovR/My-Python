N = int(input('Кол0во чисел в списке: '))
num_count = []
for count in range(N):
    print('Введите',count + 1, 'число', end=' ' )
    num = int(input())
    num_count.append(num)


divider = int(input('\nВведите делитель:'))
print()
mun_count_i =[]
for count in range(N):
    number = num_count[count]
    if number % divider == 0:
        mun_count_i.append(count)
        print(f'Индекс числа {number}: {count}')
print('Сумма индексов:', sum(mun_count_i))


