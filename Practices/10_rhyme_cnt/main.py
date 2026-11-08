# TODO здесь писать код

total_people = int(input('Количество человек: '))
people = []
for i in range(total_people):
    people.append(i+1)

number = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {number}-й человек')

index = 0
print(f"\nТекущий круг людей: {people}")
print(f"Начало счёта с номера {people[0]}")

while len(people) > 1:
    index = (index + number-1) % len(people)
    person = people[index]
    print(f"Выбывает человек под номером {person}")
    people.pop(index)
    if len(people) > 1:
        print(f"\nТекущий круг людей: {people}")
        print(f"Начало счёта с номера {(people[index]) if (person <= len(people) or person <= max(people)) else people[0]}")

print(f"\nОстался человек под номером {people}")
