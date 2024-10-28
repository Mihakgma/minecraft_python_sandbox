from numpy.random import randint

from cube_fig import Cube
# from figure_parent_class import Figure
import mcpi.minecraft as minecraft

from time import sleep as time_sleep

from pyramid_fig import Pyramid

if __name__ == "__main__":
    mc = minecraft.Minecraft.create()
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z

    pyramid = Pyramid(x + 1,
                      y+10,
                      z + 1,
                      19,
                      False,
                      mc)

    cube = Cube(x + 1,
                y,
                z + 1,
                17,
                False,
                mc)

    print(cube)
    time_sleep(3.5)
    cube.draw_filled_fig(10,10,10)
    pyramid.draw_filled_fig(10, 10, 10)  # OK
