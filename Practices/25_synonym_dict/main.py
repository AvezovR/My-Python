from num2words import num2words

def get_ordinal(number, gender='f'):
    return num2words(number, lang='ru', ordinal=True, to='ordinal', gender=gender).title()
def get_word_pair(words):
    word_pair = []
    for i_numb in range(1, words + 1):
        i_word_pair = input(f"{get_ordinal(i_numb)} пара: ")
        word_pair.append(i_word_pair.split(" — "))
    return word_pair

def get_synonyms(words):
    list_word = []
    for sublist in words:
        for word in sublist:
            list_word.append(word)
    while True:
        synonym = input('Введите слово: ').title()
        if synonym not in list_word:
            print("Такого слова в словаре нет.")
        else:
            for sublist in words:
                if synonym == words[words.index(sublist)][0]:
                    print("Синоним:", words[words.index(sublist)][1])
                elif synonym == words[words.index(sublist)][1]:
                    print("Синоним:", words[words.index(sublist)][0])
            break

number_of_word_pairs = int(input('Введите количество пар слов: '))
word_pairs = get_word_pair(number_of_word_pairs)
synonyms = get_synonyms(word_pairs)









