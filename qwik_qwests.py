# Weekend Game - Qwik Qwests   

import pygame, sys, pickle, numpy as np
import time
from blocks import *
from pygame.locals import *
from common import getmax
from random import shuffle

pygame.init()

FPS=30
fpsClock = pygame.time.Clock()






pygame.display.set_caption('Qwik Qwests')

listFH=open('levellist.pkl','rb')
levelList=pickle.load(listFH)
listFH.close()

level=0
#playerInv=np.zeros(10,dtype=np.int)

def load_level(p):
    i='levels\\' + p
    FH=open(i,'rb') # add error if doesn't exist
    Block.instances=pickle.load(FH)
    Object.instances=pickle.load(FH)
    SpawnPoint.instances=pickle.load(FH)
##    l=pickle.load(FH)
##    s=pickle.load(FH)
##    o=pickle.load(FH)
    FH.close()
    #playerInv=np.zeros(10,dtype=np.int)
    #return(l,s,o)
    
#(testLevel,spawn,objective)=load_level(levelList[level][2])
load_level(levelList[level][2])

spawns=[]
for s in SpawnPoint.instances.values():
    spawns.append(s.pos)
shuffle(spawns)
      
P1=Character(spawns[0],'Inky')
P1.setidx(1)
P1.setblock(BOY)
#P1.setpos(0,0,1)
P1.setkeys(K_UP,K_DOWN,K_LEFT,K_RIGHT,K_RCTRL)
P1.initinv()
#P1.speak('hello',5)

P2=Character(spawns[1],'Stinky')
P2.setidx(2)
P2.setblock(CATGIRL)
#P2.setpos(10,10,1)
P2.setkeys(K_w,K_s,K_a,K_d,K_LCTRL)
P2.initinv()
#P2.speak('bonjour',5)

P3=Character(spawns[2],'Winky')
P3.setidx(3)
P3.setblock(HORNGIRL)
#P3.setpos(10,0,1)
P3.setkeys(K_i,K_k,K_j,K_l,K_SPACE)
P3.initinv()
#P3.speak('hola',5)

P4=Character(spawns[3],'Pinky')
P4.setidx(4)
P4.setblock(PINKGIRL)
#P4.setpos(0,10,1)
P4.setkeys(K_KP8,K_KP2,K_KP4,K_KP6,K_KP_ENTER)
P4.initinv()
#P4.speak('guten tag',5)

#print("These are the characters ")
#for instance in Character.instances:
#    print(instance.name)

def nearObject(player,object):
    # return List of objects/players in the 8 squares
    return True
                 

##P5=Character()
##P5.setidx(5)
##P5.setname('Pinky')
##P5.setimage(PINKGIRL)
##P5.setpos(2,6,1)
##P5.setkeys(K_KP8,K_KP2,K_KP4,K_KP6,K_KP_ENTER)
##P5.initinv()

players=[P1,P2,P3,P4]


def renderPanel():
    SCREEN.blit(levelText,(1050,100))
    SCREEN.blit(number[level+1],(1100,150))


BLACK = (0,0,0)
WHITE = (255,255,255)
LIGHTBLUE = (100,150,255)
BROWN = (150,100,50)
ORANGE = (255,140,0)

titleCenter = QwikQwests.get_rect()
titleCenter.center=((screenWidth/2),50)
bubbleFont=pygame.font.Font('fonts/36daysag.ttf',16)
bubbleText=bubbleFont.render('Hello World!',1,BLACK)

testLevel=[None]*6

blockWidth=50
blockHeight=40      

limit_y=11
limit_x=19

blockOffset=20

spawn=[0,0,0]
objective=[9,5,5]



##for player in players:
##    (player.x,player.y,player.z) = (spawn[player.idx-1][0],spawn[player.idx-1][1],spawn[player.idx-1][2])

min_x=0
min_y=0
min_z=0

##max_x=len(testLevel[0][0])
##max_y=len(testLevel[0])
##max_z=len(testLevel)
##max_x -= 1
##max_y -= 1
##max_z -= 1

(max_x,max_y,max_z)=getmax(Block.instances,(0,0,0))
(max_x,max_y,max_z)=getmax(Object.instances,(max_x,max_y,max_z))
(max_x,max_y,max_z)=getmax(Character.instances,(max_x,max_y,max_z))
                    
