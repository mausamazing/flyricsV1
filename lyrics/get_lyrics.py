from lyricsgenius import Genius
genius = Genius("token from lyrics")
def get_data(song_name, **author_name):
        artist = author_name or ""
        song_data = genius.search_song(song_name,author_name["author_name"])
        lyrics = song_data.lyrics
        index = lyrics.index(song_name)

        print(f"{index} is the index")
        print(lyrics[index:len(lyrics)-7])
