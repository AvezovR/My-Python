# TODO здесь писать код
sizes_roller_skates = []
total_rollers = int(input('Количество роликов: '))
for roll in range(1, total_rollers + 1):
    print('Размер пары', roll, end=': ')
    size_roll = int(input())
    sizes_roller_skates.append(size_roll)

lucky_guy = 0
total_people = int(input('Количество людей: '))
for shoe in range(1, total_people + 1):
    print('Размер ноги человека', shoe, end=': ')
    size_shoe = int(input())
    if size_shoe in sizes_roller_skates:
        sizes_roller_skates.remove(size_shoe)
        lucky_guy += 1

print('Наибольшее количество людей, которые могут взять ролики:', lucky_guy)