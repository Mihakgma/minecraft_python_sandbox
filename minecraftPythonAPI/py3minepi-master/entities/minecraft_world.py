# from mcpi import minecraft
from mcpi.minecraft import Minecraft
from patterns.singleton import Singleton


# class MinecraftWorld:
class MinecraftWorld(Singleton):

    def __init__(self):
        mine_craft = Minecraft.create()
        self.__mc_obj = mine_craft
        self.__mc_start_state = mine_craft.saveCheckpoint()

    def get_world(self):
        mine_craft = Minecraft.create()
        self.__mc_obj = mine_craft
        return mine_craft

    def get_start_state(self):
        mine_craft = Minecraft.create()
        self.__mc_obj = mine_craft
        return self.__mc_start_state

    def restore_start_state(self):
        print("trying to restore start state")
        mine_craft = Minecraft.create()
        self.__mc_obj = mine_craft
        mine_craft.restoreCheckpoint()

    def get_tile_pos(self):
        mine_craft = Minecraft.create()
        self.__mc_obj = mine_craft
        position = mine_craft.player.getTilePos()
        return position


if __name__ == "__main__":
    print("testing work of singleton pattern...")
    mc = Minecraft.create()
    mc_obj_1 = MinecraftWorld()
    mc_obj_2 = MinecraftWorld()

    pos = mc.player.getTilePos()
    print(pos)

    print(mc_obj_1 == mc_obj_2)
    print(mc_obj_1.get_world() == mc_obj_2.get_world() == mc)
