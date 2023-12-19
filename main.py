from engine import Renderer
from engine.menu_scene import Menu


app = Renderer((800, 600))
app.scene = Menu(app)
app.run()
