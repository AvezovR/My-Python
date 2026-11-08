violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

quantity_of_songs = int(input('Сколько песен выбрать?: '))

songs_list = []
for i_song in range(1, quantity_of_songs + 1):
    name_song = input(f"Название {i_song} песни: ")
    songs_list.append(name_song)

time_song = 0
for song in songs_list:
    time_song += violator_songs[song]

print(f'\nОбщее время звучания песен: {round(time_song,2)} минуты')
