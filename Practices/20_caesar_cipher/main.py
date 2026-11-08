alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

def caesar_cipher(message, shift):
    new_message = ''
    for letter in message:
        if letter in alphabet:
            new_message += alphabet[(alphabet.index(letter) + shift) % len(alphabet)]
        else:
            new_message += letter
    return new_message

message = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))

print("Зашифрованное сообщение:", caesar_cipher(message, shift))
