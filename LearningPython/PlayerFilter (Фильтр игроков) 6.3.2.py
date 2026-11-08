players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

a_rest = []
b_training = []
c_travel = []

for i in players_dict:
    if players_dict[i]['status'] == 'Rest' and players_dict[i]['team'] == 'A':
        a_rest.append(players_dict[i]['name'])
    if players_dict[i]['status'] == 'Training' and players_dict[i]['team'] == 'B':
        b_training.append(players_dict[i]['name'])
    if players_dict[i]['status'] == 'Travel' and players_dict[i]['team'] == 'C':
        c_travel.append(players_dict[i]['name'])

print(f'Все члены команды А, которые отдыхают. {', '.join(a_rest)}.')
print(f'Все члены команды B, которые тренируются. {', '.join(b_training)}.')
print(f'Все члены команды C, которые путешествуют. {', '.join(c_travel)}.')
