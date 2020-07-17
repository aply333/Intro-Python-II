import textwrap
from os import sys

# Class That generate items that players can interact with.

class World_Items:
    """ This Generates items and their counts in the rooms and or inventory. """
    def __init__(self, name, description, count=1):
        self.name = name
        self.description = description
        self.count = count
    def __repr__(self):
        return '{self.name}'.format(self=self)

gold = World_Items("gold", "A pile of shimmering coins.", 25)

# Class That Generates rooms and provides methods for interaction.
class Locations:
    """Takes Name, Description, exits to create a Location"""
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connecting_rooms = {}
        self.contents = {}
    def __repr__(self):
        return '{self.name}'.format(self=self)
    def __str__(self):
        return '{self.name}'.format(self=self)
    def n_to(self, key, destination):
        """Takes a destination as an argument, this will then attach the current
        room to another one. This will conjoin the north wall/entrance"""
        self.north = destination
        self.connecting_rooms.update([(key , destination)])
    def s_to(self, key, destination):
        """Joins souther wall/entrance"""
        self.south = destination
        self.connecting_rooms.update([(key , destination)])
    def e_to(self, key, destination):
        """Joins eastern wall/entrance"""
        self.east = destination
        self.connecting_rooms.update([(key , destination)])
    def w_to(self, key, destination):
        """Joins western wall/entrance"""
        self.west = destination
        self.connecting_rooms.update([(key , destination)])
    def add_content(self, key, item):
        self.contents.update([(key, item)])
    def remove_content(self, key):
        pass

# Enacts the classes
roomA = Locations("roomA", "the Southern Room")
roomB = Locations("roomB", "the Northern Room")
roomC = Locations("roomC", "this room is East of room A")

# Adding contents to the rooms.
roomB.add_content("gold", gold)

# Joins the Rooms together
roomA.n_to(roomB.name, roomB)
roomB.s_to(roomA.name, roomA)
roomA.e_to(roomC.name, roomC)

# This is the Character class
class Character:
    """Create the Player Character"""
    def __init__(self, name, c_class):
        self.name = name
        self.c_class = c_class
        self.location = roomA
        self.inventory = {}
    def pick_up(self, key, item):
        """Will add an item to player inventory"""
        self.inventory.update([(key, item)])

# Menu Texts
root_menu = "Possible Actions:\n [Move(m)] [Inventory(i)] [Search(s)] [DevTest(d)] [Quit(q)]"

# Search Tool For dictionaries
def Dict_parser(param, g_dict):
    """Compares given input and see if it can be found within a dictionary, if successfull
    it will return the value of the key that matches up with it."""
    if param in g_dict:
        return g_dict.get(param)
    else:
        print("Failed to find")
        pass

# Tool for printing out options
def Context_Menu(g_dict):
    """Takes a dictionary and prints out the keys"""
    for key in g_dict:
        print(f" - {key}")

# These are the base functions for the player
def Move():
    """ Move Funtion allows the player moves between rooms, it takes no arguments
    but takes its data from the player character class. It will do everything to 
    showing the player what is available and update the character class to where 
    the player is."""
    print(f"You are currently at {player.location.name}.\n These are your options: ")
    Context_Menu(player.location.connecting_rooms)
    m_choice = input("Where to? or Stay(s):\n")
    if m_choice == "s":
        pass
    elif m_choice in player.location.connecting_rooms:
        new_location = Dict_parser(m_choice,player.location.connecting_rooms)
        player.location = new_location
        print(f'You moved to {player.location}')
    else:
        print(m_choice)
        print("Area not found, please try again")

def Inventory():
    """WIP: Should allow the character see, what is in their inventory and
    equip/use what is in there. """
    pass

def Search():
    """WIP: Should let the player inspect the room they are in, providing details
    and more options/intereactions they can have in the room."""
    print("You Look through the room and find:")
    Context_Menu(player.location.contents)
    print("What now? \n [look at (item name)] [Main Menu(m)]\n")
    s_choice = input()
    if s_choice == "m":
        pass
    elif s_choice in player.location.contents:
        print(f"You approach the {s_choice}.")
        focused_item = Dict_parser(s_choice, player.location.contents)
        print(focused_item.description)
        print('[Pick it up (p)] [Check the Count (c)] [Main Menu (m)]')
        inner_choice = input('What next?\n')
        if inner_choice == 'p':
            
            pass
        elif inner_choice == 'c':
            print(focused_item.count)
        else:
            print('Sorry, input did not match.')

def Quit():
    """ Allows player to quit the game safely and asks them if they are sure """
    exit_confirm = input("Are you sure? y/n:\n")
    if exit_confirm == 'y':
        print("Hero! We await your retrun!")
        sys.exit()
    else:
        print("Good Choice Adventure More!")
        pass

name = input("State your name: ")
c_class = input("What is your class? ")

player = Character(name, c_class)
print("What Now Adventurer?")
print(root_menu)
choice = input("Name Your Action!\n")

while True:
    if choice == "m":
        Move()
    elif choice == "i":
        print("inventory")
    elif choice == "s":
        Search()
    elif choice == "d":
        pass
    elif choice == "q":
        Quit()
    else:
        print('Wrong Choice')
    print("What Now Adventurer?")
    print(root_menu)
    choice = input("Make your Move:\n")
    

