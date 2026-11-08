import random

First_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
print("Первая команда:", First_team)

Second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
print("Вторая команда:", Second_team)

Round_winners = [First_team[i_glasses] if (First_team[i_glasses] > Second_team[i_glasses]) else Second_team[i_glasses] for i_glasses in range(20)]
print("Победители тура:", Round_winners)