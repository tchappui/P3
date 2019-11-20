from random import sample #import random.sample for init & add item in labyrinth

class Items:
    
    def __init__(self, labyrinth):
        self.labyrinth = labyrinth
        self.item = []
        self.random = None
        self.position = None

    def initialize_random_positions(self):
        self.random = iter(
            random.sample(self.labyrinth.paths, k=len(self.labyrinth.paths))
        )

    def add_item_randomly(self, item):
        self.item = random.sample(
            set(self.labyrinth.paths)-{self.labyrinth.start, self.labyrinth.end}, 3)
        return self.item
