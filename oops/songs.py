class Songs:
    """Class to represent a song

    Attributes:
    title(str): The name of the song
    artist(str): an artist object representing the songs creator
    duration(int): the duration of the song. Maybe zero
    """

    def __init__(self, title, artist, duration=0):
        """Song init method"""
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """Class to represent an album, using its treack list

    Attributes:
        album_name(str): The name of the album
        year(int):The year was album was released.
        artist: (Artist): The singer of the album
            if not specified, the artist will default to an artist with the name
        tracks (List[Song]): A list of the songs on the album.

    Methods:
        add_song: Used to add a new song to the track list.
    """

    def __init__(self, album, year, artist=None):
        self.album = album
        self.year = year
        if artist is None:
            self.artist = Artists("Various Artists")
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song_name, position=None):
        """adds song to the docstring

        Args:
            song_name (_type_): _description_
            position (_type_, optional): _description_. Defaults to None.
        """
        if position is None:
            self.tracks.append(song_name)
        else:
            self.tracks.insert(position, song_name)


class Artists:
    """This is a basic class to store artists details

    Attributes:
        name(str): The name of the artist
        albums(list[Album]): a list of albums form the artist.
    """

    def __init__(self, name) -> None:
        self.name = name
        self.album = []

    def add_album(self, album):
        """adds new albums to the album list

        Args:
            album (_type_): _description_
        """
        self.album.append(album)


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(
                line.strip("\n").split("\t")
            )
            year_field = int(year_field)
            print(artist_field, album_field, year_field, song_field)


if __name__ == "__main__":
    load_data()
