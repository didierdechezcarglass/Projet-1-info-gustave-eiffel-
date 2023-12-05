from game import Grid, Ball
from game.tirette import Tirette
main_grid = Grid()

tirettes_list = []
for item in range(main_grid.vertical_length):
    tir = Tirette(item, "vert")
    tirettes_list.append(tir)
    tir.affect(main_grid)
for item in range(main_grid.vertical_length):
    tir = Tirette(item, "hor")
    tirettes_list.append(tir)
    tir.affect(main_grid)
tirettes_list[0].trous = [0] * 6 + [1]
tirettes_list[0].affect(main_grid)
tirettes_list[7].trous = [0] * 6 + [1]
tirettes_list[7].affect(main_grid)
main_grid.set_ball(0, 0, Ball(2))
print(main_grid)

tirettes_list[0].decalage(1)
tirettes_list[0].affect(main_grid)
tirettes_list[7].decalage(1)
tirettes_list[7].affect(main_grid)

print(main_grid)