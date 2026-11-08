def get_without_sets1(list1, list2, list3):
    repeats = 0
    for item in list1:
        if item in list2 and item in list3:
            repeats += 1
    return repeats
def get_without_sets2(list1, list2, list3):
    repeats = 0
    for item in list1:
        if item not in list2 and item not in list3:
            repeats += 1
    return repeats
def get_with_sets1(list1, list2, list3):
    repeats = 0
    result = set(list1) & set(list2) & set(list3)
    repeats += len(result)
    return repeats
def get_with_sets2(list1, list2, list3):
    repeats = 0
    result = set(list1) - set(list2) - set(list3)
    repeats += len(result)
    return repeats

array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

print("Задача 1:")
print(f"\n • Решение без множеств: {get_without_sets1(array_1, array_2, array_3)}")
print(f" • Решение c множествами: {get_with_sets1(array_1, array_2, array_3)}")
print(f"\nЗадача 2:")
print(f"\n • Решение без множеств: {get_without_sets2(array_1, array_2, array_3)}")
print(f" • Решение c множествами: {get_with_sets2(array_1, array_2, array_3)}")