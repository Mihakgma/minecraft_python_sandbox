import mcpi.minecraft as minecraft
from time import sleep as time_sleep
from random import randint as rnd_int

craft = minecraft.Minecraft.create()
cor = craft.player.getTilePos()
MIN_INT = -1000
MAX_INT = 1000

print(f"x = <{cor.x}>")
print(f"y = <{cor.y}>")
print(f"z = <{cor.z}>")
answer = ""
while answer != "x":
    cor = craft.player.getTilePos()
    craft.postToChat(f"x = <{cor.x}>, y = <{cor.y}>, z = <{cor.z}>")
    xr = rnd_int(MIN_INT, MAX_INT)
    zr = rnd_int(MIN_INT, MAX_INT)
    answer = input("для телепорта нажми Enter").lower().strip()
    craft.player.setTilePos(xr, cor.y, zr)
    time_sleep(3)