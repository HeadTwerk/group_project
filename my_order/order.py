# Manage processing of orders

import csv
import os
import time
import speech_recognition as sr
import librosa # install ffmpeg
from gtts import gTTS
from playsound import playsound

# Audio files to interact with customer
def init_voice_lines():
    print("initialising voice lines ...")

    # If you are not able to generate files as wished eg: if they are clipping at the start or etc
    # try "audio_files\\oof.py"
    # create files if not already present
    if not os.path.isfile("audio_files\\greet.mp3"):
        greet = gTTS("Welcome to our restaurant. We are pleased to have you here today. What would you like to order ?", lang="hi", tld="co.in")
        greet.save("audio_files\\greet.mp3")
    if not os.path.isfile("audio_files\\anything_else.mp3"):
        ordered = gTTS("anything else ?", lang="hi", tld="co.in")
        ordered.save("audio_files\\anything_else.mp3")
    if not os.path.isfile("audio_files\\ask_add.mp3"):
        ask_add = gTTS("And what may be your delivery address ?", lang="hi", tld="co.in")
        ask_add.save("audio_files\\ask_add.mp3")
    if not os.path.isfile("audio_files\\ordered.mp3"):
        ordered = gTTS("Noted", lang="hi", tld="co.in")
        ordered.save("audio_files\\ordered.mp3")

# taking orders
def take_order(name, file="my_order\\orders.csv"):
    # add orders to data(here orders.csv)
    with open(file, 'a', newline='') as file_w:
        _writer = csv.writer(file_w)
        _writer.writerow([name])

# to recognise customer voice input, process it and
# return the generated text :str
def voice_input():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        # adjusting and calibrating for background noise
        print("calibrating for noise")
        r.adjust_for_ambient_noise(source, duration=2)
        r.dynamic_energy_threshold = True
        #print("--calibrated")

        # greeting
        playsound("audio_files\\greet.mp3")
        time.sleep(librosa.get_duration(filename="audio_files\\greet.mp3")-2)

        # Listening to customer speak
        input_as_text = ""
        while True:
            print("listening . . . ")
            try:
                audio = r.listen(source)
                # and recognizing
                print("recognizing...")
                input_as_text = input_as_text + r.recognize_google(audio, language="en-IN") + " "
                print(input_as_text)

                # confirm order
                playsound("audio_files\\anything_else.mp3")
                time.sleep(.5)
                audio = r.listen(source)
                print("anything else ?")
                confirm = r.recognize_google(audio)
                print(f"\t{confirm}")
                # if yes, then repeat
                if confirm == "yes":
                    continue
                # else
                break
            except:
                # if nothing ineligible was detected try again
                continue
        return input_as_text

def make_sense():
    text_generated = voice_input()

