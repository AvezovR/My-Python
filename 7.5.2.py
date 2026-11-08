phone_book = {}
while True:
    faname_contact = input('Введите фамилию контакта:')
    name_contact = input('Введите имя контакта:')
    if  (faname_contact, name_contact) in phone_book.keys():
        print(f"Контакт с фамилией - {faname_contact} и именем - {name_contact} уже есть в телефонной книге")
        print(f"Обновить номер контакта?")
        answer_1 = input("Да/Нет - ")
        if answer_1.lower() == 'да':
            number_contact = int(input('Введите номер контакта:'))
            phone_book[(faname_contact, name_contact)] = number_contact
        else:
            print(f"Продолжить?")
            answer_2.lower = input("Да/Нет - ")
            if answer_1.lower() == 'да':
                continue
            else:
                break
    else:
        number_contact = int(input('Введите номер контакта:'))
        phone_book[(faname_contact, name_contact)] = number_contact
    print(phone_book)
    print(f"Продолжить?")
    answer_3 = input("Да/Нет - ")
    if answer_3.lower() == 'да':
        continue
    else:
        break
