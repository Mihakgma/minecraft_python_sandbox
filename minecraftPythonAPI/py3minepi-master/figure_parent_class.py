import mcpi.minecraft as minecraft


class Figure:
    INSTANCES_CREATED = 0
    """
    Absract parent class for creating
    different figures in minecraft game.
    """

    def __new__(cls, *args, **kwargs):
        cls.INSTANCES_CREATED += 1
        return

    def __init__(self,
                 x: int,
                 y: int,
                 z: int,
                 block_id: int,
                 position: bool,
                 minecraft_world_entity):
        self.__x = x
        self.__y = y
        self.__z = z
        self.__block_id = block_id
        self.__position = position
        self.__minecraft_world_entity = minecraft_world_entity
        if position:
            self.__set_coords_from_position()

    def set_x(self, x):
        if Figure.is_int_digit(x):
            self.__x = x

    def get_x(self):
        return self.__x

    def set_y(self, y):
        if Figure.is_int_digit(y):
            self.__y = y

    def get_y(self):
        return self.__y

    def set_z(self, z):
        if Figure.is_int_digit(z):
            self.__z = z

    def get_z(self):
        return self.__z

    def set_block_id(self, block_id):
        if Figure.is_int_digit(block_id):
            self.__block_id = block_id

    def get_block_id(self):
        return self.__block_id

    def get_minecraft_world_entity(self):
        return self.__minecraft_world_entity

    def __set_coords_from_position(self):
        position = self.get_minecraft_world_entity().player.getTilePos()
        self.set_x(position.x)
        self.set_y(position.y)
        self.set_z(position.z)

    def draw_filled_fig(self, x_tiles, y_tiles, z_tiles):
        self.check_fig_dims(x_tiles, y_tiles, z_tiles)
        craft = self.get_minecraft_world_entity()
        block_id = self.get_block_id()
        x, y, z = self.get_x(), self.get_y(), self.get_z()
        print(f"\nGonna draw a FILLED <{self.__class__.__name__}> with:")
        print(f"tiles on x axis = <{x_tiles}>")
        print(f"tiles on y axis = <{y_tiles}>")
        print(f"tiles on z axis = <{z_tiles}>")
        craft.setBlocks(x, y, z,
                        x + x_tiles - 1,
                        y + y_tiles - 1,
                        z + z_tiles - 1,
                        block_id)

    def check_fig_dims(self, *args):
        if any([type(arg) != int or arg < 0 for arg in args]):
            print("all sides of figure must be natural integers!")
            raise ValueError

    @staticmethod
    def is_int_digit(digit):
        return type(digit) == int or type(digit) == float

    def __str__(self):
        return ("fig type: " + self.__class__.__name__ +
                "\nx: " + str(self.get_x()) +
                "\ny: " + str(self.get_y()) +
                "\nz: " + str(self.get_z()) +
                "\nblock type: " + str(self.get_block_id()))


if __name__ == "__main__":
    mc = minecraft.Minecraft.create()
    figure = Figure(1, 2, 3, 9, False, mc)
    print(figure)
