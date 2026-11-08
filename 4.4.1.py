numb_a = int(input("Введите первое число: "))
numb_b = int(input("Введите второе число: "))

numb_price = [x for x in range(numb_a, numb_b + 1) if x % 2 == 0]

print(numb_price)