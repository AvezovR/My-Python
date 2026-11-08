def frequency_dictionary(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict

def hustogram(string):
    print("Оригинальный словарь частот:")
    for i_sym in sorted(string.keys()):
        print(i_sym, ':', string[i_sym])

def inverted_histogram(string1):
    inverted_sym_dict = dict()
    for i_sym in sorted(string1.values()):
        i_sym_dict = []
        for sym in string1.keys():
            if i_sym == string1[sym]:
                i_sym_dict.append(sym)
        inverted_sym_dict[i_sym] = i_sym_dict
    return inverted_sym_dict

def inverted_otput(string2):
    print("\nИнвертированный словарь частот:")
    for i_sym in sorted(string2.keys()):
        print(i_sym, ':', string2[i_sym])

text = input('Введите текст: ')
hist = frequency_dictionary(text)
hustogram(hist)
inverted_hist = inverted_histogram(hist)
inverted_otput(inverted_hist)

# здесь что-то написано