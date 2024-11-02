from mcpi.minecraft import Minecraft
from patterns.singleton import Singleton


class MinecraftWorld(Singleton):

    def __init__(self, mc_obj: Minecraft):
        self.__mc_obj = mc_obj
        self.__mc_start_state = mc_obj.saveCheckpoint()

    def get_world(self):
        return self.__mc_obj

    def get_start_state(self):
        return self.__mc_start_state

    def restore_start_state(self):
        self.__mc_obj.restoreCheckpoint()


if __name__ == "__main__":
    mc = Minecraft.create()
    mc_obj_1 = MinecraftWorld(mc)
    mc_obj_2 = MinecraftWorld(mc)
    print(mc_obj_1 == mc_obj_2)
