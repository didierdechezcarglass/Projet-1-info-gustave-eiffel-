"""
class managing the buttons

classes:
Button

imports:
fltk.py
"""
from . import fltk as fl
class Button:
    """
    Button that can be clicked to execute a command

    attributes :
    origin : tuple[int, int] -> the origin of the button
    width, height : int -> the size of the button
    command : () -> function to execute when the button is clicked
    text_setting : list[3] -> list containing the parameters of the text
    color : str -> color of the button
    image : str -> path of the image, default is "" which means no image

    methods:
    update(event, coordinates, *commandparams, **commandparamdict) -> None:
        updates the button and add the possible parameters for the button command (as dict and list)
    click(event, coordinates) -> Bool:
        checks if the button is clicked
    hover(coordinates) -> Bool:
        checks if the button is hovered
    draw() -> None:
        draws the button
    """
    def __init__(self, coord, size, text_setting, color="green", image="", command: () = lambda : None):
        """
        constructor
        """
        self.origin = coord
        self.width, self.height = size
        self.command = command
        self.text_setting = text_setting
        self.command = command
        # sets the draw method in function of parameter image
        # (if no image draw with image, else draw without img)
        if image:
            self.draw = self.draw_image
        else:
            self.draw = self.draw_without_image
        self.color = color
        self.image = image
    def update(self, event, coordinates, *commandparams, **commandparamsdict):
        """
        updates the button to execute the command if clicked
        """
        if self.click(event, coordinates):
            self.command(*commandparams, **commandparamsdict)
    def hover(self, coordinates: tuple[int, int]) -> bool:
        """
        checks if the button is hovered

        >>> t = Button((0, 0), (10, 10), [])
        >>> t.hover((2, 2))
        True
        >>> t.hover((100, 100))
        False
        """
        return (self.origin[0] <= coordinates[0] <= self.origin[0]+self.width) and\
               (self.origin[1] <= coordinates[1] <= self.origin[1]+self.height)

    def click(self, event, coordinates: tuple[int, int]) -> bool:
        """
        checks if the button is clicked
        >>> t = Button((0, 0), (10, 10), [])
        >>> leftclick = ["ClicGauche"]
        >>> t.click(leftclick, (2,2))
        True
        >>> t.click([""], (2,2))
        False
        >>> t.click([""], (100, 100))
        False
        >>> t.click(leftclick, (100, 100))
        False
        """
        return self.hover(coordinates) and fl.type_ev(event) == "ClicGauche"

    def draw_image(self) -> None:
        """
        draws the image of the button
        """
        fl.image(*self.origin, self.image,
                 largeur=self.width, hauteur=self.height, ancrage="nw")
        text_cent = self.origin[0]+(self.width/2), self.origin[1]+(self.height/2),
        fl.texte(*text_cent, self.text_setting[0],
                 couleur=self.text_setting[1], taille=self.text_setting[2], ancrage="center")

    def draw_without_image(self) -> None:
        """
        draws the button without the image
        """
        southeast = [self.origin[0] + self.width,
                     self.origin[1] + self.height]
        fl.rectangle(*self.origin, *southeast,
                     remplissage=self.color)
        text_cent = self.origin[0]+(self.width/2),\
            self.origin[1]+(self.height/2),
        fl.texte(*text_cent, self.text_setting[0],
                 couleur=self.text_setting[1],
                 taille=self.text_setting[2], ancrage="center")

