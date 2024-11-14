from mcpi.minecraft import Minecraft
from patterns.singleton import Singleton
from time import sleep as time_sleep


class MinecraftWorld(Singleton):
    __try_creates = 0

    def __new__(cls, *args, **kwargs):
        cls.__try_creates += 1
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, mcw=None):
        # first init of class instance is ALWAYS with pre-created minecraft world!!!
        # further tries if its init of this class may be without minecraft world
        if mcw is None:
            pass
        elif self.__try_creates == 1:
            self.__mc_obj = mcw
            self.__mc_start_state = mcw.saveCheckpoint()
        else:
            pass

    def get_world(self):
        """
        DONT USE THIS METHOD FOR GETTING CHAT!
        USE SPECIAL METHOD get_chat()!!!
        """
        return self.__mc_obj

    def get_start_state(self):
        return self.__mc_start_state

    def restore_start_state(self):
        print("trying to restore start state")
        mine_craft = self.__mc_obj
        mine_craft.restoreCheckpoint()

    def get_tile_pos(self):
        mine_craft = self.__mc_obj
        # print("Trying to get tile pos...")
        try:
            position = mine_craft.player.getTilePos()
            # print("Tile pos:", position)
            return position
        except Exception as e:
            print(f"Error getting tile pos: {e}")
            return None

    def get_chat(self):
        mine_craft = self.__mc_obj
        my_chat = mine_craft.events.pollChatPosts()
        return my_chat

    def get_tries_created(self):
        return self.__try_creates


if __name__ == "__main__":
    print("testing work of singleton pattern...")
    mc = Minecraft.create()
    mc_obj_1 = MinecraftWorld(mcw=mc)
    for i in range(1):
        time_sleep(3)
        chat = mc_obj_1.get_chat()
        for post in chat:
            print(post.message)
    mc_obj_2 = MinecraftWorld()
    print(mc_obj_2.get_tile_pos())
    print("done")
