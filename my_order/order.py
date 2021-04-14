# Manage processing of orders

import csv
import os
import time
import speech_recognition as sr
import librosa  # install ffmpeg
from gtts import gTTS
from playsound import playsound
from my_menu.menu import menu1, say_menu

# list of insignificant words, mostly catering to ordering terminology
insig_list = ['is', 'i', 'want', 'plate', 'glass', 'scoop', 'serving', 'like', 'and']
int_names = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
# create an all lower case list of all items
def create_menu():
    menu= []
    for i in menu1:
        menu.extend(i)
    menu = [(i.name).lower() for i in menu]
    return menu
menu = create_menu()



# Audio files to interact with customer
def init_voice_lines():
    print("initialising voice lines ...")

    # If you are not able to generate files as wished eg: if they are clipping at the start or etc
    # try "audio_files\\oof.py"
    # create files if not already present
    if not os.path.isfile("audio_files\\greet.mp3"):
        greet = gTTS("Welcome to our restaurant. We are pleased to have you here today. What would you like to order ?",
                     lang="hi", tld="co.in")
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



# to recognise customer voice input, process it and
# return the generated text :str
def voice_input():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        # adjusting and calibrating for background noise
        print("calibrating for noise")
        r.adjust_for_ambient_noise(source, duration=2)
        r.dynamic_energy_threshold = True
        # print("--calibrated")


        # greeting
        playsound("audio_files\\greet.mp3")
        print("greetings")
        time.sleep(librosa.get_duration(filename="audio_files\\greet.mp3")-2)
        say_menu()


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
                # time.sleep(.1)
                print("anything else ?")
                audio = r.listen(source)
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


# a cover function for voice_input() to generate order list
def make_sense():
    str_list = voice_input()
    # filter out the insignificant words and return a list of strings
    str_list = ' '.join(filter(lambda x: x.lower() not in insig_list, str_list.split())).split()

    # a list of all detected orders
    legible_orders = []  # each order instance is a list[count, name] for item ordered
    k = 0
    while k < len(str_list):
        # if the  current string is a number
        if str_list[k].isnumeric():
            # create a new order list[] inside legible_order
            legible_orders.append([int(str_list[k])])
            k += 1
        elif str_list[k] == 'the' or str_list[k] == 'a':
            legible_orders.append([ 1 ])
            k += 1
        elif str_list[k] in int_names:
            legible_orders.append([ int_names.index(str_list[k]) ])
            k += 1

        # if k matches an item in menu, add it to the existing order instance
        if str_list[k] in menu:
            if len(legible_orders)>0 and len(legible_orders[-1]) == 2: legible_orders.append([1])  # fail-safe if no number was detected
            legible_orders[-1].append(str_list[k])
            # prepare for next order instance
            k += 1
        # else if current and next word together make sense, add it
        elif k+1 < len(str_list) and (str_list[k] + ' ' + str_list[k + 1]).lower() in menu:
            if len(legible_orders)>0 and len(legible_orders[-1]) == 2: legible_orders.append([1])  # fail-safe if no number was detected
            legible_orders[-1].append(str_list[k] + ' ' + str_list[k + 1])
            k += 2
        # otherwise drop current order instance and proceed
        elif len(legible_orders)>0 and len(legible_orders[-1]) == 1:
                legible_orders.pop()
                k += 1
        else: k+=1

    return legible_orders

# taking orders
def take_order( file="my_order\\orders.csv"):
    # add orders to data(here orders.csv)
    order_list = make_sense()
    with open(file, 'a', newline='') as file_w:
        _writer = csv.writer(file_w)
        for i, name in order_list:
            _writer.writerow([i, name])