class Labyrinth:
    def __init__(self):
        self.paths = []
        self.walls = []
        self.end = None
        self.guardian = None
        self.start = None
        self.hero = None
        self.items = Items(labyrinth=self)

        # instancier les items et leur donner une position

    def load_from_file(self, maze):
        with open(maze, "r") as carte:
            for y, line in enumerate(carte):
                for x, col in enumerate(line):
                    position = Position(x, y)
                    if col == "d":
                        self.start = position
                    elif col == "e":
                        self.end = position
                    elif col == "#":
                        self.walls.append(position)
                    elif col == ".":
                        self.paths.append(position)

        self.items.initialize_random_positions()
        self.paths.append(self.start)
        self.paths.append(self.end)

    def add_guardian(self, guardian):
        self.guardian = guardian
        self.guardian.position = self.end
    
    def add_hero(self,hero):
        self.hero = hero
        self.hero.position = self.start