screenOffsetX=0 + ((limit_x - max_x) / 2 * blockWidth)
screenOffsetY=274 + ((limit_y - max_y) / 2 * blockHeight)

playerObj=1

indexInv=0

def draw_inventory():
    invOffset=120
    for player in players:
        for i in range (1,11):
            blockId=player.inventory[i-1]
            SCREEN.blit(blockType[blockId], (950+(50*player.idx),((i*(20+blockHeight))+invOffset)))

def object_right(x,y,z):
    if ((x < max_x) and (HEART >= testLevel[z][y][x+1] >= GEMBLUE)):
        return True
    
def object_left(x,y,z):
    if ((x > min_x) and (HEART >= testLevel[z][y][x-1] >= GEMBLUE)):
        return True

def object_down(x,y,z):
    if ((y < max_y) and (HEART >= testLevel[z][y+1][x] >= GEMBLUE)):
        return True
    
def object_up(x,y,z):
    if ((y > min_y) and (HEART >= testLevel[z][y-1][x] >= GEMBLUE)):
        return True

def draw_screen():

    start=0
    height=375
    end=start+height

    (rStart,gStart,bStart)=LIGHTBLUE
    (rEnd,gEnd,bEnd)=ORANGE
    (rDelta,gDelta,bDelta)=(float(rStart-rEnd)/height,float(gStart-gEnd)/height,float(bStart-bEnd)/height)

    SCREEN.fill(ORANGE)

    
    for n in range (start,end):
        red=int(rStart-(rDelta*(n+1)))
        green=int(gStart-(gDelta*(n+1)))
        blue=int(bStart-(bDelta*(n+1)))  
        pygame.draw.line(SCREEN,(red,green,blue), (0,n),(screenWidth,n))

    SCREEN.blit(QwikQwests, titleCenter)
    renderPanel()

    renderDict=Block.instances.copy()
    renderDict.update(Object.instances)
    renderDict.update(Character.instances)
    
    for j in sorted(iter(renderDict.keys())):
        b=renderDict[j]
        (x,y,z)=b.pos
        offset=(z*-1*blockOffset)+screenOffsetY
        # Block
        SCREEN.blit(blockType[b.blocknum], ((x*blockWidth),(y*blockHeight+(offset))))
  
