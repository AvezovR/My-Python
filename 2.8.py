text = input('Введите строку: ')
text_list = list(text)
print(text_list)
count = 0
count_i = 0
symb = ';'
for i in text_list:
    count_i += 1
    if i == ':':
        count += 1
        text_list[count_i - 1] = symb
for i in text_list:
    print(i, end=' ')
print('\nКол-во замен:', count)