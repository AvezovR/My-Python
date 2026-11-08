numbers = [3,7,5]

while True:

 number = int(input('Новое число: '))

 numbers.append(number)

 print('Текущий список чисел:', numbers)

 for x in numbers:

   print(x ** 2, x ** 3, x ** 4)

 print()