from game import Grid
from game.tirette import Tirette

main_grid = Grid()
first_tirette = Tirette(2, "vert")


print(first_tirette.trous)
first_tirette.affect(main_grid)
print(main_grid)
first_tirette.decalage(1)
print()
first_tirette.affect(main_grid)
print(main_grid)
