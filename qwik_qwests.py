# Weekend Game - Qwik Qwests

import pygame, sys, pickle
from blocks import *
from pygame.locals import *

pygame.init()

FPS=60
fpsClock = pygame.time.Clock()

screenHeight=800
screenWidth=1200

SCREEN=pygame.display.set_mode((screenWidth,screenHeight),0,32)
pygame.display.set_caption('Qwik Qwests')

# load sprites




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

#numpy.zeros((8,8,8))

#blockType[0]=Brown_Block

testLevel=[None]*6

blockWidth=50
blockHeight=40      

limit_y=11
limit_x=19

blockOffset=20
# enhancement - work out way to central screen

delta_x=0
delta_y=0
delta_z=0

spawn=[0,0,0]
objective=[9,5,5]

# load level

listFH=open('levellist.pkl','rb')
levelList=pickle.load(listFH)
listFH.close()

level=0


def load_level(p):
    i='levels\\' + p
    FH=open(i,'rb') # add error if doesn't exist
    l=pickle.load(FH)
    s=pickle.load(FH)
    o=pickle.load(FH)
    FH.close()
    return(l,s,o)

print("Loading level {0} - {1}".format(levelList[level][0],levelList[level][1]))
(testLevel,spawn,objective)=load_level(levelList[level][2])

player_x=spawn[0]
player_y=spawn[1]
player_z=spawn[2]

min_x=0
min_y=0
min_z=0

# work this out based on size of level read in
#max_x=9
#max_y=5
#max_z=5
max_x=len(testLevel[0][0])
max_y=len(testLevel[0])
max_z=len(testLevel)
print("level is size x:{0} y:{1} z:{2}".format(max_x,max_y,max_z))
max_x -= 1
max_y -= 1
max_z -= 1
# work this out based on size of level read in

screenOffsetX=0 + ((limit_x - max_x) / 2 * blockWidth)
screenOffsetY=274 + ((limit_y - max_y) / 2 * blockHeight)

playerObj=1
playerInv=[None]*10
indexInv=0

def draw_inventory():
    print("Drawing inventory")
    for i in range (1,11):
        print("Slot {0} = {1}".format(i,playerInv[i-1]))

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
    
