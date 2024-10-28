import mcpi.minecraft as minecraft
from time import sleep as time_sleep
# from random import randint as rnd_int

craft = minecraft.Minecraft.create()
cor = craft.player.getTilePos()

length = 5
y_up_by_step = 1
z_up_by_step = -1
stairway_iterations = 150
block_id = 20
block_id_up_by_step = 0
x, y, z = cor.x, cor.y, cor.z
current_block_id = block_id
block_id_upper_bounday = 100

for i in range(stairway_iterations):
    if current_block_id >= block_id_upper_bounday:
        current_block_id = block_id
    time_sleep(0.5)
    try:
        craft.setBlocks(x, y, z, x + length, y, z, current_block_id)
        y += y_up_by_step
        z += z_up_by_step
    except BaseException as e:
        print(f"Block with id = <{current_block_id}> doesnt exist")
        print(e)
    current_block_id += block_id_up_by_step
