import pygame

screenWidth=1024
screenHeight=768

SCREEN=pygame.display.set_mode((screenWidth,screenHeight),0,32)


start=0
height=768
end=start+height

(rStart,gStart,bStart)=(128,0,128)
(rEnd,gEnd,bEnd)=(0,128,255)
(rDelta,gDelta,bDelta)=(float(rStart-rEnd)/height,float(gStart-gEnd)/height,float(bStart-bEnd)/height)

SCREEN.fill(endCol)

for n in range (start,end):
    red=int(rStart-(rDelta*(n+1)))
    green=int(gStart-(gDelta*(n+1)))
    blue=int(bStart-(bDelta*(n+1)))  
    pygame.draw.line(SCREEN,(red,green,blue), (0,n),(screenWidth,n))


pygame.display.update()
