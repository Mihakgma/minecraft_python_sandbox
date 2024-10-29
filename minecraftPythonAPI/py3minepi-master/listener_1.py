import mcpi.minecraft as minecraft
from time import sleep as time_sleep
# from random import randint
import threading
import sys

from datetime_current import get_current_time
from cube_fig import Cube
from pyramid_fig import Pyramid


class ChatListener(threading.Thread):
    MAIN_DELIMITER = ":"
    SECONDARY_DELIMITER = ","

    def __init__(self, mc, figure_classes: list, sleep_time: float = 1.5):
        threading.Thread.__init__(self)
        self.sleep_time = sleep_time
        self.mc = mc
        self.figure_classes = figure_classes

    def run(self):
        players_ids = self.mc.getPlayerEntityIds()
        while True:
            time_sleep(self.sleep_time)  # Проверка чата каждую ...
            try:
                chat = self.mc.events.pollChatPosts()
                if chat:
                    for post in chat:
                        print(post)
                        self.process_chat(post.message)
            except AttributeError as e:
                print(e)

    def process_chat(self, message):
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
            if obj_class_name in message:
                print(f"class <{obj_class_name}> name is in message: {message}")
                if self.MAIN_DELIMITER not in message or self.SECONDARY_DELIMITER not in message:
                    error_message = (f"for <{obj_class_name}> message doesn't contain "
                                     f"any of delims: <{self.MAIN_DELIMITER}> | <{self.SECONDARY_DELIMITER}>")
                    print(error_message)
                    self.mc.postToChat(error_message)
                else:
                    print("trying to build a figure")
                    self.build_figure(figure_class, message)
                    class_not_found = False
            else:
                print(f"class <{obj_class_name}> name is NOT in message: {message}")

    def build_figure(self, figure_class, *args):
        # pos = self.mc.player.getTilePos()
        print(figure_class)
        print(*args)
        message = args[0]
        vals_start_position = message.find(self.MAIN_DELIMITER)
        x_t, y_t, z_t, block_id = message[vals_start_position:].split(self.SECONDARY_DELIMITER)
        x_t = x_t[1:]
        print(x_t, y_t, z_t, block_id)
        figure = figure_class(0, 0, 0, int(block_id), True, self.mc)
        try:
            figure.draw_filled_fig(int(x_t), int(y_t), int(z_t))
        except ValueError as e:
            print(f"Error trying to build figure: {e}")


if __name__ == "__main__":
    start_TS = get_current_time()
    # clear all previous events
    m_craft = minecraft.Minecraft.create()
    # cmde = minecraft.CmdEvents(connection=mc.getConnection())
    # cmde.clearAll()

    sys.setrecursionlimit(1000)

    # starting listener
    figures_classes = [Cube, Pyramid]
    listener = ChatListener(m_craft, figures_classes, sleep_time=1.5)
    listener.start()

    # main cycle while listener working
    minutes_elapsed = 0
    try:
        while True:
            time_sleep(60)
            minutes_elapsed += 1
            print(f"Tik-tok, <{minutes_elapsed}> minutes elapsed...")
    except KeyboardInterrupt:
        end_TS = get_current_time()
        print(f"started at: <{start_TS}>")
        print(f"ended at: <{end_TS}>")
