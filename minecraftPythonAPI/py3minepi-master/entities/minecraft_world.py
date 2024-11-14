from mcpi.minecraft import Minecraft
from patterns.singleton import Singleton
from time import sleep as time_sleep


class MinecraftWorld(Singleton):

    def __init__(self, mcw=None):
        # first init of class instance is ALWAYS with created minecraft world!!!
        if mcw is None:
            pass
        else:
            self.__mc_obj = mcw
            self.__mc_start_state = mcw.saveCheckpoint()

    def get_world(self):
        # self.remake_world()
        world = self.__mc_obj
        print(world)
        return world

    def get_start_state(self):
        # self.remake_world()
        return self.__mc_start_state

    def restore_start_state(self):
        print("trying to restore start state")
        mine_craft = self.__mc_obj
        mine_craft.restoreCheckpoint()

    def get_tile_pos(self):
        # self.remake_world()
        mine_craft = self.__mc_obj
        print("Trying to get tile pos...")
        try:
            position = mine_craft.player.getTilePos()
            print("Tile pos:", position)
            return position
        except Exception as e:
            print(f"Error getting tile pos: {e}")
            return None

    def remake_world(self):
        new_mcw = Minecraft.create()
        self.__mc_obj = new_mcw

    def get_chat(self):
        mine_craft = self.__mc_obj
        my_chat = mine_craft.events.pollChatPosts()
        return my_chat


if __name__ == "__main__":
    print("testing work of singleton pattern...")
    mc = Minecraft.create()
    mc_obj_1 = MinecraftWorld(mcw=mc)
    # mc_new = mc_obj_1.get_world()

    # pos = mc_new.player.getTilePos()
    # pos = mc.player.getTilePos()
    # print(pos)
    for i in range(10):
        time_sleep(3)
        chat = mc_obj_1.get_chat()
        for post in chat:
            print(post.message)
