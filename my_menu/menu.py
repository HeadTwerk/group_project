# Manage food items through the functions

from my_menu.items import *
import csv
import os
import time
import librosa  # install ffmpeg
from gtts import gTTS
from playsound import playsound


# list of all item types
drinks = []
rice = []
chappatis = []
paneer = []
chicken = []

# menu for all items
menu1 = [
    drinks,
    rice,
    chappatis,
    paneer,
    chicken,
]
# We already have menu.csv as a file. For every operation, to extract data from a csv is not as easy and worth the time
# While on the other hand a database system is an overkill for small projects as ours
# Therefore we will simply load the data from csv to a runtime list or dictionary

# read menu from file and load it on runtime List menu[]
def _load_data(file):
    with open(file, 'r') as read_obj:
        csv_reader = csv.reader(read_obj)
        # read the column name of menu into header
        header = next(csv_reader)
        # if file isn't empty
        if header != None:
            # Iterating over each row after the header in the csv
            for row in csv_reader:
                # pass values of List[str] row to addItems()
                addItem(ord(row[0]) - 48, row[1], row[2], row[3])

# print different types of Items
def show_item_list():
    print("1. Drinks\n2. Rice\n3. Chappati\n4. Paneer\n5. Chicken\n")


# display menu
def show_menu():
    for i in range(len(menu1)):
        if i + 1 == 1:
            print("\tDrinks")
        elif i + 1 == 2:
            print("\tRice")
        elif i + 1 == 3:
            print("\tChappati")
        elif i + 1 == 4:
            print("\tPaneer")
        else:
            print("\tChicken")
        for j in menu1[i]:
            print(f"{j.name} {j.cost}")

# speak out the menu
def say_menu(file = "my_menu\\menu.csv"):
    with open(file) as src:
        _reader = csv.reader(src)
        _header = next(_reader)

        if not os.path.isfile("audio_files\\menu_item.mp3"):
            print("fetching menu_item.mp3")
            # create the required menu audio
            my_str = "On today's menu we have ,"
            for row in _reader:
                my_str = my_str+" {}".format(row[1])
            audio = gTTS(my_str)
            audio.save("audio_files\\menu_item.mp3")
        else:
            print("menu_item.mp3 exists")

        # play it
        print("speaking menu:")
        playsound("audio_files\\menu_item.mp3")
        time.sleep(librosa.get_duration(filename="audio_files\\menu_item.mp3")-1)

# add a new item to the menu
def addItem(i, name, cost, attri):
    if i == 1:
        drinks.append(Drink(name, cost, attri))
    elif i == 2:
        rice.append(Rice(name, cost, attri))
    elif i == 3:
        chappatis.append(Chappati(name, cost, attri))
    elif i == 4:
        paneer.append(Paneer(name, cost, attri))
    elif i == 5:
        chicken.append(Chicken(name, cost, attri))
    else:
        raise Exception("---INVALID ITEM TYPE---")
    print(f"added {name}")


# remove an exiting item from the loaded menu[]
def remItems(i, name):
    for j in range(len(menu1[i - 1]) - 1):
        if list(menu1[i - 1])[j].name == name:
            menu1[i - 1].pop(j)
            print("removed {name}")
