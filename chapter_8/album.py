def make_album(artist_name, album_title, number_of_songs=None):
    if number_of_songs:
        dictionary={'artist':artist_name, 'album':album_title, 'number of songs':number_of_songs}
    else:
        dictionary={'artist':artist_name, 'album':album_title}
    return dictionary


dict1=make_album('traistariu', 'cerbul')
print(dict1)

dict2=make_album('andra', 'trandafirul')
print(dict2)

dict3=make_album('animalx', 'pentru ea')
print(dict3)

dict4=make_album('andre', 'lasa-ma papa', 18)
print(dict4)
