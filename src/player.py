# Write a class to hold player information, e.g. what room they are in
# currently.
class Character:
    """Creates Characters and acts the The base class for all other entities"""
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.inventory = []

class Player_Character(Character):
    """Creates the Player Character, its a child to the Character Class"""
    def __init__(self, name, description, c_class, location):
        super().__init__(name, description)
        self.c_class = c_class
        self.location = location
    def __repr__(self):
        return "{self.name} the {self.description} {self.c_class}".format(self = self)
    def player_inventory_add(self, item):
        self.inventory.append(item)