from . import fltk as fl

class Renderer:
    """
    main game class that allows the user to run a gameloop
    attributes:

    scene : Any ->  current scene of the game (will be set to None at the __init__)
    __running : False -> sets the game to a running state
    """
    def __init__(self, res: tuple[int, int]) -> None:
        """
        constructor
        """
        self.scene = None
        fl.cree_fenetre(*res, redimension=False)
        self.__running = False

    def stop(self) -> None:
        """
        stops the game
        """
        self.__running = False

    def update(self, event) -> None:
        """
        updates the current scene using the current event collected in the mainloop
        """
        if self.scene is not None:
            self.scene.update(event)
            self.scene.draw()

    def run(self) -> None:
        """
        runs the game
        """
        self.__running = True
        while self.__running:
            event = fl.donne_ev()
            if fl.type_ev(event) == "Quitte":
                self.__running = False
            fl.efface_tout()
            self.update(event)
            fl.mise_a_jour()