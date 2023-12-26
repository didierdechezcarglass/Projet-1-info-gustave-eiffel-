from game import Grid, Ball
from game.tirette import Tirette
from . import fltk as fl
from .button import Button
import random

class Game:
    """
    Game scene class that manages the core mechanics

    attributes:
    grid : Grid() -> the empty grid
    tirette_vert : list -> list of vertical tirettes
    tirette_hor : list -> list of horizontal tirettes
    player_balls : dict -> dictionnary containning list of player balls
    current_player : int -> the current player number
    game_stopped : bool -> checks if the game is stopped
    winner : int | None -> the current winner
    colors : list -> the list of ball colors
    menu_button : Button -> the button to go back to the menu
    """
    def __init__(self, colors, player_number, menu_command, complementary : bool) -> None:
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
        self.alive_players = [(i + 1, colors[i]) for i in range(player_number)]
        if not complementary:
            self.cycles = 5
            self.init_nocompl(player_number)
        else:
            self.cycles = 0
        self.current_player = 0
        self.game_stopped = False
        self.colors = colors
        self.n_players = player_number
        self.complementary_phase = complementary
        grid_size_x = self.grid.horizontal_length + 2
        grid_size_y = self.grid.vertical_length + 2
        s_x = fl.largeur_fenetre() // grid_size_x
        s_y = fl.hauteur_fenetre() // grid_size_y
        self.menu_button = Button((0, 0), (s_x // 2, s_y // 2), ["<", "black", s_y // 2], "red", command=menu_command)

    def init_nocompl(self, n_player):
        """
        initializes the game when the complementary phase is not happening
        """
        tiles_avail = []
        for y in range(self.grid.vertical_length):
            for x in range(self.grid.vertical_length):
                if not all(self.grid.show_info(x, y)[1:3]):
                    tiles_avail.append((x, y))
        n_balls = 5 * n_player
        current_player = 0
        while n_balls > 0:
            coordinate = tiles_avail.pop(random.randint(0, len(tiles_avail) - 1))
            new_ball = Ball(current_player)
            self.grid.set_ball(*coordinate, new_ball)
            current_player += 1
            current_player %= n_player
            n_balls -= 1
    def check_players(self) -> list:
        """
        gives the number of players left after a move
        """
        alive_players = []
        for y in range(self.grid.vertical_length):
            for x in range(self.grid.horizontal_length):
                current_ball = self.grid.show_info(x, y)[0]
                bool_1 = current_ball is not None and current_ball.alive
                if bool_1 and current_ball.identity not in [tup[0] for tup in alive_players] :
                    alive_players.append((current_ball.identity, self.colors[current_ball.identity]))
        return sorted(alive_players, key=lambda p: p[0])


    def update_complementary(self, mouse_coordinates):
        grid_size_x = self.grid.horizontal_length + 2
        grid_size_y = self.grid.vertical_length + 2
        s_x = fl.largeur_fenetre() / grid_size_x
        s_y = fl.hauteur_fenetre() / grid_size_y
        coordinates = (int(mouse_coordinates[0] // s_x), int(mouse_coordinates[1] // s_y))
        if 1 <= coordinates[0] <= self.grid.horizontal_length + 1 and 1 <= coordinates[1] <= self.grid.vertical_length + 1:
            infos = self.grid.show_info(coordinates[0] - 1, coordinates[1] - 1)
            if infos[0] is not None or all(infos[1:3]):
                return
            else:
                self.grid.set_ball(coordinates[0] - 1, coordinates[1] - 1, Ball(self.current_player))
                self.current_player += 1
                if self.current_player >= self.n_players:
                    self.current_player = 0
                    self.cycles += 1
                if self.cycles >= 5:
                    self.complementary_phase = False
    def update_noncomplementary(self, mouse_coordinates):
        """
        updates the game when the complementary phase is over
        """
        grid_size_x = self.grid.horizontal_length + 2
        grid_size_y = self.grid.vertical_length + 2
        s_x = fl.largeur_fenetre() / grid_size_x
        s_y = fl.hauteur_fenetre() / grid_size_y
        coordinates = (int(mouse_coordinates[0] // s_x), int(mouse_coordinates[1] // s_y))
        coordinate_x = coordinates[0] / (grid_size_x - 1)
        coordinate_y = coordinates[1] / (grid_size_y - 1)
        if coordinate_x in (0, 1) and 0 < coordinate_y < 1:
            ls_ind = int(coordinates[1]) - 1
            holes = self.tirette_horizon[ls_ind].trous
            self.tirette_horizon[ls_ind].decalage(-1 if coordinate_x == 0 else 1)
            self.tirette_horizon[ls_ind].affect(self.grid)
            self.current_player += self.tirette_horizon[ls_ind].trous != holes
        if coordinate_y in (0, 1) and 0 < coordinate_x < 1:
            ls_ind = int(coordinates[0]) - 1
            holes = self.tirette_vert[ls_ind].trous
            self.tirette_vert[ls_ind].decalage(-1 if coordinate_y == 0 else 1)
            self.tirette_vert[ls_ind].affect(self.grid)
            self.current_player += self.tirette_vert[ls_ind].trous != holes
        self.alive_players = self.check_players()
        self.current_player = max(0, self.current_player % (len(self.alive_players)))
        self.game_stopped = len(self.alive_players) <= 1
    def update(self, event) -> None:
        """
        updates the scene
        """
        mouse_coordinates = (fl.abscisse_souris(), fl.ordonnee_souris())

        if fl.type_ev(event) == "ClicGauche" and not self.game_stopped:
            # updates the game when left click
            if self.complementary_phase:
                self.update_complementary(mouse_coordinates)
            else:
                self.update_noncomplementary(mouse_coordinates)



        self.menu_button.update(event, mouse_coordinates, {"Nombre Joueurs" : self.n_players, "Largeur Fenêtre" :  fl.largeur_fenetre(), "Hauteur Fenêtre" : fl.hauteur_fenetre(), "phase de placement": self.complementary_phase})



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
            for tile_x in range(self.grid.horizontal_length):
                tile = self.grid.show_info(tile_x, tile_y)
                fl.cercle(start_x + s_x / 2, start_y + s_y / 2, min(s_x / 4, s_y / 4), couleur="black", remplissage="black")
                if not tile[2]:
                    fl.rectangle(start_x, start_y + s_y / 4, start_x + s_x, start_y + (3 * s_y) / 4, couleur="red", remplissage="red")
                if not tile[1]:
                    fl.rectangle(start_x + s_x / 4, start_y, start_x + (3 * s_x) / 4, start_y + s_y, couleur="green", remplissage="green")
                if tile[0] is not None and tile[0].alive:
                    fl.cercle(start_x + s_x / 2, start_y + s_y / 2, min(s_x / 8, s_y / 8), couleur="black", remplissage=self.colors[tile[0].identity])
                start_x += s_x
            start_x = s_x
            start_y += s_y

        start_x = s_x
        start_y = s_y
        for point_x in range(1, self.grid.horizontal_length + 1):
            if self.tirette_vert[point_x - 1].position  > 0:
                fl.texte(start_x + s_x / 2, s_y / 2, chr(9650), "green", "center", taille=int(min(s_x / 4, s_y / 4)))
            if self.tirette_vert[point_x - 1].position < 2:
                fl.texte(start_x + s_x / 2, fl.hauteur_fenetre() - s_y / 2, chr(9660), "green", "center", taille=int(min(s_x / 4, s_y / 4)))
            if self.tirette_horizon[point_x - 1].position > 0:
                fl.texte(s_x / 2, start_y + s_y / 2, chr(9668), "red", "center", taille = int(min(s_x / 4, s_y / 4)))
            if self.tirette_horizon[point_x  - 1].position < 2:
                fl.texte(fl.largeur_fenetre() - s_x / 2, start_y + s_y / 2, chr(9658), "red", "center", taille=int(min(s_x / 4, s_y / 4)))
            start_x += s_x
            start_y += s_y

        if not self.game_stopped:
            size_x = fl.taille_texte(" a vous !", taille = 2 * int(min(s_x / 8, s_y / 8)))[0]
            player_color = self.alive_players[self.current_player][1]
            circ_rad = min(s_x / 8, s_y / 8)
            fl.cercle((fl.largeur_fenetre() // 2) - size_x / 2, circ_rad, circ_rad, couleur="black", remplissage=player_color)
            fl.texte(fl.largeur_fenetre() // 2, 0, "  a vous !",
                     couleur="black", taille=2 * int(circ_rad), ancrage="n")
        else:
            size_x = fl.taille_texte(" a gagné !", taille=2 * int(min(s_x / 8, s_y / 8)))[0]
            player_color = self.alive_players[self.current_player][1]
            circ_rad = min(s_x / 8, s_y / 8)
            if len(self.alive_players) == 1:
                fl.cercle((fl.largeur_fenetre() // 2) - size_x / 2, circ_rad, circ_rad, couleur="black",
                          remplissage=player_color)
                fl.texte(fl.largeur_fenetre() // 2, 0, "  a gagné !",
                         couleur="black", taille=2 * int(circ_rad), ancrage="n")
            else:
                fl.texte(fl.largeur_fenetre() // 2, 0, "match nul", couleur="black",
                     taille=2 * int(max(s_x / 8, s_y / 8)), ancrage="n")

        self.menu_button.draw()