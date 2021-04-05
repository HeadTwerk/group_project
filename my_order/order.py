# Manage processing of orders

import csv
import os
import time
import speech_recognition as sr
import librosa # install ffmpeg
from gtts import gTTS

# Audio files to interact with customer
def init_voiceLines():
    greet = gTTS("Welcome to our restaurant. We are pleased to have you here today. What would you like to order ?", lang="en")
    greet.save("my_order\\greet.wav")
    ordered = gTTS("Noted")
    ordered.save("my_order\\ordered.wav")

# taking orders
def take_order(name, file="my_order\\orders.csv"):
    # add orders to data(here orders.csv)
    with open(file, 'a', newline='') as file_w:
        _writer = csv.writer(file_w)
        _writer.writerow([name])

def voice_input():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=int(librosa.get_duration(filename="my_order\\greet.wav")))
        r.dynamic_energy_threshold = True
        os.system("my_order\\greet.wav")
        time.sleep(librosa.get_duration(filename="my_order\\greet.wav"))

        while True:
            print("listening . . . ")
            try:
                audio = r.listen(source)
                input_as_text = r.recognize_google(audio)
                break
            except:
                continue
        print(input_as_text)

