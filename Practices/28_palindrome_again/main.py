def frequency_dictionary(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict

def frequency_counting(string):
    count = 0
    for sym in string.values():
        if sym % 2 != 0:
            count += 1
    return count

def palindrome_check(string):
    if int(string) > 1:
        print("Нельзя сделать палиндромом")
    else:
        print("Можно сделать палиндромом")

text = input('Введите строку: ')
text_dict = frequency_dictionary(text)
counting_symb = frequency_counting(text_dict)
palindrome_check(counting_symb)

