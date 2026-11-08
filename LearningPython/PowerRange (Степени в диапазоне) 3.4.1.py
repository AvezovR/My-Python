left_boundary = int(input("Левая граница: "))
right_boundary = int(input("Правая граница: "))

list_cubes = [x ** 3 for x in range(left_boundary, right_boundary+1)]
list_squares = [x ** 2 for x in range(left_boundary, right_boundary+1)]

print(f'Список кубов чисел в диапазоне от {left_boundary} до {right_boundary}: {list_cubes}')
print(f'Список квадратов чисел в диапазоне от {left_boundary} до {right_boundary}: {list_squares}')
