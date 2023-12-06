from engine import Renderer
from engine.game_scene import Game
app = Renderer((800, 600))
app.scene = Game()
app.run()