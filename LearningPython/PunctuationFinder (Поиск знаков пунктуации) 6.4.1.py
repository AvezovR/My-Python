signs = {".",",",";",":","!","?"}
text = input('Введите строку: ')
sign_text = []
for sign in text:
    if sign in signs and not sign in sign_text:
        sign_text.append(sign)
        print(sign_text)
i_sing = set(sign_text)
print(f'Различные знаки пунктуации:{''.join(i_sing)}')
print(f'Количество различных знаков пунктуации:{len(i_sing)}')

# или

user_input = set(input("Введите строку: "))
symbols = set(".,;:!?")
print("Различные знаки пунктуации:", user_input.intersection(symbols))
print("Количество знаков пунктуации:", len(user_input.intersection(symbols)))
