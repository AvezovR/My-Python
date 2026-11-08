films = [

    'Крепкий орешек', 'Назад в будущее', 'Таксист',

    'Леон', 'Богемская рапсодия', 'Город грехов',

    'Мементо', 'Отступники', 'Деревня',

    'Проклятый остров', 'Начало', 'Матрица'

]
print('Сколько фильмов выбрать?', end=' ')
count_film = int(input())

my_films = []

while len(my_films) < (count_film +1):
    print('\nВаш текущий топ фильмов:', my_films)
    print('Название фильма:', end=' ')
    name_film = input()
    print('Команды: добавить, вставить, удалить')
    comand = input('Введите команду: ')
    if comand == 'добавить':
        if name_film in my_films:
            print('Этот фильм уже естьв вашем списке.')
        else:
            my_films.append(name_film)
    if comand == 'удалить':
        my_films.remove(name_film)
    if comand == 'вставить':
        print('На какое место вставить:', end=' ')
        place_film = int(input())
        my_films.insert(place_film + 1, name_film)
