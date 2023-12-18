from . import fltk as fl
from .button import Button
#from .sceneswitcher import switch_menu

class Setting:
    """
    setting scene for the game
    """
    def __init__(self, game, menu_command, button_commands, **settings):
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
        for index, (setting, value) in enumerate(self.settings.items()):
            text_sizex = fl.taille_texte(f"{setting} : {value}", taille=text_sizey)[0]
            self.buttons.append((Button((start_x + text_sizex, start_y + (delta_y / 2) - text_sizey / 2), (button_sizex, button_sizey), ["+", "black", text_sizey], "orange", command=button_commands[index][0]),
                                Button((start_x + text_sizex + button_sizex, start_y + (delta_y / 2)  - text_sizey / 2), (button_sizex, button_sizey), ["-", "black", text_sizey], "orange", command=button_commands[index][1])))
            start_y += delta_y
        self.menu_button = Button((0, 0), (button_sizex, button_sizey), ["<", "black", text_sizey], "red", command=menu_command)

    def update(self, event):
        mouse_coordinates = (fl.abscisse_souris(), fl.ordonnee_souris())
        old_size = self.settings.values()
        if fl.type_ev(event) == "ClicDroit":
            print(self.settings)
        for b1, b2 in self.buttons:
            b1.update(event, mouse_coordinates, self.settings)
            b2.update(event, mouse_coordinates, self.settings)
        if old_size != self.settings.values():
            fl.redimensionne_fenetre(*list(self.settings.values())[1:3])
        self.menu_button.update(event, mouse_coordinates, self.settings)
    def draw(self):
        start_y = 0
        delta_y = fl.hauteur_fenetre() / len(self.settings)
        delta_x = fl.largeur_fenetre() / len(self.settings)
        text_sizey = min(int(delta_x / 10), int(delta_y / 10))
        button_sizex = fl.largeur_fenetre() / 50
        button_sizey = text_sizey
        start_x = fl.largeur_fenetre() / 2 + text_sizey
        for index, (text, value) in enumerate(self.settings.items()):
            fl.texte(fl.largeur_fenetre() / 2, start_y + delta_y / 2, f"{text} : {value}", taille = text_sizey, couleur = "Black", ancrage = "center")
            Button_1, Button_2 = self.buttons[index]
            text_sizex = fl.taille_texte(f"{text} : {value}", taille=text_sizey)[0] / 2
            Button_1.origin = start_x + text_sizex, start_y + (delta_y / 2) - text_sizey / 2
            Button_1.width, Button_1.height = button_sizex, button_sizey
            Button_2.origin = start_x + text_sizex + button_sizex, start_y + (delta_y / 2) - text_sizey / 2
            Button_2.width, Button_2.height = button_sizex, button_sizey
            Button_1.text_setting[2] = text_sizey
            Button_2.text_setting[2] = text_sizey
            Button_1.draw()
            Button_2.draw()
            start_y += delta_y
        self.menu_button.width = button_sizex
        self.menu_button.height = button_sizey
        self.menu_button.draw()