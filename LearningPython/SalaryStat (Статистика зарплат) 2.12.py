salary_employees = []
number_employees = int(input('Кол-во сотрудников: '))
for i in range(number_employees):
    print('Зарплата', i + 1, 'сотрудника', end=' ')
    salary = int(input(''))
    if salary > 0:
        salary_employees.append(salary)
print('Осталось сотрудников:', len(salary_employees))
print('Зарплаты: ', salary_employees)
print('Максимальная зп: ', max(salary_employees))
print('Минимальная зп: ', min(salary_employees))
