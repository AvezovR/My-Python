integer = int(input('Введите целое число: '))
result = {}
for letter in range(1, integer + 1):
    result[letter] = letter**2
print(result)
