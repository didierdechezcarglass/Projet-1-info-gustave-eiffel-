from . import fltk as fl
from .button import Button

def evolve_color(cls, ball_index, index, delta):
    """
    updates the color with a certain delta
    """
    cls.ball_colors_rgb[ball_index][index] = min(255, max(0, cls.ball_colors_rgb[ball_index][index] + delta))

def convert_rgb(col):
    final_rgb = []
    for index in range(0, len(col), 2):
        final_rgb.append(int(col[index:index + 2], 16))
    return final_rgb

def rgb_to_hex(rgb):
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"

class BallColors:
    """
    scene for the ball colors, allows you to change the 4 colors of the balls
    """
    def __init__(self, menu_command, ball_colors, settings):
        self.settings = settings
        self.ball_colors = ball_colors
        self.ball_colors_rgb = [convert_rgb(color[1:]) for color in ball_colors]
        self.menu_button = Button((0, 0), (fl.largeur_fenetre() // 20, fl.hauteur_fenetre() // 20),
                                  ["<", "black", fl.largeur_fenetre() // 40], "red", command=menu_command)
        s_x = fl.largeur_fenetre() // len(self.ball_colors)
        start_y = fl.hauteur_fenetre() / 2 + min(fl.largeur_fenetre() / 16, fl.hauteur_fenetre() / 16)
        self.buttons = []
        s_y = fl.hauteur_fenetre() // 8
        for y in range(len(self.ball_colors)):
            for x in range(3):
                self.buttons.append(Button((y*s_x + s_x // 4, start_y +x*s_y), (s_x // 4, s_y), ["+", "black", s_y // 4], "green", command = lambda y=y, x=x: evolve_color(self, y, x, 5)))
                self.buttons.append(Button((y * s_x + s_x // 2, start_y + x * s_y), (s_x // 4, s_y), ["-", "black", s_y // 4], "red", command=lambda y=y, x=x: evolve_color(self, y, x, -5)))

    def update(self, event):
        coordinates = (fl.abscisse_souris(), fl.ordonnee_souris())
        self.menu_button.update(event, coordinates, self.ball_colors)
        for index, button in enumerate(self.buttons):
            button.update(event, coordinates)
            if button.click(event, coordinates):
                print(self.ball_colors[index // 6])
                excluded_rgb = self.ball_colors_rgb[0:index//6] + self.ball_colors_rgb[(index//6) + 1:]
                while self.ball_colors_rgb[index // 6] in excluded_rgb:
                    self.ball_colors_rgb[index // 6][0] = min(255, max(0, self.ball_colors_rgb[index // 6][0] + 5))
                self.ball_colors[index // 6] = rgb_to_hex(self.ball_colors_rgb[index // 6])

    def draw(self):
        s_x = fl.largeur_fenetre() // len(self.ball_colors)
        circ_rad = min(fl.largeur_fenetre() / 16, fl.hauteur_fenetre() / 16)
        for index, color in enumerate(self.ball_colors):
            fl.texte(index*s_x + s_x // 2, fl.hauteur_fenetre() // 2 - 3*int(circ_rad), str(self.ball_colors_rgb[index]), couleur = "black", taille = int(circ_rad / 2), ancrage = "center")
            fl.cercle(index*s_x + s_x / 2, fl.hauteur_fenetre() / 2 - circ_rad, circ_rad, "black", color)
        for button in self.buttons:
            button.draw()
        self.menu_button.draw()
