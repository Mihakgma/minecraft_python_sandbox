from figure_parent_class import Figure
import mcpi.minecraft as minecraft

from time import sleep as time_sleep


# from random import randint


class Pyramid(Figure):

    def __new__(cls, *args, **kwargs):
        super(Pyramid, cls).__new__(cls)
        return object.__new__(cls)

    def check_fig_dims(self, *args):
        super(Pyramid, self).check_fig_dims(*args)
        if len(args) != 3:
            print("pyramid figure must have three dimensions!")
            raise ValueError

    def draw_filled_fig(self, x_tiles, y_tiles, z_tiles):
        self.check_fig_dims(x_tiles, y_tiles, z_tiles)
        craft = self.get_minecraft_world_entity()
        block_id = self.get_block_id()
        x, y, z = self.get_x(), self.get_y(), self.get_z()
        # print(f"\nGonna draw a FILLED <{self.class.name}> with:")
        print(f"tiles on x axis = <{x_tiles}>")
        print(f"tiles on y axis = <{y_tiles}>")
        print(f"tiles on z axis = <{z_tiles}>")

        # Calculate steps for each layer
        x_step = x_tiles // (y_tiles - 1)
        z_step = z_tiles // (y_tiles - 1)

        # Iterate over layers
        for y_up in range(y_tiles):
            # Calculate current dimensions for the layer
            current_x_tiles = x_tiles - x_step * y_up
            current_z_tiles = z_tiles - z_step * y_up
            # print(f"{current_x_tiles} tiles on y axis = <{y_up}>")
            # print(f"{current_z_tiles} tiles on z axis = <{y_up}>")

            x_size = abs((x + x_step * y_up) - (x + current_x_tiles))
            z_size = abs((z + z_step * y_up) - (z + current_z_tiles))
            # print(f"x_size = <{x_size}>")

            # Set blocks for the current layer
            craft.setBlocks(
                x + x_step * y_up,
                y + y_up,
                z + z_step * y_up,
                x + current_x_tiles,
                y + y_up,
                z + current_z_tiles,
                block_id,
            )
            # Adjust dimensions for the next layer
            # Preventing building sand clocks (duplicated pyramid)
            if x_size <= 1 or z_size <= 1:
                break

    def draw_filled_sand_clocks(self, x_tiles, y_tiles, z_tiles):
        self.check_fig_dims(x_tiles, y_tiles, z_tiles)
        craft = self.get_minecraft_world_entity()
        block_id = self.get_block_id()
        x, y, z = self.get_x(), self.get_y(), self.get_z()
        # print(f"\nGonna draw a FILLED <{self.class.name}> with:")
        print(f"tiles on x axis = <{x_tiles}>")
        print(f"tiles on y axis = <{y_tiles}>")
        print(f"tiles on z axis = <{z_tiles}>")

        # Calculate steps for each layer
        x_step = x_tiles // (y_tiles - 1)
        z_step = z_tiles // (y_tiles - 1)

        # Iterate over layers
        for y_up in range(y_tiles):
            # Calculate current dimensions for the layer
            current_x_tiles = x_tiles - x_step * y_up
            current_z_tiles = z_tiles - z_step * y_up

            # Set blocks for the current layer
            craft.setBlocks(
                x + x_step * y_up,
                y + y_up,
                z + z_step * y_up,
                x + current_x_tiles,
                y + y_up,
                z + current_z_tiles,
                block_id,
            )


if __name__ == "__main__":
    mc = minecraft.Minecraft.create()
    pos = mc.player.getTilePos()
    pyramid = Pyramid(pos.x + 1,
                      pos.y,
                      pos.z + 1,
                      19,
                      False,
                      mc)
    time_sleep(3.5)
    pyramid.draw_filled_fig(120, 120, 120)  # OK
    time_sleep(3.5)
    # pyramid.draw_filled_sand_clocks(30, 30, 50)
    