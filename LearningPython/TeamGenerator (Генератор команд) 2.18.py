N = int(input('Кол-во участников: '))
K = int(input('Кол-во человек в команде: '))
command = []
num = 0

for _ in range(1, (int(N/K)) + 1):
    new_command = []
    for _ in range(1, K + 1):
        num += 1
        new_command.append(num)
    command.append(new_command)
print(command)