##    for z in range (0,(max_z+1)):
##        offset=(z*-1*blockOffset)+screenOffsetY
##        for y in range (0,(max_y+1)):
##            for x in range (0,(max_x+1)):
##                block=testLevel[z][y][x]
##                
##                tallBlockOffset=0
##                if (block == DOORTALLC):
##                    tallBlockoffset=2*blockOffset
##
##                if block > 0:
##                    image=blockType[block]
##                    SCREEN.blit(image, ((x*blockWidth+screenOffsetX),(y*blockHeight+(offset))))
##                
##                # shadow processing
##                if (z < max_z) and (testLevel[z+1][y][x] == EMPTY or (TREEUGLY < testLevel[z+1][y][x] < CHESTC)) and (RAMP_W < block < ROCK):
##                    # South East
##                    if (z < max_z) and (y < max_y) and (x < max_x) and (RAMP_W < testLevel[z+1][y+1][x+1] < ROCK) and (testLevel[z+1][y][x+1] == EMPTY) and (testLevel[z+1][y+1][x] == EMPTY):
##                       SCREEN.blit(shadowType[SHADOW_SE], ((x*blockWidth+screenOffsetX),(y*blockHeight+(offset))))
##                       #print("Placing SE shadow at {0},{1},{2}".format(x,y,z))
##                    # South - needs check to see if we're the top block - purely a waste of cycles - nothing cosmetic AFAIK
##                    if (z < max_z) and (y < max_y) and (RAMP_W < testLevel[z+1][y+1][x] < ROCK):
##                       SCREEN.blit(shadowType[SHADOW_S], ((x*blockWidth+screenOffsetX),(y*blockHeight+(offset))))
##                    # South West
##                    if (z < max_z) and (y < max_y) and (x > min_x) and (RAMP_W < testLevel[z+1][y+1][x-1] < ROCK) and (testLevel[z+1][y][x-1] == EMPTY) and (testLevel[z+1][y+1][x] == EMPTY):
##                       SCREEN.blit(shadowType[SHADOW_SW], ((x*blockWidth+screenOffsetX),(y*blockHeight+(offset))))
##                    # East
##                    if (z < max_z) and (x < max_x) and (RAMP_W < testLevel[z+1][y][x+1] < ROCK):
##                       SCREEN.blit(shadowType[SHADOW_E], ((x*blockWidth+screenOffsetX),(y*blockHeight+(offset))))
##                    # West
##                    if (z < max_z) and (x > min_x) and (RAMP_W < testLevel[z+1][y][x-1] < ROCK):
##                       SCREEN.blit(shadowType[SHADOW_W], ((x*blockWidth+screenOffsetX),(y*blockHeight+(offset))))
##                    # North East
##                    if (z < max_z) and (y > min_y) and (x < max_x) and (RAMP_W < testLevel[z+1][y-1][x+1] < ROCK) and (testLevel[z+1][y][x+1] == EMPTY) and (testLevel[z+1][y-1][x] == EMPTY):
##                       SCREEN.blit(shadowType[SHADOW_NE], ((x*blockWidth+screenOffsetX),(y*blockHeight+(offset))))
##                    # North
##                    if (z < max_z) and (y > min_y) and (RAMP_W < testLevel[z+1][y-1][x] < ROCK):
##                       SCREEN.blit(shadowType[SHADOW_N], ((x*blockWidth+screenOffsetX),(y*blockHeight+(offset))))
##                    # North West
##                    if (z < max_z) and (y > min_y) and (x > min_x) and (RAMP_W < testLevel[z+1][y-1][x-1] < ROCK) and (testLevel[z+1][y][x-1] == EMPTY) and (testLevel[z+1][y-1][x] == EMPTY):
##                       SCREEN.blit(shadowType[SHADOW_NW], ((x*blockWidth+screenOffsetX),(y*blockHeight+(offset))))
##                    # Side West
##                    if (z < max_z) and (x > min_x) and (y < max_y) and (RAMP_W < testLevel[z][y+1][x-1] < ROCK) and (testLevel[z][y+1][x] == EMPTY) and (testLevel[z+1][y+1][x] == EMPTY):
##                       SCREEN.blit(shadowType[SHADOW_SIDEW], ((x*blockWidth+screenOffsetX),(y*blockHeight+(offset))))
##                    # South (top)
##                    if (z < y + 3 )and (z < max_z) and (y > min_y) and (testLevel[z+1][y][x] == EMPTY) and (testLevel[z][y-1][x] == EMPTY) and (testLevel[z+1][y-1][x] == EMPTY):
##                       SCREEN.blit(shadowType[SHADOW_S], ((x*blockWidth+screenOffsetX),(y*blockHeight+(offset)-blockOffset-tallBlockOffset)))
##
##                for player in players:
##                    if (player.x,player.y,player.z) == (x,y,z):
##                        ramp = 0
##                        below=testLevel[z-1][y][x]
##                        if (below == RAMP_N) or (below == RAMP_S) or (below == RAMP_E) or (below == RAMP_W):
##                            ramp = 10
##                        SCREEN.blit(objectType[player.blocknum],((x*blockWidth+screenOffsetX),y*blockHeight+offset+ramp))
##                        if (player.speaking == True):
##                            if (time.mktime(time.gmtime()) > (player.sayage + player.saysecs)):
##                                player.say=''
##                                player.sayage=0
##                                player.saysecs=0
##                                player.speaking = False
##                            else:
##                                bubbleText=bubbleFont.render(player.say,1,BLACK)
##                                SCREEN.blit(bubble,((x*blockWidth+screenOffsetX+35),y*blockHeight+offset+ramp-30))
##                                SCREEN.blit(bubbleText,((x*blockWidth+screenOffsetX+45),y*blockHeight+offset+ramp+15))
##                    
####                if (z == objective[2] ) and (y == objective[1]) and (x == objective[0]):
####                    SCREEN.blit(objectType[STAR], ((x*blockWidth+screenOffsetX),y*blockHeight+offset))

    draw_inventory()


def canMoveRight(px,py,pz):
    if (px < max_x):
        if ((testLevel[pz][py][px + 1] == EMPTY) or (HEART >= testLevel[pz][py][px+1] >= GEMBLUE)) and (testLevel[pz-1][py][px+1] < WATERBLOCK):
            if (testLevel[pz-1][py][px+1] == EMPTY):
                if (testLevel[pz-1][py][px] == RAMP_E):  
                    return True
                return False
            return True
        if (testLevel[pz][py][px+1] == RAMP_W):
            return True
        return False
    return False

