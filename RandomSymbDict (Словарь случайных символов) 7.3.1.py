def random_letter():
    import random
    lowercase = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    letters_list = [random.choice(lowercase) for _ in range(10)]
    return letters_list

def random_dict(letters_list):
    list_letter = dict()
    for count, letter in enumerate(letters_list):
        list_letter[count] = letter
    return list_letter   

letters_list1 = random_letter()
letters_list2 = random_letter()
print('Первый список:', letters_list1)
print('Второй список:', letters_list2)
letters_dict1 = random_dict(letters_list1)
letters_dict2 = random_dict(letters_list2)
print('Первый словарь:', letters_dict1)
print('Второй словарь:', letters_dict2)