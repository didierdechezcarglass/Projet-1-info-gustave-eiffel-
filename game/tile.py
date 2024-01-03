"""
the file containing the tile= class

classes:
Tile
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

