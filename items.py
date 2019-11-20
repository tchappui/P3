from random import sample #import random.sample for init & add item in labyrinth

class Item:
    
    def __init__(self, name, position):
        self.name = name
        self.position
        
Item("needle", Position(10, 5))
("needle", Position(10, 5))

class Items:
    
    def __init__(self, labyrinth):
        self.labyrinth = labyrinth
        self.items = {}
        self.random = None
        self.position = None

    def add_items_randomly(self):
        positions = sample(
            set(self.labyrinth.paths)-{self.labyrinth.start, self.labyrinth.end}, 3)
        needle_pos, tube_pos, ether_pos = positions
        self.items[needle_pos] = "needle"
        self.items[tube_pos] = "tube"
        self.items[ether_pos] = "ether"
        
    def catch_item(self, position):
        if position in self.items:
            item = self.items[position]
            del self.items[position]
            return item
  
