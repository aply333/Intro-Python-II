# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    """Takes name, description, and create rooms players can traverse through"""
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connecting_rooms = {}
        self.contents = []
    def __repr__(self):
        return '{self.name}'.format(self=self)
    def __str__(self):
        return '{self.name}'.format(self=self)
    def n_to(self, key, destination):
        """Takes a key and destination, adding to a dictionary of connecting rooms
        each, creates a attribute dictating its direction """
        self.north = destination
        self.connecting_rooms.update([(key, destination)])
    def s_to(self, key, destination):
        """Same as n_to, but for south"""
        self.south = destination
        self.connecting_rooms.update([(key, destination)])
    def e_to(self, key, destination):
        """Same as n_to, but for east"""
        self.east = destination
        self.connecting_rooms.update([(key, destination)])
    def w_to(self, key, destination):
        """Same as n_to, but for west"""
        self.west = destination
        self.connecting_rooms.update([(key, destination)])
    def room_contents(self, item, count):
        """Take an item and count and adds it to the room"""
        content = {
            "item": item,
            "quantity": count
        }
        self.contents.append(content)