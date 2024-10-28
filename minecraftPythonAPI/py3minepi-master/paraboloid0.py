import mcpi.minecraft as minecraft
import mcpi.block as block
import math

craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

x = cor.x
y = cor.y
z = cor.z

#k=0.2
# очистка пространства

craft.setBlocks(x-50,y,z-50,x+50,y+50, z+50, 0)

a= b = 10

for k in range(20):
    y1=k
    
    r = a * math.sqrt(k)
    
    for j in range (360):
        x1 = 0.2*r*math.cos((math.pi *j)/180)
        z1 = 0.2*r*math.sin((math.pi *j)/180)
        
        craft.setBlock(x+x1,y+y1,z+z1, 246)    

    
         
         
