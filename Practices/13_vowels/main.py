enter_text = input("Введите текст: ") # Нужно отнести кольцо в Мордор!
vowels = 'уеыаоэяию'

list_of_vowel = [letter for letter in enter_text if letter in vowels]

print("Список гласных букв:", list_of_vowel)
print("Длина списка:", len(list_of_vowel))
