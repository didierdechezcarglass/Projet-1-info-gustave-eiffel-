import random
def random_tirette():
    random_binary=[random.randint(2, 8),random.randint(2, 8)]
    return [random.randint(0,1) if (i not in random_binary and i not in (0,1)) else 0 for i in range(7)]

def decale(lst, sens):
    new_lst = [0] * len(lst)
    for i in range(len(lst)):
        directed = (i + sens) % len(lst)
        new_lst[directed] = lst[i]
    return new_lst

class Tirette:
    def __init__(self, index, affects):
        """
        classe représentant les tirettes du jeu
        celle ci permet de stocker les informations de la tirette, c'est à dire sa position, son
        sens et les positions des trous de la tirette
        la classe dispose également de méthodes permettant de manipuler dans les besoins du jeu
        la liste contenant les positions des trous, et enfin d'afficher la tirette
        """
        self.trous = random_tirette()
        self.index = index
        # original position
        self.position = 1
        if affects == "vert":
            self.affect = self.affect_vertical
        else:
            self.affect = self.affect_horizontal
    def decalage(self,sens):
        internal_incr = sens
        self.trous = decale(self.trous,sens)
        self.position += internal_incr
        return self.trous
    def affiche(self):
        """
        affichage des tirettes sur l'interface graphique
        """
        pass

    def affect_vertical(self, grid):
        for vert in range(grid.vertical_length):
            grid.affect_hole(self.index, vert, "vert", self.trous[vert])
    def affect_horizontal(self, grid):
        for hor in range(grid.horizontal_length):
            grid.affect_hole(hor, self.index, "hor", self.trous[hor])
