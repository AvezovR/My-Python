count_dogs = [111, 56, 1, 7]
print(count_dogs)
num_max = max(count_dogs)
num_min = min(count_dogs)

for i, x in enumerate(count_dogs):
    if x == num_min:
        num_min_index = i
    if x == num_max:
        num_max_index = i
count_dogs[num_min_index] = num_max
count_dogs[num_max_index] = num_min
print(count_dogs)


