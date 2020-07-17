from os import sys, listdir
from room import Room
from player import Character, Player_Character
from items import basic_items, weapons
import pickle

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together
room['outside'].n_to(room['foyer'].name, room['foyer'])
room['foyer'].s_to(room['outside'].name, room['outside'])
room['foyer'].n_to(room['overlook'].name, room['overlook'])
room['foyer'].e_to(room['narrow'].name, room['narrow'])
room['overlook'].s_to(room['foyer'].name, room['foyer'])
room['narrow'].w_to(room['foyer'].name, room['foyer'])
room['narrow'].n_to(room['treasure'].name, room['treasure'])
room['treasure'].s_to(room['narrow'].name, room['narrow'])



def Dict_parser(param, dictionary):
    """Compares a given param and checks to see if its within a dictionary
    if so, will return that item"""
    if param in dictionary:
        return dictionary(param)
    else:
        print("Failed to find")
        pass

def Main_menu_prompt():
    print("[Move (m)] [Search (s)] [Inventory (i)] [Quit (q)]")
    choice = input("State your action: ")
    return choice

def Key_Based_Print(dictionary):
    """Will take a dictionary and print out all the key values"""
    for key in dictionary:
        print(f" -| {key}")

def Player_Create():
    name = input("What shall we call you?\n:: ")
    desc = input("In one word, describe yourself:\n:: ")
    c_choice=input("State your trade \n[Warrior (w)], [Mage (m)], [Rogue (r)], [Archer (a)]\n:: ")
    chosen = ""
    if c_choice == "w":
        chosen = "Warrior"
    elif c_choice == "m":
        chosen = "Mage"
    elif c_choice == "r":
        chosen = "Rogue"
    else:
        chosen = "Archer"
    location = room['outside']
    p_character = Player_Character(name, desc, chosen, location)
    if p_character.c_class == "Warrior":
        p_character.player_inventory_add(weapons['sword'])
    elif p_character.c_class == "Mage":
        p_character.player_inventory_add(weapons['wand'])
    elif p_character.c_class == "Rogue":
        p_character.player_inventory_add(weapons['dagger'])
    elif p_character.c_class == "Archer":
        p_character.player_inventory_add(weapons['bow'])
    else:
        pass
    return p_character

def Game_Start():
    g_choice = input(" Do you wish to start a New Game(n) or Continue(c) and old one?\n:: ")
    if g_choice == "n":
        new_char = Player_Create()
        return new_char
    elif g_choice == "c":
        saved_games = listdir("saves/")
        Key_Based_Print(saved_games)
        game_selection = input('Which Game you like to load?\n:: ')
        try:
            with open(f"saves/{game_selection}.pkl", "rb") as opened_file:
                player_data = pickle.load(opened_file)
                return player_data
        except:
            print("Sorry File name did not match")
            pass
    else:
        print("Sorry invalid option.")
        sys.exit()

active_player = Game_Start()

def Quit():
    """Allows user to exit the game, will prompt to check if they are sure"""
    exit_confirm = input('Are you sure? (y/n)\n:: ')
    if exit_confirm == "y":
        to_save = input("Would You Like to Save? (y/n)\n:: ")
        if to_save == "y":
            with open(f"saves/{active_player.name}.pkl","wb") as save_file:
                pickle.dump(active_player, save_file)
            print("Hero! We await your return!")
            sys.exit()
        else:
            print("Hero! We await your return!")
            sys.exit()
    else:
        print("Good Choice, The Saga Continues!")
        pass

def Move():
    print(f"\n --| {active_player.location.name} |--")
    print(f"{active_player.location.description}\n")
    m_choice = input("[Direction (d)] [Stay (s)]\n::")
    def Cardinal_Move(destination):
        try:
            print(f"You have moved to the {active_player.location.north}")
            active_player.location = active_player.location.north
        except:
            print("Sorry but no entrancce was found")
    if m_choice == "d":
        print("[North (n)] [South (s)] [East (e)] [West (w)]")
        c_choice = input("Which direction?\n :: ")
        if c_choice == "n":
            Cardinal_Move(active_player.location.north)
        elif c_choice == "s":
            Cardinal_Move(active_player.location.south)
        elif c_choice == "e":
            Cardinal_Move(active_player.location.east)
        elif c_choice == "w":
            Cardinal_Move(active_player.location.west)
    else:
        print("Sorry, but that was not an options")
        pass

while True:
    choice = Main_menu_prompt()
    if choice == "m":
        Move()
    elif choice == "i":
        print(active_player.inventory)
    elif choice == "q":
        Quit()
    elif choice == "t":
        print (weapons['sword'])
    else:
        print("Sorry, choice wasn't valid.")
    



# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.



# I opted to use my own system to join the rooms

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

#
# Main
#