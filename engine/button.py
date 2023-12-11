from engine import fltk as fl
def get_mouse_coo():
    return (fl.abscisse_souris,fl.ordonnee_souris)
class Button:
    def __init__(self,nw,width,height,text,color):
        self.origin=nw
        self.width=width
        self.height=height
        self.southeast=(nw[0]+width,nw[1]+height)
        self.text=text
        self.color=color
        self.tag=f"button{self.origin}"
        self.state=False
    def hover(self):
        if (self.origin[0]< fl.abscisse_souris < self.origin[0]+self.width)  and (self.origin[1]<fl.ordonnee_souris<self.origin[1]+self.height):
            return True
        return False
    def click(self):
        event=fl.donne_ev()
        if fl.typeeve(event)=='ClicGauche' and self.hover():
            print("clique!!")
    def draw(self):
        if not self.state:
            fl.rectangle(self.origin[0],self.origin[1],self.origin[0]+self.width,self.origin[1]+self.height,self.color,self.color,self.tag)
            fl.texte(self.origin[0]+(self.width/2), self.origin[1]+(self.height/2), self.text, couleur="green", taille=18, police='Courier',tag=self.text)

        else:
            fl.efface(self.tag)
            fl.efface(self.text)
            fl.rectangle(self.origin[0],self.origin[1],self.origin[0]+self.width,self.origin[1]+self.height,self.color,self.color,self.tag)
            fl.texte(self.origin[0]+(self.width/2), self.origin[1]+(self.height/2), self.text, couleur="green", taille=18, police='Courier',tag=self.text)
