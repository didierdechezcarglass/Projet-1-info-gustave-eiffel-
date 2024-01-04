"""
authors of the files:
Léo PIERRAT
Quentin BARTOLONE

manipulation of grid

classes:
Grid

import:
tile.py
"""
from .tile import Tile


class Grid:
    """
    7x7 grid for the game

    attributes:
    horizontal_length : int = 7 -> the grids horizontal length
    vertical_length : int = 7 -> the grids vertical length
    methods:
    show_info(x : int, y : int) -> list : the info of a grid at point x,y
    affect_hole(x: int, y: int, hole_type: str, hole: bool) -> None : affects hole at position x,y
    set_ball(x: int, y: int, ball : Ball) -> None : sets the ball at x,y to ball
    __str__() -> str : the python __str__ overloading for print() and str() conversion
    """
    def __init__(self) -> None:
        """
        constructor
        """
        self.__grid: list = [[Tile() for _ in range(7)] for _ in range(7)]
        self.horizontal_length = 7
        self.vertical_length = 7

    def show_info(self, x: int, y: int) -> list:
        """
        returns the info at grid position x,y
        >>> t = Grid()
        >>> t.show_info(0, 0)
        [None, 0, 0]
        >>> t.show_info(1, 1)
        [None, 0, 0]
        """
        return self.__grid[y][x].get_info

    def affect_hole(self, x: int, y: int, hole_type: str, hole: bool) -> None:
        """
        adds the object to a list
        """
        self.__grid[y][x].change_hole(hole_type, hole)

    def set_ball(self, x: int, y: int, ball) -> None:
        """
        sets the current ball of the grid at position x,y
        """
        self.__grid[y][x].set_ball(ball)

    def __str__(self) -> str:
        """
        prints the whole grid
        """
        matrix = []
        for lst in self.__grid:
            full_elt = ""
            for elt in lst:
                full_elt += "" + str(elt.get_info)
            matrix.append(full_elt)

        return str(matrix)
