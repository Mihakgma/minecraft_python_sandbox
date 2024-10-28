from figure_parent_class import Figure
import mcpi.minecraft as minecraft


# from time import sleep as time_sleep
# from random import randint


class Rectangle(Figure):

    def __new__(cls, *args, **kwargs):
        super(Rectangle, cls).__new__(cls)
        return object.__new__(cls)

    def check_fig_dims(self, *args):
        if any([type(arg) != int or arg < 0 for arg in args]):
            print("all sides of figure must be natural integers!")
            raise ValueError
        if len(args) != 3:
            print("pyramid figure must have three dimensions!")
            raise ValueError
        if not any([arg == 1 for arg in args]):
            print("one dimension of pyramid figure must be equals to 1!")
            raise ValueError


if __name__ == "__main__":
    mc = minecraft.Minecraft.create()
    pos = mc.player.getTilePos()
    rectangle = Rectangle(pos.x + 1,
                          pos.y,
                          pos.z + 1,
                          11,
                          False,
                          mc)
    rectangle.draw_filled_fig(1, 2, 3)  # OK
    # pyramid.draw_filled_fig(0.5, 2, 3)  # ValueError
    # pyramid.draw_filled_fig(5, 2, 3)  # ValueError
