text = input('Введите строку: ')

# for letter in text:
#     if letter.islower():
#         text1.append(letter)
# print(' '.join(text1))
# print(' '.join(text2))

# или
# text1 = [letter for letter in text if letter.islower()]
# text2 = [letter for letter in text if letter.isupper()]
# print(' '.join(text1))
# print(' '.join(text2))

lowers = len([letter for letter in text if letter.islower()])
uppers = len([letter for letter in text if letter.isupper()])
# print(lowers, uppers)

if lowers > uppers:
    print("Результат:", text.lower())
else:
    print("Результат:", text.upper())
