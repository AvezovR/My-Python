data_student = input('Введите информацию о студенте через пробел '
                     '(имя, фамилия, город, место учёбы, оценки):'
)
data = data_student.split(' ')
print(data)
result_dict = {}
result_dict['Имя'] = data[0]
result_dict['Фамилия'] = data[1]
result_dict['Город'] = data[2]
result_dict['Место учёбы'] = data[3]
result_dict['Оценки'] = []
for i_grade in data[4:]:
    result_dict['Оценки'].append(i_grade)
for i_info in result_dict:
    print(i_info, '-', result_dict[i_info])