def canMoveLeft(px,py,pz):
    if (px > min_x):
        if ((testLevel[pz][py][px-1] == EMPTY) or (HEART >= testLevel[pz][py][px-1] >= GEMBLUE)) and (testLevel[pz-1][py][px-1] < WATERBLOCK):
            if (testLevel[pz-1][py][px-1] == EMPTY):
                if (testLevel[pz-1][py][px] == RAMP_W):  
                    return True
                return False
            return True
        if (testLevel[pz][py][px-1] == RAMP_E):
            return True
        return False
    return False

def canMoveUp(px,py,pz):
    if (py > min_y):
        if ((testLevel[pz][py-1][px] == EMPTY) or (HEART >= testLevel[pz][py-1][px] >= GEMBLUE)) and (testLevel[pz-1][py-1][px] < WATERBLOCK):
            if (testLevel[pz-1][py-1][px] == EMPTY):
                if (testLevel[pz-1][py][px] == RAMP_N):  
                    return True
                return False
            return True
        if (testLevel[pz][py-1][px] == RAMP_S):
            return True
        return False
    return False

def canMoveDown(px,py,pz):
    if (py < max_y):
        if ((testLevel[pz][py+1][px] == EMPTY) or (HEART >= testLevel[pz][py+1][px] >= GEMBLUE)) and (testLevel[pz-1][py+1][px] < WATERBLOCK):
            if (testLevel[pz-1][py+1][px] == EMPTY):
                if (testLevel[pz-1][py][px] == RAMP_S):  
                    return True
                return False
            return True
        if (testLevel[pz][py+1][px] == RAMP_N):
            return True
        return False
    return False


def changeLevel(direction):
    if(direction == "next"):
        return True
       
def collision(dx,dy,dz):
    collide=False
    
    for others in players:
        if player.x+dx == others.x and player.y+dy == others.y and player.z+dz == others.z:
            collide = True
    return collide

def outofbounds(oob):
    (z,y,x)=oob
    if ( min_x <= x <= max_x ) and ( min_y <= y <= max_y ) and ( min_z <= z <= max_z ):
        print("somewhere else")
        return False
    print("out of bounds {0}".format(oob))
    return True

def canmoveto(pos):
    # Edges
    
    # Players
    print("checking: {0}".format(pos))
    # at the edge
    if outofbounds(pos):
        return False
    elif (Character.instances.get(pos) != None):
        # another player
        print("found a character")
        return False
    elif (Object.instances.get(pos) != None):
        # next to an object
        print("found an object")
        return False
    elif (Block.instances.get(pos) != None):
        # next to a block
        print("found a block")
        return False
    else:
        # empty space
        # however must be above space or water
        (bz,by,bx)=pos
        below=(bz-1,by,bx)
        underblock=Block.instances.get(below)
        # we're not The Snowman or Jesus
        if (underblock == None or underblock.blocknum == WATERBLOCK):
            print("can't fly or walk on water {0}".format(underblock))
            return False
            
    return True

draw_screen()
                
