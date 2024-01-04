"""
authors of the files:
Léo PIERRAT
Quentin BARTOLONE

main file to run the pieges game

classes:
No classes

Function:
No functions

imports:

engine
engine/menu_scene.py
"""
from engine import Renderer
from engine.menu_scene import Menu

app = Renderer((800, 600))
app.scene = Menu(app)
app.run()
