import mcpi.minecraft as minecraft
mc=minecraft.Minecraft.create()
pos=mc.player.getTilePos()

#Строительные блоки

base=49
mid=1
spire=112
window=20

#Устанавливаем координаты

x=pos.x+1
y=pos.y
z=pos.z+1

#База
mc.setBlocks(x,y,z,x+4,y+16,z+4,base)

#Середина
mc.setBlocks(x+1,y+16,z+1,x+3,y+19,z+3,mid)

#Шпиль
mc.setBlocks(x+2,y+19,z+2,x+2,y+21,z+2,spire)

#Окна
for i in range(4):
    mc.setBlocks(x+3,y+2,z+4,x+1,y+3,z,window)
    y=y+4