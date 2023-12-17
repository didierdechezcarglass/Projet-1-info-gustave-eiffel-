from .menu_scene import Menu
from .setting_scene import Setting
from .game_scene import Game

def switch_game(app, params):
    """
    switches to the game scene
    """
    app.scene = Game(*params)

def switch_setting(app, params):
    """
    switches to the setting scene
    """
    app.scene = Setting(*params)

def switch_menu(app, params):
    """
    switches to the menu
    """
    app.scene = Menu(*params)

