from mcpi import minecraft
from mcpi.minecraft import Minecraft
from patterns.singleton import Singleton


class MinecraftWorld(Singleton):

    def __init__(self):
        mine_craft = minecraft.Minecraft.create()
        self.__mc_obj = mine_craft
        self.__mc_start_state = mine_craft.saveCheckpoint()

    def get_world(self):
        return self.__mc_obj

    def get_start_state(self):
        return self.__mc_start_state

    def restore_start_state(self):
        self.__mc_obj.restoreCheckpoint()

    def get_tile_pos(self):
        player = self.get_world().player  # Get the player object
        # print(type(player))
        if player is not None:
            pos = player.getTilePos()
            print(pos)
            return pos
        else:
            print("Error: Player not found.")
            return None


if __name__ == "__main__":
    print("testing work of singleton pattern...")
    mc = Minecraft.create()
    mc_obj_1 = MinecraftWorld()
    mc_obj_2 = MinecraftWorld()
    print(mc_obj_1 == mc_obj_2)
    print(mc_obj_1.get_world() == mc_obj_2.get_world())
