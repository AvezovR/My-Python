file_path = input('Путь к файлу: ')
file_disk = input('На каком диске должен лежать файл: ')
file_extension = input('Требуемое расширение файла: ')
if file_path.endswith(file_extension) and file_path.startswith(file_disk):
    print('Путь корректен!')
else:
    print('Путь некорректен!')
