from position import Position
from items import Items
from labyrinth import Labyrinth



class Hero:
    def __init__(self,labyrinth): 
        self.position = Position()  # lien vers l'instance de position correspondante
        self.labyrinth = Labyrinth()  # lien vers l'instance du labyrinth
        self.items = Items()

    def move(self, direction):
        # nouvelle_position <- demander à l'objet self.position de renvoyer la position dans direction
        new_position = self.position.get_new_position_from_direction(direction)
        # SI nouvelle_position est dans les chemins du labyrinthe:
        if new_position in self.labyrinth.paths:
            # Déplacer le héro
            self.position = new_position
        # SI self.position est dans la liste d'items de labyrinthe:
        if self.labyrinth.has_item_on_position(self.position):
            # ramasser l'objet
            self.labyrinth.has_item_on_position.append(self.labyrinth.inventory[0]) # Je ne sais pas si je dois mettre les objets de ma liste ou laisser vide.