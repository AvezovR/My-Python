import random

detachment1 = [random.randint(50, 80) for _ in range(10)]
detachment2 = [random.randint(30, 60) for _ in range(10)]
detachment3 = [('Погиб' if (detachment1[i_damage] + detachment2[i_damage]) > 100 else "Выжил")  for i_damage in range(10)]

print('Урон первого отряда:', detachment1)
print('Урон второго отряда:', detachment2)
print('Состояние третьего отряда:', detachment3)
