"""
management of the menu scene

functions:
update_setting
get_default
menu_command
set_setting
set_game
set_ballcolor

classes:
Menu

imports
button.py
fltk.py
game_scene.py
setting_scene.py
ballcolor_scene.py
"""
from .button import Button
from . import fltk as fl
from .game_scene import Game
from .setting_scene import Setting
from .ballcolor_scene import BallColors


def update_setting(settings, key, min_max, delta) -> None:
    """
    updates a certain setting in function of a certain offset
    """
    settings[key] = min(min_max[1], max(min_max[0], settings[key] + delta))


def get_default(param = fl):
    """
    returns the default settings of the game
    >>> class nothing : pass
    >>> fl = nothing()
    >>> setattr(fl, "largeur_fenetre", lambda : 800)
    >>> setattr(fl, "hauteur_fenetre", lambda : 600)
    >>> get_default(fl)
    {'Nombre Joueurs': 4, 'Largeur Fenêtre': 800, 'Hauteur Fenêtre': 600, 'phase de placement': 1}
    """
    return {"Nombre Joueurs": 4,
            "Largeur Fenêtre": param.largeur_fenetre(),
            "Hauteur Fenêtre": param.hauteur_fenetre(),
            "phase de placement": 1}


DEFAULT_COLORS = ["#0000FF", "#00FFFF", "#FFFF00", "#000000"]


def menu_command(app, cached_settings: list | tuple):
    """
    command to switch back to the menu, used for all the other scenes
    """
    app.scene = Menu(app, *cached_settings)


def set_setting(app, cls) -> None:
    """
    sets the scene of the app to setting, as well as taking the menu command to it
    """
    app.scene = Setting(app,
                        lambda settings: menu_command(app, (settings, cls.ball_color_settings)),
                        cls.button_commands, **cls.game_setting)


def set_game(app, cls) -> None:
    """
    sets the scene of the app to Game, as well as taking the menu command to it
    """
    app.scene = Game(cls.ball_color_settings, cls.game_setting["Nombre Joueurs"],
                     lambda settings: menu_command(app, (settings, cls.ball_color_settings)),
                     cls.game_setting["phase de placement"])


def set_ballcolor(app, cls) -> None:
    """
    sets the scene of the app to ballcolor, as well as taking the menu command to it
    """
    app.scene = BallColors(lambda colors: menu_command(app, (cls.game_setting, colors)),
                           cls.ball_color_settings, cls.game_setting)


class Menu:
    """
    Menu class, controls button commands and scene switching

    attributes:
    game_setting : dict | None -> the setting of the game
    ball_colors : list | None -> the ball color
    button_commands : list -> all the commands for incrementing / decrementing settings
    app : Renderer -> the Renderer class (see __init__.py for more info)
    buttons : list -> all the buttons that will be displayed for switching scenes

    methods:
    update(event : fl.TkEvent) -> None : updates all the buttons
    draw() -> None : draws all the buttons
    """
    def __init__(self, app, params=None, ball_colors=None) -> None:

        if params is None:
            params = get_default()
        if ball_colors is None:
            ball_colors = DEFAULT_COLORS

        self.game_setting = params
        self.ball_color_settings = ball_colors
        # all the commands to update the settings for the game
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
        # all the commands to switch scenes
        commands = [lambda: set_game(self.app, self),
                    lambda: set_setting(self.app, self),
                    lambda: set_ballcolor(self.app, self),
                    lambda: self.app.stop()]
        # all the button prompts
        prompts = ["Jouer", "Paramètres", "Couleur balles", "Quitter"]
        for i in range(4):
            self.buttons.append(Button((button_x, i * delta_y + fl.hauteur_fenetre() // 20),
                                       (size_x, size_y),
                                       [prompts[i], "black", min(size_x // 10, size_y // 2)],
                                       "blue", command=commands[i]))

    def update(self, event: fl.TkEvent) -> None:
        """
        updates the current state of the game
        """
        mouse_coordinates = (fl.abscisse_souris(), fl.ordonnee_souris())
        for button in self.buttons:
            button.update(event, mouse_coordinates)

    def draw(self) -> None:
        """
        draws the buttons of the scene
        """
        for button in self.buttons:
            button.draw()