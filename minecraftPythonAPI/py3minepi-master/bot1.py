import mcpi.minecraft as minecraft
from mineflayer import bot
# from time import sleep as time_sleep
# from random import randint as rnd_int


craft = minecraft.Minecraft.create()
cor = craft.player.getTilePos()

my_bot = bot.createBot(host='localhost', port= 61424, username='DTFBot')
my_bot.chat("Я родился :-)))")
