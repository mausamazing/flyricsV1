from lyrics import get_lyrics
from fingerprinting import acoust_fingerprint_generator
from API import request_handler
from listener import audio_listener
import wave, time,json

listen_in_real_time = False
last_fingerprint =""
current_lyrics = ""

import json

# Read the content of the file
def read():
    global data
    with open("song_data.json", "r") as file:
        content = file.read()
        data = json.loads(content)
read()
old_song_name = data["name"]
old_author_name = data["artist"]

def get_duration_wave(file_path):
   with wave.open(file_path, 'r') as audio_file:
      frame_rate = audio_file.getframerate()
      n_frames = audio_file.getnframes()
      duration = n_frames / float(frame_rate)
      return duration
def old_code():#    might need later

    # if __name__ == "__main__":

    #     if listen_in_real_time:
    #         audio_file = 'output.wav'
    #         try:
    #             while True:
    #                 audio_listener.listen()
    #                 time.sleep(6)
    #                 duration = get_duration_wave(audio_file)
    #                 print(f"Duration: {duration:.2f} seconds")
    #                 fingerprint = acoust_fingerprint_generator.generate_audio_fingerprint(audio_file)
    #                 print("Generated fingerprint...")
    #                 if last_fingerprint != fingerprint:
    #                     last_fingerprint = fingerprint
    #                     save_fingerprint = open("fingerprint.txt","w")
    #                     save_fingerprint.write(str(fingerprint))
    #                     request_handler.lookup_acoustid(fingerprint=fingerprint,duration=duration)
    #                     try:
    #                         song = request_handler.song_name
    #                         author = request_handler.artist_name
    #                         current_lyrics = get_lyrics.get_data(song,author_name=author)
    #                     except AttributeError:
    #                         print("No results found")
    #                 else:
    #                     song = request_handler.song_name 
    #                     author = request_handler.artist_name
    #                     current_lyrics = get_lyrics.get_data(song,author_name=author)
                    
    #         except KeyboardInterrupt:
    #             print("Closing the program")
    #     else:
    #         audio_file = 'old_output.wav'
    #         duration = get_duration_wave(audio_file)
    #         print(f"Duration: {duration:.2f} seconds")
    #         fingerprint = acoust_fingerprint_generator.generate_audio_fingerprint(audio_file)
    #         print("Generated fingerprint...")
    #         if last_fingerprint != fingerprint:
    #             last_fingerprint = fingerprint
    #             request_handler.lookup_acoustid(fingerprint=fingerprint,duration=duration)
    #             song = request_handler.song_name 
    #             author = request_handler.artist_name
    #             current_lyrics = get_lyrics.get_data(song,author_name=author)
    return

def write():
    writer = open("lyrics.txt","w")
    writer.write(get_lyrics.final_lyrics)
if __name__=="__main__":
    read()
    lyrics = get_lyrics.get_data(song_name=old_song_name,author_name=old_author_name)
    write()
    while True:
        time.sleep(3)
        try:
            read()
            song_name = data["name"]
            author_name = data["artist"]
            print(song_name,author_name)
            if(old_author_name!=author_name or old_song_name!=song_name):
                old_author_name = author_name
                old_song_name = song_name
                lyrics = get_lyrics.get_data(song_name=song_name,author_name=author_name)
                write()
            else:
                # print("Lyrics not changing yet...")
                continue
        except Exception as e:
            print(e)