number_of_employees = int(input('Кол-во соотрудников в офисе: '))
employees = []
for _ in range(number_of_employees):
    employee_number = int(input('ID сотрудника: '))
    employees.append(employee_number)
for number in employees:
    employee_search = int(input('Какой ID ищем? '))
    if number == employee_search:
        print('Сотрудник на месте')
    else:
        print('Сотрудник не работает')
        break