while True:
    fpsClock.tick(FPS)
        
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if (event.type == KEYDOWN):
            if (event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            for player in players:


                if (event.key == player.upkey):
                    if (canmoveto((player.z,player.y-1,player.x)) == True):
                        print("Moving up from {0}".format(player.pos))
                        Character.instances[(player.z,player.y-1,player.x)] = Character.instances.pop((player.z,player.y,player.x))
                        player.setpos((player.x,player.y-1,player.z))
                        print("Moved up to {0}".format(player.pos))

                if (event.key == player.downkey):
                    if (canmoveto((player.z,player.y+1,player.x)) == True):
                        print("Moving down from {0}".format(player.pos))
                        Character.instances[(player.z,player.y+1,player.x)] = Character.instances.pop((player.z,player.y,player.x))
                        player.setpos((player.x,player.y+1,player.z))
                        print("Moved down to {0}".format(player.pos))
                
##                new_x = player.x
##                new_y = player.y
##                new_z = player.z
##                if (event.key == player.upkey) and (canMoveUp(player.x,player.y,player.z) == True):
##                    if (testLevel[player.z-1][player.y][player.x] == RAMP_N): # Going down a North Ramp
##                        new_z = player.z-1
##                    if (testLevel[player.z][player.y-1][player.x] == RAMP_S): # Going up a South Ramp
##                        new_z = player.z+1
##                    new_y = player.y-1
##                    vacant=True
##                    for occupied in players:
##                        if (occupied != player):
##                            if (new_x == occupied.x and new_y == occupied.y and new_z == occupied.z):
##                                vacant=False
##                    if (vacant == True):
##                        player.x = new_x
##                        player.y = new_y
##                        player.z = new_z
##                                
##                if (event.key == player.downkey) and (canMoveDown(player.x,player.y,player.z) == True):
##                    if (testLevel[player.z][player.y+1][player.x] == RAMP_N): # Going up a North Ramp
##                        new_z = player.z+1
##                    if (testLevel[player.z-1][player.y][player.x] == RAMP_S): # Going down a South Ramp
##                        new_z = player.z-1
##                    new_y = player.y+1
##                    vacant=True
##                    for occupied in players:
##                        if (occupied != player):
##                            if (new_x == occupied.x and new_y == occupied.y and new_z == occupied.z):
##                                vacant=False
##                    if (vacant == True):
##                        player.x = new_x
##                        player.y = new_y
##                        player.z = new_z

##                if (event.key == player.leftkey) and (canMoveLeft(player.x,player.y,player.z) == True):
##                    if (testLevel[player.z][player.y][player.x-1] == RAMP_E): # Going up an East Ramp
##                        new_z = player.z+1
##                    if (testLevel[player.z-1][player.y][player.x] == RAMP_W): # Going down a West Ramp
##                        new_z = player.z-1
##                    new_x = player.x-1
##                    vacant=True
##                    for occupied in players:
##                        if (occupied != player):
##                            if (new_x == occupied.x and new_y == occupied.y and new_z == occupied.z):
##                                vacant=False
##                    if (vacant == True):
##                        player.x = new_x
##                        player.y = new_y
##                        player.z = new_z
                        
##                if (event.key == player.rightkey) and (canMoveRight(player.x,player.y,player.z) == True):
##                    if (testLevel[player.z-1][player.y][player.x] == RAMP_E): # Going down an East Ramp
##                        new_z = player.z-1
##                    if (testLevel[player.z][player.y][player.x+1] == RAMP_W): # Going up a West Ramp
##                        new_z = player.z+1
##                    new_x = player.x+1
##                    vacant=True
##                    for occupied in players:
##                        if (occupied != player):
##                            if (new_x == occupied.x and new_y == occupied.y and new_z == occupied.z):
##                                vacant=False
##                    if (vacant == True):
##                        player.x = new_x
##                        player.y = new_y
##                        player.z = new_z
                        
                if (event.key == player.leftkey):
                    if (canmoveto((player.z,player.y,player.x-1)) == True):
                        print("Moving left from {0}".format(player.pos))
                        Character.instances[(player.z,player.y,player.x-1)] = Character.instances.pop((player.z,player.y,player.x))
                        player.setpos((player.x-1,player.y,player.z))
                        print("Moved left to {0}".format(player.pos))
                        
                if (event.key == player.rightkey):
                    if (canmoveto((player.z,player.y,player.x+1)) == True):
                        print("Moving right from {0}".format(player.pos))
                        Character.instances[(player.z,player.y,player.x+1)] = Character.instances.pop((player.z,player.y,player.x))
                        player.setpos((player.x + 1,player.y,player.z))
                        print("Moved right to {0}".format(player.pos))
                    
                if (event.key == player.actionkey) and (HEART >= testLevel[player.z][player.y][player.x] >= GEMBLUE):
                    player.inventory[player.invidx] = testLevel[player.z][player.y][player.x]
                    testLevel[player.z][player.y][player.x] = EMPTY
                    player.invidx += 1

                
            if (event.key == K_EQUALS):
                level = (level + 1) % len(levelList)
                (testLevel,spawn,objective)=load_level(levelList[level][2])
                for player in (P1,P2,P3,P4):
                    (player.x,player.y,player.z) = (spawn[player.idx-1][0],spawn[player.idx-1][1],spawn[player.idx-1][2])                
                max_x=len(testLevel[0][0])
                max_y=len(testLevel[0])
                max_z=len(testLevel)
                max_x -= 1
                max_y -= 1
                max_z -= 1
                screenOffsetX=0 + ((limit_x - max_x) / 2 * blockWidth)
                screenOffsetY=274 + ((limit_y - max_y) / 2 * blockHeight)
                playerInv=np.zeros(10,dtype=np.int)
            draw_screen()
    pygame.display.flip()
