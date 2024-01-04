"""
authors of the files:
Léo PIERRAT
Quentin BARTOLONE

modules that manages the tirettes

classes:
Tirette

functions:
random_tirette
decale

imports:
random.py (built in)
"""
import random


def random_tirette() -> list:
    """
    creates a random tirette
    >>> import random
    >>> random.seed(1)
    >>> random_tirette()
    [0, 0, 1, 0, 1, 0, 1, 0, 0]
    """
    n_holes = random.randint(3, 5)
    ls_holes = [0] * 7
    avail_index = list(range(len(ls_holes)))
    for hole in range(1, len(ls_holes), 2):
        ls_holes[hole] = 1
        n_holes -= 1
        avail_index.remove(hole)
    while n_holes > 0:
        new_hole = avail_index.pop(random.randint(0, len(avail_index) - 1))
        ls_holes[new_hole] = 1
        n_holes -= 1

    return [0] + ls_holes + [0]


def decale(lst: list, sens: int) -> list:
    """
    moves a list to a certain sense sens
    note that the first and last values of the list are not affected as it is not a circular move

    >>> decale([0, 0, 1, 1, 1, 1, 0, 0], 1)
    [0, 0, 0, 1, 1, 1, 1, 0]
    >>> decale([0, 0, 1, 1, 1, 1, 0, 0], -1)
    [0, 1, 1, 1, 1, 0, 0, 0]
    """
    new_lst = [0] * len(lst)
    for i in range(1, len(lst) - 1):
        directed = i + sens
        new_lst[directed] = lst[i]
    return new_lst


class Tirette:
    """
    the class that manages the tirettes

    attributes:
    trous : list -> the holes of the tirette
    index : int -> the index of the tirette in the grid
    position : int -> the tirettes current status (0, 1, 2)
    affect : () -> will affect the grid vertically or horizontally once called
    methods:
    decalage(sens: int) -> list : moves the holes of the tirette to a certain sense sens if possible
    affect_vertical(grid : Grid) -> None : affects the grid of the game using the tirettes index
    affect_horizontal(grid : Grid) -> None: does the same as affect_vertical
    """
    def __init__(self, index: int, affects: str) -> None:
        """
        constructor
        """
        self.trous = random_tirette()
        self.index = index
        # original position
        self.position = 1
        if affects == "vert":
            self.affect = self.affect_vertical
        else:
            self.affect = self.affect_horizontal

    def decalage(self, sens: int) -> list:
        """
        moves the tirette holes if possible
        """
        internal_incr = sens
        if 0 <= self.position + internal_incr <= 2:
            self.trous = decale(self.trous, sens)
            self.position += internal_incr
        return self.trous

    def affect_vertical(self, grid) -> None:
        """
        affects the grid vertically
        """
        for vert in range(grid.vertical_length):
            grid.affect_hole(self.index, vert, "vert", self.trous[vert + 1])

    def affect_horizontal(self, grid) -> None:
        """
        affects the grid horizontally
        """
        for hor in range(grid.horizontal_length):
            grid.affect_hole(hor, self.index, "hor", self.trous[hor + 1])
