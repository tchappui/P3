from random import sample

class Items:
    
    def __init__(self, labyrinth,name):
        self.labyrinth = labyrinth
        self.items = {}
        self.random = None
        self.position = None
        self.name = name
        
    def initialize_random_positions(self):
        self.random = iter(
            random.sample(self.labyrinth.paths, k=len(self.labyrinth.paths))
        )

    def add_item_randomly(self, item):
        item.position = next(self.labyrinth.random)
        self.items[item.position] = item

   
