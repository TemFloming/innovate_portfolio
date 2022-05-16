music_list = [
    {
        "artist": "Miley Cyrus",
        "song name": "Idioteque",
        "release year": "2003",
        "genre": "Alt Rock"
    },
    {
        "artist": "Throwdown",
        "song name": "Step It Up",
        "release year": "2008",
        "genre": "Hardcore"
    },
    {
        "artist": "Suicide Silence",
        "song name": "Slave To Substance",
        "release year": "2010",
        "genre": "Deathcore"
    },
    {
        "artist": "Angelmaker",
        "song name": "Leech",
        "release year": "2018",
        "genre": "Deathcore"
    },
]

fave_bands = []

for dict_i in music_list:
    fave_bands.append(list(dict_i.values())[0])

def add_to_list(band):
    fave_bands.append(band)

def del_from_list(band):
    fave_bands.remove(band)

# ------------------------