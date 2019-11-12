from position import Position

class Labyrinth:
# Init item
    def __init__(self):
        self.start = None
        self.end = None
        self.guardian = None
        self.hero = None
        self.width = None
        self.height = None
        self.wall = []
        self.paths = []
        self.inventory = ["tube","needle","ether"] 
        self.bag = []

# load labyrinth file for reading the txt    
    def load_from_file(self,maze):
        with open(maze, "r") as carte: 
            for y, line in enumerate(carte):
                for x, col in enumerate(line):
                    position = Position(x , y)
                    if col == "d":
                        self.paths.append(position)
                        self.start = (position)
                    elif col == "e":
                        self.end = position
                    elif col == "g":
                        self.paths.append(position)
                        self.guardian = position
                    elif col == "#":
                        self.wall.append(position)
                    elif col == ".":
                        self.paths.append(position)

            self.width = x + 1
            self.height = y + 1

   #Console mode, placer mon mode console ici ou ailleurs ?
   
    def show_console(self):
        
        for y in range(self.height):
            for x in range(self.width):
                position = Position(x, y)
                if position == self.start:
                    print("d")
                elif position in self.inventory:
                    print # je sais pas quoi mettre ici
                elif position == self.hero:
                    print("h")
                elif position == self.guardian:
                    print("g")
                elif position == self.end:
                    print("e")
                elif position in self.paths:
                    print(".")
                elif position in self.wall:
                    print("#")

def main():


if __name__ == "__main__":
    main()