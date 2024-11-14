import mcpi.minecraft as minecraft
from time import sleep as time_sleep
# from random import randint
import threading
import sys

from common_comands import commands, stop_commands
from datetime_current import get_current_time
from entities.minecraft_world import MinecraftWorld
from figures.cube_fig import Cube
from figures.double_pyramid_fig import DoublePyramid
from figures.pyramid_fig import Pyramid
from figures.rectangle_fig import Rectangle
from patterns.function_invoker import Invoker
# from patterns.singleton import Singleton
from tower_chatgpt_1 import SpiraledStairwayTower


class ChatListener(threading.Thread):
    __COMMANDS__ = commands
    __STOP_COMMANDS = stop_commands
    MAIN_DELIMITER = ":"
    SECONDARY_DELIMITER = ","

    def __init__(self, figure_classes: list,
                 mc: MinecraftWorld,
                 sleep_time: float = 3.5):
        threading.Thread.__init__(self)
        self.sleep_time = sleep_time
        self.mc = mc
        self.figure_classes = figure_classes

    def get_commands(self):
        return self.__COMMANDS__

    def run(self):
        # lock = threading.RLock()
        # players_ids = self.mc.getPlayerEntityIds()
        mess = ""
        while (mess.lower().strip() not in self.__STOP_COMMANDS
               and self.mc.get_world()):
            # with lock:
            # lock.acquire()
            time_sleep(self.sleep_time)  # check chat every ... seconds
            try:
                chat = self.mc.get_chat()
                if chat:
                    for post in chat:
                        print(post)
                        self.process_chat(post.message)
                        mess = post.message
            except AttributeError as e:
                print(e)
                # lock.release()
        else:
            print("Здесь мы будем приводить мир в исходное состояние!")

    def process_chat(self, message):
        chat_commands = self.get_commands()
        message = message.lower()
        print(message)
        class_not_found = True
        i = 0
        while class_not_found:
            figure_class = self.figure_classes[i]
            i += 1
            if len(self.figure_classes) == i:
                class_not_found = False
            obj_class_name = figure_class.__name__.lower()
            fig_name = message.split(self.MAIN_DELIMITER)[0].lower().strip()
            if obj_class_name == fig_name:
                print(f"class <{obj_class_name}> name is in message: {message}")
                if self.MAIN_DELIMITER not in message or self.SECONDARY_DELIMITER not in message:
                    error_message = (f"for <{obj_class_name}> message doesn't contain "
                                     f"any of delims: <{self.MAIN_DELIMITER}> | <{self.SECONDARY_DELIMITER}>")
                    print(error_message)
                    self.mc.get_world().postToChat(error_message)
                else:
                    print("trying to build a figure")
                    self.build_figure(figure_class, message)
                    class_not_found = False
            else:
                print(f"class <{obj_class_name}> name is NOT in message: {message}")
        else:
            for command, func in chat_commands.items():
                if command in message:
                    invoker = Invoker(self.mc, func)
                    invoker()

    def build_figure(self, figure_class, *args):
        pos = self.mc.get_tile_pos()
        print(figure_class)
        print(*args)
        message = args[0]
        vals_start_position = message.find(self.MAIN_DELIMITER)
        try:
            x_t, y_t, z_t, block_id = message[vals_start_position:].split(self.SECONDARY_DELIMITER)
        except ValueError as e:
            print(e)
            return
        x_t = x_t[1:]
        print(x_t, y_t, z_t, block_id)
        try:
            figure = figure_class(0, 0, 0, int(block_id), True)
            try:
                figure.draw_filled_fig(int(x_t), int(y_t), int(z_t))
            except ValueError as e:
                print(f"Error trying to build figure: {e}")
            except BaseException as be:
                print(f"Error trying to build figure: {be}")
                figure_1 = figure_class(pos.x, pos.y, pos.z,
                                        int(block_id), False)
                figure_1.draw_filled_fig(int(x_t), int(y_t), int(z_t))
        except TypeError as te:
            print(f"Error trying to init figures class new object: {te}")


if __name__ == "__main__":
    start_TS = get_current_time()
    # clear all previous events
    m_craft = minecraft.Minecraft.create()
    mc_1 = MinecraftWorld(m_craft)
    # cmde = minecraft.CmdEvents(connection=mc.getConnection())
    # cmde.clearAll()

    sys.setrecursionlimit(1000)

    # starting listener
    mcw = MinecraftWorld()
    figures_classes = [Cube,
                       Pyramid,
                       Rectangle,
                       DoublePyramid,
                       SpiraledStairwayTower]
    listener = ChatListener(figures_classes,
                            sleep_time=0.5,
                            mc=mcw)
    listener.start()

    # main cycle while listener working
    minutes_elapsed = 0
    minutes_to_finish = 60
    try:
        while (minutes_elapsed < minutes_to_finish
               and mcw.get_world()):
            time_sleep(60)
            mc = MinecraftWorld()
            print(f"Class MinecraftWorld instance have been created <{mc.get_tries_created()}> times already.")
            minutes_elapsed += 1
            print(f"Tik-tok, <{minutes_elapsed}> minutes elapsed...")
            print(f"<{minutes_to_finish - minutes_elapsed}> minutes to finish...")
    except KeyboardInterrupt:
        pass
    end_TS = get_current_time()
    print(f"started at: <{start_TS}>")
    print(f"ended at: <{end_TS}>")
