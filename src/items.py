class Item:
    """The base class that generate items players can interact with"""
    def __init__(self, name, description, value = 0 ):
        self.name = name
        self.description = description
        self.value = value
    def quantity(self, count):
        self.count = count

class Weapon(Item):
    """These are weapons, base is item, but add attack stats to it"""
    def __init__(self, name, description, value, attack_points, speed):
        super().__init__(name, description, value)
        self.attack_points = attack_points
        self.speed = speed
    def __repr__(self):
        return f"|--{self.name}--|\n{self.description}\n Att: {self.attack_points} Spd: {self.speed}"


basic_items = {
    'gold': Item("Gold","Gold, its gold what do you think", 1),
    'ruby': Item("Ruby","Priceless gem, well we can find a price", 10),
    'diamond': Item("Diamond", "Wow, this gonna pay well", 100)
}

weapons = {
    'sword': Weapon("Sword", "Weapon of Choice of a Warrior", 10, 6, 1),
    'wand': Weapon("Wand", "The tool of a Mage", 10, 3, 2),
    'dagger': Weapon("Dagger", "Tool to Trick the Trade", 10, 2, 3),
    'bow': Weapon("Bow", "Quick Shot", 10, 1, 6)
}
