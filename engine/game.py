from game import Grid,Ball
from game.tirette import Tirette
class Game:
    def __init__(self):
        self.atm_running=None

        self.grid=Grid()
        tirette_vert=[]
        tirette_horizon=[]
        for loop in range(self.grid.vertical_length):
            tirette_vert.append(Tirette(loop,'vert'))
            tirette_vert[-1].affect(self.grid)
        for loop in range(self.grid.horizontal_length):
            tirette_horizon.append(Tirette(loop,"hor"))
            tirette_horizon[-1].affect(self.grid)
        
    def update(self, event):
        if fl.type_ev(event)
    def draw(self):
        """
        draws the game scene
        """
        pass