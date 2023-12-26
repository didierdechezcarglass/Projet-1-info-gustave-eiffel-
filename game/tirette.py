import random
def random_tirette():
    n_holes = random.randint(3, 5)
    ls_holes = [0] * 7
    avail_index = [i for i in range(len(ls_holes))]
    for hole in range(1, len(ls_holes), 2):
        ls_holes[hole] = 1
        n_holes -= 1
        avail_index.remove(hole)
    while n_holes > 0:
        new_hole = avail_index.pop(random.randint(0, len(avail_index) - 1))
        ls_holes[new_hole] = 1
        n_holes -= 1

    return [0] + ls_holes + [0]

def decale(lst, sens):
    new_lst = [0] * len(lst)
    for i in range(1, len(lst) - 1):
        directed = (i + sens)
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
        if 0 <= self.position + internal_incr <= 2:
            self.trous = decale(self.trous, sens)
            self.position += internal_incr
        return self.trous

    def affect_vertical(self, grid):
        for vert in range(grid.vertical_length):
            grid.affect_hole(self.index, vert, "vert", self.trous[vert + 1])
    def affect_horizontal(self, grid):

        for hor in range(grid.horizontal_length):
            grid.affect_hole(hor, self.index, "hor", self.trous[hor + 1])
