# TODO здесь писать код
quantity_gcart = int(input('Количество видеокарт: '))
list_gcart = []

for i in range(quantity_gcart):
    print('Видеокарта', i+1, end = ':   ')
    name_gcart = input()
    list_gcart.append(name_gcart)

print('\nСтарый список видеокарт:', list_gcart)

max_gcart = max(list_gcart)
while max_gcart in list_gcart:
    list_gcart.remove(max_gcart)

print('Новый список видеокарт:', list_gcart)
