# TODO здесь писать код
list = [1,4,-3,0,10]
print('Изначальный список: ', list)
for run in range(len(list) - 1):
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            list[i], list[i + 1] = list[i+1], list[i]
print('Отсортированный список: ', list)