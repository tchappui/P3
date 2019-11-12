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
    def catch_item(self):
        # item - Demander à self.labyrinthe de me renvoyer l'objet situé à self.position
        item = self.labyrinth.get_item_located_at(self.position)
        # AJouter objet dans la liste self.bag (self.bag.append(item))
        self.bag.append(item)

    def fight_guardian(self):
        if self.position == self.labyrinth.end:
            if self.bag == 3:
                return 1
            else:
                return 0
