from lyricsgenius import Genius

genius = Genius("token from lyrics")
global is_corrupted 
is_corrupted= False #checks if the lyrics are extra super duper corrupted
def get_data(song_name, author_name):
        global final_lyrics
    
        # Search for the song
        song_data = genius.search_song(song_name, author_name)
        
        if song_data is None:
                raise ValueError(f"No lyrics found for '{song_name}' by '{author_name}'")
        
        # Get the lyrics
        lyrics = song_data.lyrics
        
        # Find the index of the song name in the lyrics
        index = lyrics.find(song_name)
        split_name = song_name.rsplit()
        first_word = split_name[0]
        if index == -1:
                string = f"Contributors{first_word}".lower()
                print(f"--------->{string, 'ContrbutorsTHE'.lower()} {string.lower()=='ContributorsTHE'.lower()}")

                index = lyrics.lower().find(string)
                print(lyrics[index+12:len(lyrics)-7])  # Adjust the slicing as needed
                final_lyrics = lyrics[index+12:len(lyrics)-7]
                return final_lyrics
                if index == -1:
                        raise ValueError(f"Cannot find Contributors'{song_name}' in the lyrics",lyrics)
        
        print(f"{index} is the index")
        print(lyrics[index:len(lyrics)-7])  # Adjust the slicing as needed
        final_lyrics = f"{lyrics[index:len(lyrics)-7]}"
        return final_lyrics