films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

# TODO здесь писать код
my_list = []

print('Сколько фильмов хотите добавить?', end=' ')
number_of_films = int(input())

for i in range(number_of_films):
    print('Введите название фильма:', end=' ')
    name_film = input()
    if name_film in films:
        my_list.append(name_film)
    else:
        print(f'Ошибка: фильма {name_film} у нас нет :(')
print('Ваш список любимых фильмов:', my_list)

