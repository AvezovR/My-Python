from itertools import groupby
cod = input('Введите строку: ')

result = [(char, str(len(list(group)))) for char, group in groupby(cod)]
flat_list = [item for sublist in result for item in sublist]

print('Закодированная строка:', ''.join(flat_list))