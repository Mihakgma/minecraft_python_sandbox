# import mcpi.minecraft as minecraft
# from time import sleep as time_sleep
from figures.pyramid_fig import Pyramid
# from random import randint


class DoublePyramid(Pyramid):
    def __new__(cls, *args, **kwargs):
        super(Pyramid, cls).__new__(cls)
        return object.__new__(cls)

    def draw_filled_fig(self, x_tiles, y_tiles, z_tiles):
        super().draw_filled_sand_clocks(x_tiles, y_tiles, z_tiles)
