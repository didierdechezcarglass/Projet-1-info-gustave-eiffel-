"""
manipulation of tiles and grid

classes:
Tile
Grid
Ball
"""


class Tile:
    """
    Tile containing information regarding position and stored items

    attributes:
    no public attributes

    methods:
    change_hole(hole_type : str, hole_value : bool | int) -> None: changes the hole (vert or hor) to value hole_value
    set_ball(ball: Ball) -> None: sets the to ball of tile to ball
    """
    def __init__(self) -> None:
        """
        constructor
        """
        self.__current_ball = None
        self.__vertical_hole = 0
        self.__horizontal_hole = 0

    @property
    def get_info(self) -> list:
        """
        returns the current object in tile self
        """
        return [self.__current_ball, self.__vertical_hole, self.__horizontal_hole]

    def change_hole(self, hole_type: str, hole_value: bool | int) -> None:
        """
        changes the hole inside the tile  and possibly removes the ball
        """
        if hole_type == "vert":
            self.__vertical_hole = hole_value
        if hole_type == "hor":
            self.__horizontal_hole = hole_value
        if all([self.__horizontal_hole, self.__vertical_hole]) and self.__current_ball is not None:
            self.__current_ball.kill()

    def set_ball(self, ball):
        """
        sets the current ball of the tile to a ball ball
        """
        self.__current_ball = ball


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


class Ball:
    """
    player ball containing status and player info

    attributes:
    no public attributes

    methods:
    kill() -> sets the ball to dead in the private attributes
    __str__() -> operator overloading for print to show the balls info

    properties:
    alive -> checks if the ball is alive
    identity -> gives the current id of the ball
    """
    def __init__(self, player_id: int) -> None:
        """
        constructor
        """
        self.__player_id = player_id
        self.__alive = True
    def kill(self) -> None:
        """
        kills the ball
        """
        self.__alive = False

    def __str__(self) -> str:
        """
        the str operator overloading for print() and str()
        """
        return str((self.__player_id, self.__alive))

    @property
    def alive(self) -> bool:
        """
        returns the current status of the ball (dead or alive)
        """
        return self.__alive

    @property
    def identity(self) -> int:
        """
        returns the player assigned to the ball
        """
        return self.__player_id
