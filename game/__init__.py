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
    def __init__(self):
        """
        constructor
        """
        self.__present_objects = [""] * 3

    @property
    def get_info(self) -> list:
        """
        returns the current object in tile self
        """
        return self.__present_objects

    def change_object(self, position : int, object : str):
        """
        sets the current object in list index position to string object
        """
        self.__present_objects[position] = object

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
        self.__grid: list = [[Tile() for _ in range(11)] for _ in range(11)]

    def show_info(self, x : int, y : int) -> list:
        """
        returns the info at grid position x,y
        """
        return self.__grid[y][x].get_info
    def add_object(self, x : int, y : int, lst_position : int, object) -> None:
        """
        adds the object to a list
        """
        self.__grid[y][x].change_object(lst_position, object)
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
    player ball containing info on wher
    """
    def __init__(self, player_id : int):
        """
        constructor
        """
        self.__player_id = player_id
        self.__alive = True
    @property
    def kill(self):
        self.__alive = False