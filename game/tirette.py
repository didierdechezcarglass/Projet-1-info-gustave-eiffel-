import random
def random_tirette():
    random_binary=[random.randint(2,8),random.randint(2,8)]
    return [random.randint(0,1) if (i not in random_binary and i not in (0,1)) else 0 for i in range(9)]

def decale(lst,sens):
    if sens=="left":
        for i in range(1,len(lst)):
            lst[i],lst[i-1]=lst[i-1],lst[i]
        return lst
    for i in range(len(lst)-1,1,-1):
        lst[i],lst[i-1]=lst[i-1],lst[i]
        #print(lst)
    return lst

class Tirette:
    def __init__(self,sens:bool,coordonnee:int):
        """
        classe représentant les tirettes du jeu
        celle ci permet de stocker les informations de la tirette, c'est à dire sa position, son
        sens et les positions des trous de la tirette
        la classe dispose également de méthodes permettant de manipuler dans les besoins du jeu
        la liste contenant les positions des trous, et enfin d'afficher la tirette
        """
        self.sens=sens
        self.coordonnee=coordonnee
        self.trous=random_tirette()
        self.position=0
    def decalage(self,sens):
        if sens=="left":
            stopper=0
            internal_incr=-1
        else:
            stopper=2
            internal_incr=1
        if self.position==stopper:
            return "cmon"
        else:
            self.trous=decale(self.trous,sens)
            self.position+=internal_incr
            return self.trous
    def affiche(self):
        """
        affichage des tirettes sur l'interface graphique
        """
        pass



"""a=[random_tirette() for loop in range(1000)]
for loop in a:
    print(loop)
    stock=loop
    print(decale(loop,"left"))
    print(decale(loop,"left"))
    print(decale(loop,"right"))
    print(decale(loop,"right"))
    print("\n")
    if stock!=loop:
        print("FAUX ERREUR")"""