from . import fltk as fl
def get_mouse_coo():
    return (fl.abscisse_souris,fl.ordonnee_souris)
class Button:
    def __init__(self,nw,width,height,text,color="green",image=False,picker="color"):
        """
        nw : (x,y), x and y are coordinates of """
        self.origin=nw
        self.width=width
        self.height=height
        self.southeast=(nw[0]+width,nw[1]+height)
        self.text=text
        if picker!="image" or type(image)!=str:
            self.picker="color"
        else:
            self.picker=picker
        self.color=color
        self.tag=f"button{self.origin}"
        self.image=image
        self.state=False
    def hover(self):
        return (self.origin[0]< fl.abscisse_souris() < self.origin[0]+self.width)  and (self.origin[1]<fl.ordonnee_souris()<self.origin[1]+self.height)
    def click(self):
        if self.hover():
            print("clique!!")
    def draw_image(self):
        if not self.state:
            fl.image(largeur=self.width,hauteur=self.height,x=self.origin[0],y=self.origin[1],fichier=self.image,ancrage="nw",tag=self.tag)
            fl.texte(self.origin[0]+(self.width/2), self.origin[1]+(self.height/2), self.text, couleur="green", taille=9,tag=self.text,ancrage="center")
            self.state=True
        else:
            fl.efface(self.tag)
            fl.efface(self.text)
            fl.image(largeur=self.width,hauteur=self.height,x=self.origin[0],y=self.origin[1],fichier=self.image,ancrage="nw",tag=self.tag)
            fl.texte(self.origin[0]+(self.width/2), self.origin[1]+(self.height/2), self.text, couleur="green", taille=9,tag=self.text,ancrage="center")

    def draw_without_image(self):
        if not self.state:
            fl.rectangle(self.origin[0],self.origin[1],self.southeast[0],self.southeast[1],tag=self.tag,remplissage=self.color)
            fl.texte(self.origin[0]+(self.width/2), self.origin[1]+(self.height/2), self.text, couleur="green", taille=9,tag=self.text,ancrage="center")
            self.state=True
        else:
            fl.efface(self.tag)
            fl.efface(self.text)
            fl.rectangle(self.origin[0],self.origin[1],self.southeast[0],self.southeast[1],tag=self.tag,remplissage=self.color)
            fl.texte(self.origin[0]+(self.width/2), self.origin[1]+(self.height/2), self.text, couleur="green", taille=9,tag=self.text,ancrage="center")
    def draw(self):
        if self.picker=="image":
            self.draw_image()
        else:
            self.draw_without_image()