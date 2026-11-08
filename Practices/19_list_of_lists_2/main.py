nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

print("Ответ:", [item for sublist1 in nice_list for sublist2 in sublist1 for item in sublist2])

# или через itertools
import itertools
print("Ответ:",list(itertools.chain.from_iterable(list(itertools.chain.from_iterable(nice_list)))))

