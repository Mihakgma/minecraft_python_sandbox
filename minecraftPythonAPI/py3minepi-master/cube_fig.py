from figure_parent_class import Figure
import mcpi.minecraft as minecraft
from time import sleep as time_sleep
from random import randint


class Cube(Figure):

    def __new__(cls, *args, **kwargs):
        super(Cube, cls).__new__(cls)
        return object.__new__(cls)

    def check_fig_dims(self, *args):
        if any([type(arg) != int or arg < 0 for arg in args]):
            print("all sides of figure must be natural integers!")
            raise ValueError
        if len(set(args)) > 1:
            print("for cube all sides must be equal!")
            raise ValueError


if __name__ == "__main__":
    test_draw_cube_dims = [
        (3, 2, 1),
        (3, 2, 1.0),
        ("", 1, -10),
        (-12, 3, 3),
        (5, 5, 5),
        (15, 15, 15),
        (3, 3, 3),
        (2, 2, 2),
        # (25, 25, 25),
        # (50, 50, 50),
        (5, 5, 5),
        (15, 15, 15),
        (3, 3, 3),
        (9, 9, 9),
        # (75, 75, 75),
    ]
    mc = minecraft.Minecraft.create()

    for cube_dims in test_draw_cube_dims:
        time_sleep(3)
        pos = mc.player.getTilePos()
        cube = Cube(pos.x+1,
                    pos.y,
                    pos.z+1,
                    randint(1, 111),
                    False,
                    mc)
        print(cube)
        try:
            cube.draw_filled_fig(*cube_dims)
        except ValueError as e:
            print(f"Error trying to build cube with dims: <{cube_dims}>")
            print(e)
    print("Totally have been created:")
    print(f"<{Cube.INSTANCES_CREATED}> figures (cubes)")
