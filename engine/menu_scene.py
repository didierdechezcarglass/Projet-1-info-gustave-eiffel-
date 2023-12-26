from .button import Button
from . import fltk as fl
from .game_scene import Game
from .setting_scene import Setting
from .ballcolor_scene import BallColors
def update_setting(settings, key, min_max, delta):
    settings[key] = min(min_max[1], max(min_max[0], settings[key] + delta))

def get_default():
    return {"Nombre Joueurs" : 4, "Largeur Fenêtre" :  fl.largeur_fenetre(), "Hauteur Fenêtre" : fl.hauteur_fenetre(), "phase de placement" : 1}
DEFAULT_COLORS = ["#0000FF", "#00FFFF", "#FFFF00", "#000000"]
def menu_command(app, cached_settings):
    app.scene = Menu(app, *cached_settings)
def set_setting(app, cls):
    app.scene = Setting(app, lambda settings: menu_command(app, (settings, cls.ball_color_settings)), cls.button_commands, **cls.game_setting)

def set_game(app, cls):
    app.scene = Game(cls.ball_color_settings, cls.game_setting["Nombre Joueurs"], lambda settings: menu_command(app, (settings, cls.ball_color_settings)), cls.game_setting["phase de placement"])

def set_ballcolor(app, cls):
    app.scene = BallColors(lambda colors : menu_command(app, (cls.game_setting, colors)), cls.ball_color_settings, cls.game_setting)
class Menu:
    def __init__(self, app, params=None, ball_colors= DEFAULT_COLORS):
        if params is None:
            params = get_default()
        self.game_setting = params
        self.ball_color_settings = ball_colors
        self.button_commands = [
                            (lambda setting: update_setting(setting, "Nombre Joueurs", (2, 4),  1),
                             lambda setting: update_setting(setting, "Nombre Joueurs", (2, 4),  -1)),
                            (lambda setting: update_setting(setting, "Largeur Fenêtre", (400, 1900),  100),
                             lambda setting: update_setting(setting, "Largeur Fenêtre", (400, 1920),  -100)),
                            (lambda setting: update_setting(setting, "Hauteur Fenêtre", (400, 1000),  100),
                             lambda setting: update_setting(setting, "Hauteur Fenêtre", (400, 1080),  -100)),
                            (lambda setting: update_setting(setting, "phase de placement", (0, 1), 1),
                             lambda setting: update_setting(setting, "phase de placement", (0, 1), -1))
        ]
        self.app = app
        self.buttons = []
        size_x = (fl.largeur_fenetre()) - (2 * fl.largeur_fenetre() // 10)
        button_x = (fl.largeur_fenetre() // 10)
        size_y = (fl.hauteur_fenetre() // 4) - (2*fl.hauteur_fenetre() // 20)
        delta_y = fl.hauteur_fenetre() // 4
        commands = [lambda: set_game(self.app, self), lambda: set_setting(self.app, self), lambda : set_ballcolor(self.app, self), lambda : self.app.stop()]
        prompts = ["Jouer", "Paramètres", "Couleur balles", "Quitter"]
        for i in range(4):
            self.buttons.append(Button((button_x, i*delta_y + fl.hauteur_fenetre() // 20), (size_x, size_y), [prompts[i], "black", min(size_x // 10, size_y // 2)], "blue", command=commands[i]))

    def update(self, event):
        mouse_coordinates = (fl.abscisse_souris(), fl.ordonnee_souris())
        for button in self.buttons:
            button.update(event, mouse_coordinates)
    def draw(self):
        for button in self.buttons:
            button.draw()