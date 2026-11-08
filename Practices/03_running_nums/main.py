# TODO здесь писать код

shift = int(input('Сдвиг: '))
initial_list = [1, 2, 3, 4, 5]

print('Изначальный список:', initial_list)

shifted_list = initial_list[-shift:] + initial_list[:-shift]

print('Сдвинутый список:', shifted_list)
