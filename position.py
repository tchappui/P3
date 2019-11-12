class Position:
    # Init x = horizontal, y = vertical
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #Deplacement    
    def up(self):
        return Position(self.y + 1, self.x)

    def down(self):
        return Position(self.y - 1, self.x)
    
    def left(self):
        return Position(self.x - 1, self.y)

    def right(self):
        return Position(self.x + 1, self.y)

    