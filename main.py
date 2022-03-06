import csv
import random
import time
from graphics import *
from constants import directions, rooms, items

# declaring dynamic objects
score = 0
counter_action = 0
counter_item = 0
inventory = []
current_room = rooms["entrance hall"]
data_rows = []

# game intro & instructions
def game_intro():
    print("\nWelcome to the House of Antiques!\n")
    print("You will now enter the house and face some challenges in order to exit")
    print("First, you will have to move around the different rooms.. You will notice objects inside the rooms")
    print("You have to collect a total of 5 objects to your inventory")
    print("Once you've collected them, there will be a second challenge that involves using the object")
    print("\nInstructions of Navegation:\n")
    print("You may use the following MOVING commands:\n - go north\n - go south\n - go east\n - go west\n")
    print("To examine objects you see, use the LOOK command:\n - look <object name>")
    print(" - example: if you notice a car & want to observe it, you can type: look car\n")
    print("To collect objects, use the GET command:\n - get <object name>")
    print(" - example: if you notice a car & want to collect it, you can type: get car\n")
    print("To view your inventory, use the VIEW INVENTORY command:\n - view inventory")
    print("-----------------------------\n\n")

# function to display images of items in a room
def display_image(img):
    win = GraphWin("{}".format(img),500,500)
    image = Image(Point(250,250), "images/{}.gif".format(img))
    image.draw(win)
    time.sleep(2)
    win.close()

# function to write appended actions in .csv file
def write_csv(data):
    with open('actions.csv','w',encoding='UTF8',newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# first main game loop - move around rooms, view items, get items, view inventory
def game_loop(inventory,current_room,counter_item,counter_action):
    while True:
        print("You're in the {}...\n{}".format(current_room["name"],current_room["text"]))
        if current_room["name"] != 'entrance hall' and len(current_room["item"]) != 0:
            for key,value in items.items():
                if key in current_room["item"]:
                    print(value["item_in_room"])
        if counter_item == 5:
            print("-----------------------------\n")
            print("\nYou've completed the first part of the game!")
            print("Now in order to exit the house you will have to face a challenge with the objects you've collected...")
            print("Each object will be shown & you will be able to use them..")
            print("You will have 2 options to use each object & depending on what you choose, you will have a successful or non-successful exit")
            break
        else:
            command = input("\n>> ").lower()
            print("-----------------------------\n")
            if command in directions:
                counter_action += 1
                data_rows.append(["Action {}: {}".format(counter_action,command)])
                if command in current_room:
                    current_room = rooms[current_room[command]]
                    # support for only moving in entrance hall
                    if current_room["name"] != 'entrance hall' and len(current_room["item"]) != 0:
                        for i in current_room["item"]:
                            display_image(i)
                else:
                    print('You cannot go this way!\n')
            elif "look" in command:
                try:
                    if len(current_room["item"]) == 0:
                        print("No more items available in this room! you can only MOVE not LOOK\n")
                    else:
                        if command == "look {}".format(current_room["item"][0]):
                            item = current_room["item"][0]
                            data_rows.append(["Action {}: {}".format(counter_action,command)])
                            for key,value in items.items():
                                if key == item:
                                    print(value["description"])
                        elif command == "look {}".format(current_room["item"][-1]):
                            data_rows.append(["Action {}: {}".format(counter_action,command)])
                            item = current_room["item"][-1]
                            for key,value in items.items():
                                if key == item:
                                    print(value["description"])
                        else:
                            print("Invalid Input!\n")
                except:
                    print("\nInvalid input! Make sure you're typing one of the commands 1\n")
            elif "get" in command:
                try:
                    if len(current_room["item"]) == 0:
                        print("No more items available in this room! you can only MOVE not GET\n")
                    else:
                        if command == "get {}".format(current_room["item"][0]):
                            counter_action += 1
                            data_rows.append(["Action {}: {}".format(counter_action,command)])
                            item = current_room["item"][0]
                            counter_item += 1
                            inventory.append(item)
                            current_room["item"].remove(item)
                            print("Ok. You got a {}\n".format(item))
                        elif command == "get {}".format(current_room["item"][-1]):
                            counter_action += 1
                            data_rows.append(["Action {}: {}".format(counter_action,command)])
                            item = current_room["item"][-1]
                            counter_item += 1
                            inventory.append(item)
                            current_room["item"].remove(item)
                            print("Ok. You got a {}\n".format(item))
                        else:
                            print("Invalid Input!\n")
                except:
                    print("\nInvalid input! Make sure you're typing one of the commands 2\n")
            elif command == "view inventory":
                counter_action += 1
                data_rows.append(["Action {}: {}".format(counter_action,command)])
                print("You're inventory is: {}\n".format(inventory))
            else:
                print("\nInvalid input! Make sure you're typing one of the commands\n")
    return inventory, counter_action

def perform_actions_and_score(inventory,score,counter_action):
    counter_score = 0
    score_denominator = len(inventory)
    while True:
        if counter_score == 5:
            print("\n\nThe game has ended!\nYour score is {} out 5 (success rate: {}%)".format(score,100 * round(score/score_denominator,4)))
            break
        else:
            item = random.choice(inventory)
            choice = input("\nWhat do you with the {}? (type 'a' or 'b')\
                \n - a. {}\n - b. {}\n\n>> ".format(item,items[item]['a']['option'],items[item]['b']['option'])).lower()
            if choice == 'a':
                inventory.remove(item)
                counter_score += 1
                counter_action += 1
                data_rows.append(["Action {}: {}".format(counter_action,items[item]['a']['option'])])
                score += items[item]['a']['score']
            elif choice == 'b':
                inventory.remove(item)
                counter_score += 1
                counter_action += 1
                data_rows.append(["Action {}: {}".format(counter_action,items[item]['b']['option'])])
                score += items[item]['b']['score']
            else:
                print('Invalid Input! Make sure you type a or b!')

def main(inventory,data_rows,current_room,counter_item,counter_action,score):
    game_intro()
    inventory, counter_action = game_loop(inventory,current_room,counter_item,counter_action)
    perform_actions_and_score(inventory,score,counter_action)
    write_csv(data_rows)

main(inventory,data_rows,current_room,counter_item,counter_action,score)