class Tile:
    """
    Tile containing information regarding position and stored items

    constructor:
    --> needs argument position

    methods:
    get_info
    change_object(self, position, object)

    attributes:
    __present_objects : list -> private attributes than can only be modified using change_object
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
        return [str(self.__current_ball), self.__vertical_hole, self.__horizontal_hole]

    def change_hole(self, hole_type : str, hole_value : bool | int) -> None:
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
        self.__current_ball = ball
class Grid:
    """
    7x7 grid for the game

    methods:

    attributes:
    """
    def __init__(self) -> None:
        """
        constructor
        """
        self.__grid: list = [[Tile() for _ in range(7)] for _ in range(7)]
        self.horizontal_length = 7
        self.vertical_length = 7

    def show_info(self, x : int, y : int) -> list:
        """
        returns the info at grid position x,y
        """
        return self.__grid[y][x].get_info
    def affect_hole(self, x : int, y : int, hole_type : str, hole : bool) -> None:
        """
        adds the object to a list
        """
        self.__grid[y][x].change_hole(hole_type, hole)
    def set_ball(self, x : int, y : int, ball):
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
    """
    def __init__(self, player_id : int):
        """
        constructor
        """
        self.__player_id = player_id
        self.__alive = True
    def kill(self):
        self.__alive = False

    def __str__(self):
        return str((self.__player_id, self.__alive))

    def draw(self):
        pass
