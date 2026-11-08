violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

# TODO здесь писать код
total_songs = int(input('Сколько песен выбрать? '))
time_songs = float(0)
for i in range(total_songs):
    print(f'Название {i+1}-й песни:', end = ' ')
    name_song = input()
    for song in violator_songs:
        if name_song in song:
            time_songs += round(float(song[1]), 2)
print(f'Общее время звучания песен — {str(round(time_songs, 2)).replace('.', ',')} минуты')
