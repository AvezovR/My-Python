while True:
    grats_template = input('Введите шаблон поздравления,'
                            'в шаблоне можно использовать'
                            'конструкцию {name} и {age}: ')
    if '{name}' in grats_template and '{age}' in grats_template:
        break
    print('Ошибка, отсутствует одна или две конструкции')

names_lst = input('Список людей через запятую: ').split(',')
ages_lst = input('Возраст людей через пробел: ').split()
ages = [int(age) for age in ages_lst]
for i_man in range(len(names_lst)):
    print(grats_template.format(name=names_lst[i_man], age=ages_lst[i_man]))

people = [' '.join([names_lst[i_man], ages_lst[i_man]]) for i_man in range(len(names_lst))]
print(people)
