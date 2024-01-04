"""
authors of the files:
Léo PIERRAT
Quentin BARTOLONE

setting scene file

classes:
Setting

functions:
No functions

imports:
fltk.py
button.py
"""
from . import fltk as fl
from .button import Button

class Setting:
    """
    setting scene for the game

    attributes:
    game -> the current game
    settings : dict -> all the settings used as arguments for instance typing Setting( ... , x = "2") then settings["x"] -> 2
    buttons : list -> the list of all buttons
    menu_button : Button -> the button that will send the user back to the menu

    methods:
    update(event : fl.TkEvent) -> None : updates the game
    draw() -> None : draws every item needed to be drawn for the scene
    """
    def __init__(self, game, menu_command: (), button_commands: list[()], **settings) -> None:
        """
        constructor
        """
        self.game = game
        self.settings = settings
        delta_y = fl.hauteur_fenetre() / len(self.settings)
        delta_x = fl.largeur_fenetre() / len(self.settings)
        text_sizey = min(int(delta_x / 10), int(delta_y / 10))
        self.buttons = []
        button_sizex = fl.largeur_fenetre() / 50
        button_sizey = text_sizey
        start_x = fl.largeur_fenetre() / 2
        start_y = 0
        # prepares the button placement for the settings, that way we can use them for later and update them
        for index, (setting, value) in enumerate(self.settings.items()):
            text_sizex = fl.taille_texte(f"{setting} : {value}", taille=text_sizey)[0]
            self.buttons.append((Button((start_x + text_sizex, start_y + (delta_y / 2) - text_sizey / 2),
                                        (button_sizex, button_sizey), ["+", "black", text_sizey],
                                        "orange", command=button_commands[index][0]),
                                Button((start_x + text_sizex + button_sizex, start_y + (delta_y / 2) - text_sizey / 2),
                                       (button_sizex, button_sizey), ["-", "black", text_sizey], "orange",
                                       command=button_commands[index][1])))
            start_y += delta_y
        self.menu_button = Button((0, 0), (button_sizex, button_sizey),
                                  ["<", "black", text_sizey], "red", command=menu_command)

    def update(self, event: fl.TkEvent) -> None:
        """
        updates the scene using the mouse
        """
        mouse_coordinates = (fl.abscisse_souris(), fl.ordonnee_souris())
        old_size = list(self.settings.values())[1:3]
        for b1, b2 in self.buttons:
            b1.update(event, mouse_coordinates, self.settings)
            b2.update(event, mouse_coordinates, self.settings)
        if old_size != list(self.settings.values())[1:3]:
            fl.redimensionne_fenetre(*list(self.settings.values())[1:3])
        self.menu_button.update(event, mouse_coordinates, self.settings)

    def draw(self) -> None:
        """
        draws the buttons
        """
        # calculation of new offsets
        start_y = 0
        delta_y = fl.hauteur_fenetre() / len(self.settings)
        delta_x = fl.largeur_fenetre() / len(self.settings)
        text_sizey = min(int(delta_x / 10), int(delta_y / 10))
        button_sizex = fl.largeur_fenetre() / 50
        button_sizey = text_sizey
        start_x = fl.largeur_fenetre() / 2 + text_sizey

        for index, (text, value) in enumerate(self.settings.items()):

            value = "Non" if value == 0 else "Oui" if value == 1 else value
            fl.texte(fl.largeur_fenetre() / 2,
                     start_y + delta_y / 2, f"{text} : {value}", taille=text_sizey, couleur="Black", ancrage="center")
            Button_1, Button_2 = self.buttons[index]
            text_sizex = fl.taille_texte(f"{text} : {value}", taille=text_sizey)[0] / 2

            # updates the buttons coordinates and draws the menu button
            Button_1.origin = start_x + text_sizex, start_y + (delta_y / 2) - text_sizey / 2
            Button_1.width, Button_1.height = button_sizex, button_sizey
            Button_2.origin = start_x + text_sizex + button_sizex, start_y + (delta_y / 2) - text_sizey / 2
            Button_2.width, Button_2.height = button_sizex, button_sizey
            Button_1.text_setting[2] = text_sizey
            Button_2.text_setting[2] = text_sizey
            Button_1.draw()
            Button_2.draw()
            start_y += delta_y

        # updates the menu button
        self.menu_button.width = button_sizex
        self.menu_button.height = button_sizey
        self.menu_button.text_setting[2] = text_sizey
        self.menu_button.draw()