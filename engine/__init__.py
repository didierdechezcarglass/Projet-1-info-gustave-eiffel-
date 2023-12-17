from . import fltk as fl

class Renderer:
    """
    main game class that allows the user to run a gameloop
    """
    def __init__(self, res):
        self.scene = None
        fl.cree_fenetre(*res, redimension=False)
        self.__running = False

    def stop(self):
        self.__running = False

    def update(self, event):

        if self.scene is not None:
            self.scene.update(event)
            self.scene.draw()

    def run(self):
        self.__running = True
        while self.__running:
            event = fl.donne_ev()
            if fl.type_ev(event) == "Quitte":
                self.__running = False
            fl.efface_tout()
            self.update(event)
            fl.mise_a_jour()