draw_inventory()

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
    
    for z in range (0,(max_z+1)):
        offset=(z*-1*blockOffset)+screenOffsetY
        for y in range (0,(max_y+1)):
            for x in range (0,(max_x+1)):
                block=testLevel[z][y][x]
                
                tallBlockOffset=0
                if (block == DOORTALLC):
                    tallBlockoffset=2*blockOffset

                # possile bug with high south shadow at back of tall blocks - well tall blocks in general
                # suspect need shadow shift for all tall blocks - fix another day

                if block > 0:
                    image=blockType[block]
                    SCREEN.blit(image, ((x*blockWidth+screenOffsetX),(y*blockHeight+(offset))))
                
                # shadow processing
                if (z < max_z) and (testLevel[z+1][y][x] == EMPTY or (TREEUGLY < testLevel[z+1][y][x] < CHESTC)) and (RAMP_W < block < ROCK):
                    # South East
                    if (z < max_z) and (y < max_y) and (x < max_x) and (RAMP_W < testLevel[z+1][y+1][x+1] < ROCK) and (testLevel[z+1][y][x+1] == EMPTY) and (testLevel[z+1][y+1][x] == EMPTY):
                       SCREEN.blit(shadowType[SHADOW_SE], ((x*blockWidth+screenOffsetX),(y*blockHeight+(offset))))
                       #print("Placing SE shadow at {0},{1},{2}".format(x,y,z))
                    # South - needs check to see if we're the top block - purely a waste of cycles - nothing cosmetic AFAIK
                    if (z < max_z) and (y < max_y) and (RAMP_W < testLevel[z+1][y+1][x] < ROCK):
                       SCREEN.blit(shadowType[SHADOW_S], ((x*blockWidth+screenOffsetX),(y*blockHeight+(offset))))
                    # South West
                    if (z < max_z) and (y < max_y) and (x > min_x) and (RAMP_W < testLevel[z+1][y+1][x-1] < ROCK) and (testLevel[z+1][y][x-1] == EMPTY) and (testLevel[z+1][y+1][x] == EMPTY):
                       SCREEN.blit(shadowType[SHADOW_SW], ((x*blockWidth+screenOffsetX),(y*blockHeight+(offset))))
                    # East
                    if (z < max_z) and (x < max_x) and (RAMP_W < testLevel[z+1][y][x+1] < ROCK):
                       SCREEN.blit(shadowType[SHADOW_E], ((x*blockWidth+screenOffsetX),(y*blockHeight+(offset))))
                    # West
                    if (z < max_z) and (x > min_x) and (RAMP_W < testLevel[z+1][y][x-1] < ROCK):
                       SCREEN.blit(shadowType[SHADOW_W], ((x*blockWidth+screenOffsetX),(y*blockHeight+(offset))))
                    # North East
                    if (z < max_z) and (y > min_y) and (x < max_x) and (RAMP_W < testLevel[z+1][y-1][x+1] < ROCK) and (testLevel[z+1][y][x+1] == EMPTY) and (testLevel[z+1][y-1][x] == EMPTY):
                       SCREEN.blit(shadowType[SHADOW_NE], ((x*blockWidth+screenOffsetX),(y*blockHeight+(offset))))
                    # North
                    if (z < max_z) and (y > min_y) and (RAMP_W < testLevel[z+1][y-1][x] < ROCK):
                       SCREEN.blit(shadowType[SHADOW_N], ((x*blockWidth+screenOffsetX),(y*blockHeight+(offset))))
                    # North West
                    if (z < max_z) and (y > min_y) and (x > min_x) and (RAMP_W < testLevel[z+1][y-1][x-1] < ROCK) and (testLevel[z+1][y][x-1] == EMPTY) and (testLevel[z+1][y-1][x] == EMPTY):
                       SCREEN.blit(shadowType[SHADOW_NW], ((x*blockWidth+screenOffsetX),(y*blockHeight+(offset))))
                    # Side West
                    if (z < max_z) and (x > min_x) and (y < max_y) and (RAMP_W < testLevel[z][y+1][x-1] < ROCK) and (testLevel[z][y+1][x] == EMPTY) and (testLevel[z+1][y+1][x] == EMPTY):
                       SCREEN.blit(shadowType[SHADOW_SIDEW], ((x*blockWidth+screenOffsetX),(y*blockHeight+(offset))))

                    # **BUG** - not totally happy with this processing - particularly on ramps/static objects
                    # need to detect empty space behind it and not render
                    # South (top)
                    if (z < y + 3 )and (z < max_z) and (y > min_y) and (testLevel[z+1][y][x] == EMPTY) and (testLevel[z][y-1][x] == EMPTY) and (testLevel[z+1][y-1][x] == EMPTY):
                       SCREEN.blit(shadowType[SHADOW_S], ((x*blockWidth+screenOffsetX),(y*blockHeight+(offset)-blockOffset-tallBlockOffset)))
                # South (top ceiling)
                #if (x == 6) and (y == 3) and (z == 5):
                #    #print("DEBUG: block {0}".format(testLevel[z][y-1][x]))
                #if (z < y + 3) and (z == max_z) and (y > min_y) and (testLevel[z][y-1][x] == EMPTY):
                #  SCREEN.blit(shadowType[SHADOW_S], ((x*blockWidth),(y*blockHeight+(offset)-blockOffset-tallBlockOffset)))                       
                # Player 
                if (z == player_z) and (x == player_x) and (y == player_y):
                    # visual adjustment for when player is on a ramp
                    ramp = 0
                    below=testLevel[z-1][y][x]
                    if (below == RAMP_N) or (below == RAMP_S) or (below == RAMP_E) or (below == RAMP_W):
                        ramp = 10
                    # print("DEBUG ramp adjustment {0}".format(ramp))
                    player=objectType[playerObj]
                    SCREEN.blit(player, ((x*blockWidth+screenOffsetX+delta_x),(y*blockHeight+offset+ramp+delta_y+delta_z)))
                if (z == objective[2] ) and (y == objective[1]) and (x == objective[0]):
                    SCREEN.blit(objectType[STAR], ((x*blockWidth+screenOffsetX),y*blockHeight+offset))

    #screen_x=player_x*blockWidth
    #screen_y=(player_y*blockHeight)+(screenOffsetY)-(player_z*blockOffset)
    #s.blit(objectType[playerObj], (screen_x, screen_y))


