text = input('Введите текст: ')
for count, letter in enumerate(text):
    if letter == '~':
        print(count, letter)
