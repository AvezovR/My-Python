string = input("Введите строку: ") # На вход в программу подаётся строка, в которой буква h встречается как минимум два раза
letter = 'h' # Искомая буква

print(string[(string.rindex(letter))-1:(string.index(letter)):-1])