enter_text = input('Введите строку: ')
number_text = int(input('Номер символа: '))
count = 0

print('Символ слева', enter_text[number_text - 2])
print('Символ справа', enter_text[number_text])

for i in enter_text:
    if i == enter_text[number_text - 1]:
        count += 1
if count == 1:
    print (f'Таких же символов нет')
if count == 2:
    print(f'Есть ровно один такой же символ')