def canMoveRight(px,py,pz):
    ##print("px:{0} py:{1} pz:{2} max_x:{3} block:{4}".format(px,py,pz,max_x,testLevel[pz][py][px+1]))
    if (px < max_x):
        #print("Not at the far right edge")
        if (testLevel[pz][py][px + 1] == EMPTY) and (testLevel[pz-1][py][px+1] < WATERBLOCK):
            #print("Can move right")
            if (testLevel[pz-1][py][px+1] == EMPTY):
                #print("But there's a drop")
                #print("We're on a {0}".format(testLevel[pz-1][py][px]))
                if (testLevel[pz-1][py][px] == RAMP_E):  
                    #print("so that's ok because we're on an East ramp")
                    return True
                return False
            return True
        if (testLevel[pz][py][px+1] == RAMP_W):
            #print("Up onto the West ramp")
            return True
        #print("Something in the way")
        return False
    #print("At the far right edge")
    return False

def canMoveLeft(px,py,pz):
    ##print("px:{0} py:{1} pz:{2} min_x:{3} block:{4}".format(px,py,pz,min_x,testLevel[pz][py][px-1]))
    if (px > min_x):
        #print("Not at the far left edge")
        if (testLevel[pz][py][px-1] == EMPTY) and (testLevel[pz-1][py][px-1] < WATERBLOCK):
            #print("Can move left")
            if (testLevel[pz-1][py][px-1] == EMPTY):
                #print("But there's a drop")
                #print("We're on a {0}".format(testLevel[pz-1][py][px]))
                if (testLevel[pz-1][py][px] == RAMP_W):  
                    #print("so that's ok because we're on an West ramp")
                    return True
                return False
            return True
        if (testLevel[pz][py][px-1] == RAMP_E):
            #print("Up onto the East ramp")
            return True
        #print("Something in the way")
        return False
    #print("At the far left edge")
    return False

def canMoveUp(px,py,pz):
    ##print("px:{0} py:{1} pz:{2} max_y:{3} block:{4}".format(px,py,pz,max_y,testLevel[pz][py-1][px]))
    if (py > min_y):
        #print("Not at the far top edge")
        if (testLevel[pz][py-1][px] == EMPTY) and (testLevel[pz-1][py-1][px] < WATERBLOCK):
            #print("Can move up")
            if (testLevel[pz-1][py-1][px] == EMPTY):
                #print("But there's a drop")
                #print("We're on a {0}".format(testLevel[pz-1][py][px]))
                if (testLevel[pz-1][py][px] == RAMP_N):  
                    #print("so that's ok because we're on a North ramp")
                    return True
                return False
            return True
        if (testLevel[pz][py-1][px] == RAMP_S):
            #print("Up onto the South ramp")
            return True
        #print("Something in the way")
        return False
    #print("At the far top edge")
    return False

def canMoveDown(px,py,pz):
    ##print("px:{0} py:{1} pz:{2} max_y:{3} block:{4}".format(px,py,pz,max_y,testLevel[pz][py+1][px]))
    if (py < max_y):
        #print("Not at the far bottom edge")
        if (testLevel[pz][py+1][px] == EMPTY) and (testLevel[pz-1][py+1][px] < WATERBLOCK):
            #print("Can move down")
            if (testLevel[pz-1][py+1][px] == EMPTY):
                #print("But there's a drop")
                #print("We're on a {0}".format(testLevel[pz-1][py][px]))
                if (testLevel[pz-1][py][px] == RAMP_S):  
                    #print("so that's ok because we're on a South ramp")
                    return True
                return False
            return True
        if (testLevel[pz][py+1][px] == RAMP_N):
            #print("Up onto the North ramp")
            return True
        #print("Something in the way")
        return False
    #print("At the far bottom edge")
    return False


def changeLevel(direction):
    if(direction == "next"):
        return True
        




#obj = 0

