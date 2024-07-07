import wave, time,json
from lyrics import get_lyrics
from fingerprinting import acoust_fingerprint_generator
from API import request_handler
from listener import audio_listener


data = json.load("song_data.json")
listen_in_real_time = False
last_fingerprint =""
current_lyrics = ""

def get_duration_wave(file_path):
   with wave.open(file_path, 'r') as audio_file:
      frame_rate = audio_file.getframerate()
      n_frames = audio_file.getnframes()
      duration = n_frames / float(frame_rate)
      return duration


if __name__ == "__main__":

    if listen_in_real_time:
        audio_file = 'output.wav'
        try:
            while True:
                audio_listener.listen()
                time.sleep(6)
                duration = get_duration_wave(audio_file)
                print(f"Duration: {duration:.2f} seconds")
                fingerprint = acoust_fingerprint_generator.generate_audio_fingerprint(audio_file)
                print("Generated fingerprint...")
                if last_fingerprint != fingerprint:
                    last_fingerprint = fingerprint
                    save_fingerprint = open("fingerprint.txt","w")
                    save_fingerprint.write(str(fingerprint))
                    request_handler.lookup_acoustid(fingerprint=fingerprint,duration=duration)
                    try:
                        song = request_handler.song_name
                        author = request_handler.artist_name
                        current_lyrics = get_lyrics.get_data(song,author_name=author)
                    except AttributeError:
                        print("No results found")
                else:
                    song = request_handler.song_name 
                    author = request_handler.artist_name
                    current_lyrics = get_lyrics.get_data(song,author_name=author)
                
        except KeyboardInterrupt:
            print("Closing the program")
    else:
        audio_file = 'old_output.wav'
        duration = get_duration_wave(audio_file)
        print(f"Duration: {duration:.2f} seconds")
        fingerprint = acoust_fingerprint_generator.generate_audio_fingerprint(audio_file)
        print("Generated fingerprint...")
        if last_fingerprint != fingerprint:
            last_fingerprint = fingerprint
            request_handler.lookup_acoustid(fingerprint=fingerprint,duration=duration)
            song = request_handler.song_name 
            author = request_handler.artist_name
            current_lyrics = get_lyrics.get_data(song,author_name=author)