"""
authors of the files:
Léo PIERRAT
Quentin BARTOLONE

the file containning the ball class

classes:
Ball
"""


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
