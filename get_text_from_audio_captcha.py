from pydub import AudioSegment
from os import path
import speech_recognition as sr
import os

def mp3_to_wav():

    #files
    source_mp3_audio_file = "/Users/martinanikola/PycharmProjects/PROPSHT/venv/QUORA/AUDIO_files/audio.mp3"
    new_wav_file = "/Users/martinanikola/PycharmProjects/PROPSHT/venv/QUORA/AUDIO_files/new_file.wav"


    #convert wav to mp3
    sound = AudioSegment.from_mp3(source_mp3_audio_file)
    sound.export(new_wav_file, format="wav")




def wav_to_text():

    filename = '/Users/martinanikola/PycharmProjects/PROPSHT/venv/QUORA/AUDIO_files/new_file.wav'

    # initialize the recognizer
    r = sr.Recognizer()

    # Open the file
    with sr.AudioFile(filename) as source:

        # listen for the data (load audio to memory)
        audio_data = r.record(source)

        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)

        os.remove(file_location)

        return text

