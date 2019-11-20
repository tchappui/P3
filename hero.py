class Hero:
    def __init__(self, labyrinth):
        self.labyrinth = labyrinth
        self.position = None
        self.inventory = []
        
    def move(self, direction):
        # nouvelle_position <- demander à l'objet self.position de renvoyer la position dans direction
        new_position = self.position.get_new_position_from_direction(direction)
        # SI nouvelle_position est dans les chemins du labyrinthe:
        if new_position in self.labyrinth.paths:
            # Déplacer le héro
            self.position = new_position
            self.get_item()
            return self.fight_guardian()

    def get_item(self):
        item = self.labyrinth.items.catch_item(self.position)
        if item is not None:
            self.inventory.append(self.position)
    
    def fight_guardian(self):
        if self.position == self.labyrinth.end:
            if len(self.inventory) == 3:
                    return "win"
            else:
                    return "loss"
