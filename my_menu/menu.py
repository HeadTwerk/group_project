# Manage food items through the functions

from my_menu.items import *
import csv

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
            print("{} {}".format(j.name, j.cost))


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


# remove an exiting item from the loaded menu[]
def remItems(i, name):
    for j in range(len(menu1[i - 1]) - 1):
        if menu1[i - 1][j].name == name:
            menu1[i - 1].pop(j)
