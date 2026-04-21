class Album:

    def __init__(self, album_name, number_of_songs, album_artist):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist

    def __str__(self):
        # written over multiple lines for character limit
        name = self.album_name
        artist = self.album_artist
        songs = self.number_of_songs
        return f"({name}, {artist}, {songs})"


albums1 = []
album1 = Album("Thriller", 9, "Michael Jackson")
album2 = Album("25", 11, "Adele")
album3 = Album("Back in Black", 10, "AC/DC")
album4 = Album("Rumours", 11, "Fleetwood Mac")
album5 = Album("Divide", 16, "Ed Sheeran")


albums1.append(album1)
albums1.append(album2)
albums1.append(album3)
albums1.append(album4)
albums1.append(album5)

for album in albums1:
    print(album)

# sort by number of songs
print("Printing sorted")
albums1 = sorted(albums1, key=lambda albums: albums.number_of_songs)
for album in albums1:
    print(album)

albums1[0], albums1[1] = albums1[1], albums1[0]

print("Printing swapped")
for album in albums1:
    print(album)

albums2 = []
album6 = Album("1989", 13, "Taylor Swift")
album7 = Album("Hybrid Theory", 12, "Linkin Park")
album8 = Album("The Eminem Show", 20, "Eminem")
album9 = Album("Nevermind", 12, "Nirvana")
album10 = Album("Abbey Road", 17, "The Beatles")

albums2.append(album6)
albums2.append(album7)
albums2.append(album8)
albums2.append(album9)
albums2.append(album10)

print("Printing albums 2")
for album in albums2:
    print(album)

# Learned from stack overflow
albums2.extend(albums1)

print("Printing albums 2 with 1 added")
for album in albums2:
    print(album)

albums2.append(Album("Dark Side of the Moon", 9, "Pink Floyd"))
albums2.append(Album("Oops!... I Did It Again", 16, "Britney Spears"))

albums2 = sorted(albums2, key=lambda album: album.album_name)

print("Printing album2 sorted by album name")
for album in albums2:
    print(album)

for index, album in enumerate(albums2):
    if album.album_name == "Dark Side of the Moon":
        print(index)
