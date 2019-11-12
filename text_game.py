# TerribleTurtles
# 11-11-19
# text_based adventure game

import time
import random


# Variables

PROMPT = "       <North>\n<West>         <East>\n       <South>\n>>>"
PROMPT_ARROW = ">>>"
inventory = []


def display_intro():

    """
    Starting introduction text for the game

    Input: None
    Output: None

    :return:
    """
    current_room = "entry"                         # sets the current room

    print("\n\nYou are about to embark on an EPIC quest!")
    # time.sleep(2)
    print("\nTo find the Dragon's Treasure!")
    # time.sleep(4)
    print("\n\nYou awaken in a dark cell, armed with only a compass\n")
    time.sleep(3)
    print("To the North you see a large wooden cell door")
    time.sleep(1.5)
    print("To the East is a bare cell wall")
    time.sleep(1.5)
    print("To the South is a bare cell wall")
    time.sleep(1.5)
    print("To the West is a cell wall with many large cracks")

    return current_room


def choose_path(current_room):
    """
    Input: User Inputs String, must == directions to continue
    Output: returns a compass direction as a string AKA path
    :return:
    """
    path = ""
    directions = ["north", "east", "west", "south"]     # sets the allowed inputs
    while path not in directions:                       # keeps asking for input until proper input is entered
        if path != "":
            time.sleep(2)
            path = input(f"\n\nPlease pick an ACTUAL direction!\n{PROMPT}").lower()
        else:
            time.sleep(2)
            path = input(f"\n\nWhich way will you go?\n{PROMPT}").lower()
    check_path(path, current_room)


def check_path(chosen_path, current_room):
    """
    Check what path the user wants, then sends them that way
    Input: The path that the user chose
    Output: UNKNOWN
    :param current_room:  STRING of the current room
    :param chosen_path:   String of the path the user chose
    :return:
    """
    if current_room == "entry":
        if chosen_path == "north":
            entry_north(current_room)
        elif chosen_path == "east":
            print("There's nothing here\n")
            time.sleep(1)
            print("You walk back to the center\n")
            choose_path(current_room)
        elif chosen_path == "south":
            print("There's nothing here\n")
            time.sleep(1)
            print("You walk back to the center\n")
            choose_path(current_room)

        elif chosen_path == "west":
            choice = ""
            actions = ["go back", "inspect"]
            print("You come to wall, you see something shiny in a large crack.")
            while choice not in actions:
                choice = input(f"What do you do?\n\n<inspect>  <go back>\n{PROMPT_ARROW}").lower()
            if choice == "go back":
                print("You walk back to the center\n")
                choose_path(current_room)
            elif "entry_key" in inventory:
                print("You find nothing")
                choose_path(current_room)
            else:
                print("You find an old key in the large crack")
                time.sleep(1)
                print("You take the key with you and head back to the center")
                inventory.append("entry_key")
                choose_path(current_room)




def entry_north(current_room):
    print("You approach the door and try to open it...")
    time.sleep(1)
    if "entry_key" in inventory:
        print("You take out the key and put it into the lock..")
        time.sleep(1)
        print("The door pops open!")
    else:
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("The door is locked.")
        time.sleep(2)
        print("\nYou head back to the center")
        choose_path(current_room)

display_intro()


choose_path("entry")



