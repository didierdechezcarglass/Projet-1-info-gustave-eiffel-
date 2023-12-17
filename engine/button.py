from . import fltk as fl
class Button:
    def __init__(self, coord, size, text_setting, color="green", image="", command: () = lambda : None):
        """
        nw : (x,y), x and y are coordinates of """
        self.origin = coord
        self.width, self.height = size
        self.command = command
        self.text_setting = text_setting
        self.command = command
        if image:
            self.draw = self.draw_image
        else:
            self.draw = self.draw_without_image
        self.color = color
        self.image = image
    def update(self, event, coordinates, *commandparams, **commandparamsdict):
        if self.click(event, coordinates):
            self.command(*commandparams, **commandparamsdict)
    def hover(self, coordinates):
        return (self.origin[0] <= coordinates[0] <= self.origin[0]+self.width) and (self.origin[1] <= coordinates[1] <= self.origin[1]+self.height)
    def click(self, event, coordinates):
        return self.hover(coordinates) and fl.type_ev(event) == "ClicGauche"
    def draw_image(self):
        fl.image(*self.origin, self.image, largeur=self.width, hauteur=self.height, ancrage="nw")
        text_cent = self.origin[0]+(self.width/2), self.origin[1]+(self.height/2),
        fl.texte(*text_cent, self.text_setting[0], couleur=self.text_setting[1], taille=self.text_setting[2], ancrage="center")

    def draw_without_image(self):
        southeast = [self.origin[0] + self.width, self.origin[1] + self.height]
        fl.rectangle(*self.origin, *southeast, remplissage = self.color)
        text_cent = self.origin[0]+(self.width/2), self.origin[1]+(self.height/2),
        fl.texte(*text_cent, self.text_setting[0], couleur = self.text_setting[1], taille=self.text_setting[2], ancrage="center")