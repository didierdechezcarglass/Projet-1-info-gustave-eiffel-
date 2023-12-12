from .button import Button
from . import fltk as fl
class Menu:
    def __init__(self):
        self.state=None
        self.path="./images/ciel.jpg"
        self.button_image_path="./images/cielsombre.jpeg"
        self.bouton=Button((100,100),600,100,"BONJOUR","blue",self.button_image_path,picker="image")
        self.switch_scene=""
    def update(self,event):
        if fl.type_ev(event)=="ClicGauche":
            self.bouton.click()
    def draw(self):
        fl.image(largeur=fl.largeur_fenetre(),hauteur=fl.hauteur_fenetre(),x=0,y=0,fichier=self.path,ancrage="nw")
        self.bouton.draw()