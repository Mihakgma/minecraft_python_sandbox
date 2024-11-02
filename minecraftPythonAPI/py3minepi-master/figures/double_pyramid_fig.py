# import mcpi.minecraft as minecraft
# from time import sleep as time_sleep
from figures.pyramid_fig import Pyramid
# from random import randint


class DoublePyramid(Pyramid):

    def draw_filled_fig(self, x_tiles, y_tiles, z_tiles):
        super().draw_filled_sand_clocks(x_tiles, y_tiles, z_tiles)
