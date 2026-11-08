zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
zoo.insert(1, 'bear')
zoo.remove('elephant')
lion_i = zoo.index('lion')
monkey_i = zoo.index('monkey')
print(f'Зоопарк: {zoo}')
print(f'Лев сидит в клетке номер {lion_i + 1}')
print(f'Обезьяна сидит в клетке номер {monkey_i + 1}')
