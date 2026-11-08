phone_book = {}
while True:
    print('Текущие контакты на телефоне:')
    if not phone_book:
        print('<Пусто>')
    for i_info in phone_book:
        print(i_info,':', phone_book[i_info])
    name_abonent = input('Введите имя: ')
    if name_abonent in phone_book:
        print('Ошибка: такое имя уже существует.')
        continue
    nomber_abonent = input('Введите номер телефона: ')
    phone_book[name_abonent] = nomber_abonent
    continue
