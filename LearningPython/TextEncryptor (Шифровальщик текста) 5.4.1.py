alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

message = input("Введите сообщение: ").lower()
shift = int(input("Введите сдвиг: "))

new_message = [alphabet[(alphabet.index(letter) + shift) % len(alphabet)]
               if letter in alphabet
               else letter
               for letter in message
               ]

print("Зашифрованное сообщение:", ''.join(new_message))
