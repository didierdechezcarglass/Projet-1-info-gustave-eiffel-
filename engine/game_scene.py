from game import Grid, Ball
from game.tirette import Tirette
from . import fltk as fl
import random

COLOR = ["black", "yellow", "pink", "blue"]
class Game:
    def __init__(self):
        self.grid = Grid()
        tirette_vert = []
        tirette_horizon = []
        for loop in range(self.grid.vertical_length):
            tirette_vert.append(Tirette(loop, 'vert'))
            tirette_vert[-1].affect(self.grid)
        for loop in range(self.grid.horizontal_length):
            tirette_horizon.append(Tirette(loop, "hor"))
            tirette_horizon[-1].affect(self.grid)
        self.tirette_vert = tirette_vert
        self.tirette_horizon = tirette_horizon
        n_player = max(2, min(4, int(input("enter player number :"))))
        tiles_avail = []
        self.player_balls = {player : [] for player in range(n_player)}
        for y in range(self.grid.vertical_length):
            for x in range(self.grid.vertical_length):
                if not all(self.grid.show_info(x, y)[1:3]):
                    tiles_avail.append((x, y))
        n_balls = len(tiles_avail)
        current_player = 0
        while n_balls > 0:
            coordinate = tiles_avail.pop(random.randint(0, len(tiles_avail) - 1))
            new_ball = Ball(current_player)
            self.grid.set_ball(*coordinate, new_ball)
            self.player_balls[current_player].append(new_ball)
            current_player += 1
            current_player %= n_player
            n_balls -= 1
        self.current_player = 1
        self.game_stopped = False
        self.winner = None

    def update(self, event):
        grid_size_x = self.grid.horizontal_length + 2
        grid_size_y = self.grid.vertical_length + 2
        s_x = fl.largeur_fenetre() / grid_size_x
        s_y = fl.hauteur_fenetre() / grid_size_y
        if fl.type_ev(event) == "ClicGauche" and not self.game_stopped:
            coordinates = (int(fl.abscisse_souris() // s_x), int(fl.ordonnee_souris() // s_y))
            coordinate_x = coordinates[0] / (grid_size_x - 1)
            coordinate_y = coordinates[1] / (grid_size_y - 1)
            if (coordinate_x == 0 or coordinate_x == 1) and 0 < coordinate_y < 1:
                ls_ind = int(coordinates[1]) - 1
                self.tirette_horizon[ls_ind].decalage(-1 if coordinate_x == 0 else 1)
                self.tirette_horizon[ls_ind].affect(self.grid)
                self.current_player += 1
            if (coordinate_y == 0 or coordinate_y == 1) and 0 < coordinate_x < 1:
                ls_ind = int(coordinates[0]) - 1
                self.tirette_vert[ls_ind].decalage(-1 if coordinate_y == 0 else 1)
                self.tirette_vert[ls_ind].affect(self.grid)
                self.current_player += 1
            self.current_player = max(1, self.current_player % (len(self.player_balls) + 1))
            iterations = 0
            while len(self.player_balls[self.current_player - 1]) == 0 and iterations < 4:
                self.current_player += 1
                self.current_player = max(1, self.current_player % (len(self.player_balls) + 1))
                iterations += 1
            dead_player = 0
            possible_winner = None
            for player in self.player_balls:
                if not any([ball.alive for ball in self.player_balls[player]]):
                    self.player_balls[player].clear()
                    print(f"player {player} eliminated !")
                    dead_player += 1
                else:
                    possible_winner = player
            if dead_player >= len(self.player_balls) - 1:
                self.winner = possible_winner
                self.game_stopped = True



    def draw(self):
        """
        draws the game scene
        """
        grid_size_x = self.grid.horizontal_length + 2
        grid_size_y = self.grid.vertical_length + 2
        s_x = fl.largeur_fenetre() // grid_size_x
        s_y = fl.hauteur_fenetre() // grid_size_y
        start_x = s_x
        start_y = s_y
        for tile_y in range(self.grid.vertical_length):
            for tile_x in range(self.grid.vertical_length):
                tile = self.grid.show_info(tile_x, tile_y)
                fl.cercle(start_x + s_x / 2, start_y + s_y / 2, max(s_x / 4 , s_y / 4), couleur="black", remplissage="black")
                if not tile[2]:
                    fl.rectangle(start_x, start_y + s_y / 4, start_x + s_x, start_y + (3 * s_y) / 4, couleur="red", remplissage="red")
                if not tile[1]:
                    fl.rectangle(start_x + s_x / 4, start_y, start_x + (3 * s_x) / 4, start_y + s_y, couleur="green", remplissage="green")
                if tile[0] is not None and tile[0].alive:
                    fl.cercle(start_x + s_x / 2, start_y + s_y / 2, max(s_x / 8, s_y / 8), couleur= COLOR[tile[0].identity], remplissage= COLOR[tile[0].identity])
                start_x += s_x

                if start_x >= (grid_size_x - 1) * s_x:
                    start_x = s_x
                    start_y += s_y
        if not self.game_stopped:
            size_x = fl.taille_texte(" a vous !", taille = 2 * int(max(s_x / 8, s_y / 8)))[0]
            player_color = COLOR[self.player_balls[self.current_player - 1][0].identity]
            circ_rad = max(s_x / 8, s_y / 8)
            fl.cercle((fl.largeur_fenetre() // 2) - size_x / 2, circ_rad, circ_rad, couleur = player_color, remplissage = player_color)
            fl.texte(fl.largeur_fenetre() // 2, 0, "  a vous !",
                     couleur = "black", taille = 2 * int(circ_rad), ancrage = "n")
        else:
            text = f"le joueur {self.winner + 1} à gagné" if isinstance(self.winner, int) else "match nul!"
            fl.texte(fl.largeur_fenetre() // 2, 0, text, couleur="black",
                     taille=2 * int(max(s_x / 8, s_y / 8)), ancrage="n")