#render_object(SCREEN,obj,player_x,player_y,player_z)

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
            (new_x,new_y,new_z) = (player_x,player_y,player_z)
            if (event.key == K_UP) and (canMoveUp(player_x,player_y,player_z) == True):
                if (testLevel[player_z-1][player_y][player_x] == RAMP_N):
                    new_z = player_z -1
                if (testLevel[player_z][player_y-1][player_x] == RAMP_S):
                    new_z = player_z+1
                new_y=player_y-1
                
            if (event.key == K_DOWN) and (canMoveDown(player_x,player_y,player_z) == True):
                if (testLevel[player_z][player_y+1][player_x] == RAMP_N):
                    new_z=player_z+1
                if (testLevel[player_z-1][player_y][player_x] == RAMP_S):
                    new_z=player_z-1
                new_y=player_y+1

            if (event.key == K_LEFT) and (canMoveLeft(player_x,player_y,player_z) == True):
                if (testLevel[player_z][player_y][player_x-1] == RAMP_E):
                    new_z=player_z+1
                if (testLevel[player_z-1][player_y][player_x] == RAMP_W):
                    new_z=player_z-1
                new_x=player_x-1
                
            if (event.key == K_RIGHT) and (canMoveRight(player_x,player_y,player_z) == True):
                if (testLevel[player_z-1][player_y][player_x] == RAMP_E):
                    new_z=player_z-1
                if (testLevel[player_z][player_y][player_x+1] == RAMP_W):
                    new_z=player_z+1
                new_x=player_x+1

            if (event.key == K_i and object_down(player_x,player_y,player_z)):
                playerInv[indexInv] = testLevel[player_z][player_y+1][player_x]
                testLevel[player_z][player_y+1][player_x] = EMPTY
                indexInv += 1
                draw_inventory()

            if (event.key == K_i and object_up(player_x,player_y,player_z)):
                playerInv[indexInv] = testLevel[player_z][player_y-1][player_x]
                testLevel[player_z][player_y-1][player_x] = EMPTY
                indexInv += 1
                draw_inventory()    

            if (event.key == K_i and object_left(player_x,player_y,player_z)):
                playerInv[indexInv] = testLevel[player_z][player_y][player_x-1]
                testLevel[player_z][player_y][player_x-1] = EMPTY
                indexInv += 1
                draw_inventory()

            if (event.key == K_i and object_down(player_x,player_y,player_z)):
                playerInv[indexInv] = testLevel[player_z][player_y][player_x+1]
                testLevel[player_z][player_y][player_x+1] = EMPTY
                indexInv += 1
                draw_inventory()
                
##            if (event.key == K_o and indexInv > 0):
##                indexInv -= 1
##                testLevel[player_z][player_y+1][player_x] = playerInv[indexInv]
##                playerInv[indexInv] = EMPTY
##                draw_inventory()
                
##            if (event.key == K_l):
##                level = (level + 1) % len(levelList)
##                print("Loading level {0} - {1}".format(levelList[level][0],levelList[level][1]))
##                (testLevel,spawn,objective)=load_level(levelList[level][2])
##                player_x=spawn[0]
##                player_y=spawn[1]
##                player_z=spawn[2]
##                max_x=len(testLevel[0][0])
##                max_y=len(testLevel[0])
##                max_z=len(testLevel)
##                print("level is size x:{0} y:{1} z:{2}".format(max_x,max_y,max_z))
##                max_x -= 1
##                max_y -= 1
##                max_z -= 1
##                screenOffsetX=0 + ((limit_x - max_x) / 2 * blockWidth)
##                screenOffsetY=274 + ((limit_y - max_y) / 2 * blockHeight)
            if (player_x == objective[0]) and (player_y == objective[1]) and (player_z == objective[2]):
                level = (level + 1) % len(levelList)
                print("Loading level {0} - {1}".format(levelList[level][0],levelList[level][1]))
                (testLevel,spawn,objective)=load_level(levelList[level][2])
                player_x=spawn[0]
                player_y=spawn[1]
                player_z=spawn[2]
                max_x=len(testLevel[0][0])
                max_y=len(testLevel[0])
                max_z=len(testLevel)
                print("level is size x:{0} y:{1} z:{2}".format(max_x,max_y,max_z))
                max_x -= 1
                max_y -= 1
                max_z -= 1
                screenOffsetX=0 + ((limit_x - max_x) / 2 * blockWidth)
                screenOffsetY=274 + ((limit_y - max_y) / 2 * blockHeight)                
            if ((new_x,new_y,new_z) != (player_x,player_y,player_z)):
                if (player_x < new_x):
                    # moving right
                    for delta_x in range (1, (blockWidth - 1),2):
                        if (player_z < new_z):
                            delta_z = int(delta_x * blockOffset / blockWidth) * -1
                        draw_screen()
                        pygame.display.flip()
            delta_x = 0
            delta_y = 0
            delta_z = 0
            (player_x,player_y,player_z) = (new_x,new_y,new_z)
            
            draw_screen()

    pygame.display.flip()
