students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

def student_info(student):
    age_students = []
    interest_students = []
    length_surname = []
    for i_info in student:
        age_students += [(i_info, student[i_info]['age'])]
        interest_students += (student[i_info]['interests'])
        length_surname += (student[i_info]['surname'])
    return age_students, set(interest_students), len(length_surname),

student_data = student_info(students)

print(f'Список пар «ID студента — возраст»: {student_data[0]}')
print(f'Полный список интересов всех студентов: {student_data[1]}')
print(f'Общая длина всех фамилий студентов: {student_data[2]}')
