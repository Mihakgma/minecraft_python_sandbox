import mcpi.minecraft as minecraft
# import mcpi.block as block

import random


craft = minecraft.Minecraft.create()

cor = craft.player.getTilePos()
# cor = craft.player.getPos()
print(cor.x)
x = cor.x + 2
y = cor.y
z = cor.z

def snow_golem(x, z):
    craft.setBlocks(x, y, z, x, y+1, z, 80)
    craft.setBlocks(x, y+2, z, 103)

for i in range(20):
    snow_golem(x, z)
    x = x + random.randint(-10, 10)
    z = z + random.randint(-10, 10)
