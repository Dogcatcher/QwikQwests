# Weekend Game - Qwik Qwests

import pygame, sys, pickle
from pygame.locals import *

pygame.init()

FPS=60
fpsClock = pygame.time.Clock()

screenHeight=800
screenWidth=1200

SCREEN=pygame.display.set_mode((screenWidth,screenHeight),0,32)
pygame.display.set_caption('Qwik Qwests')

# load sprites

numBlocks=18
blockType=[None]*numBlocks

EMPTY=0

RAMP_N=1
RAMP_S=2
RAMP_E=3
RAMP_W=4

GRASSBLOCK=5
STONEBLOCK=6
WOODBLOCK=7
PLAINBLOCK=8
DIRTBLOCK=9
WALLBLOCK=10
DOORTALLC=11
BROWNBLOCK=12

WATERBLOCK=13

# ramps
blockType[RAMP_N]=pygame.image.load('PlanetCute PNG\Ramp North.png') #6
blockType[RAMP_S]=pygame.image.load('PlanetCute PNG\Ramp South.png') #7
blockType[RAMP_E]=pygame.image.load('PlanetCute PNG\Ramp East.png') #8
blockType[RAMP_W]=pygame.image.load('PlanetCute PNG\Ramp West.png') #9

# blocks
blockType[GRASSBLOCK]=pygame.image.load('PlanetCute PNG\Grass Block.png')
blockType[STONEBLOCK]=pygame.image.load('PlanetCute PNG\Stone Block.png')
blockType[PLAINBLOCK]=pygame.image.load('PlanetCute PNG\Plain Block.png')
blockType[DIRTBLOCK]=pygame.image.load('PlanetCute PNG\Dirt Block.png')
blockType[WALLBLOCK]=pygame.image.load('PlanetCute PNG\Wall Block.png')
blockType[BROWNBLOCK]=pygame.image.load('PlanetCute PNG\Brown Block.png')
blockType[WOODBLOCK]=pygame.image.load('PlanetCute PNG\Wood Block.png')

blockType[WATERBLOCK]=pygame.image.load('PlanetCute PNG\Water Block.png')
blockType[DOORTALLC]=pygame.image.load('PlanetCute PNG\Door Tall Closed.png')

ROCK=14
TREESHORT=15
TREETALL=16
TREEUGLY=17

# objects
blockType[ROCK]=pygame.image.load('PlanetCute PNG\Rock.png')
blockType[TREESHORT]=pygame.image.load('PlanetCute PNG\Tree Short.png')
blockType[TREETALL]=pygame.image.load('PlanetCute PNG\Tree Tall.png')
blockType[TREEUGLY]=pygame.image.load('PlanetCute PNG\Tree Ugly.png')

shadowType=[None]*9

SHADOW_SE=0
SHADOW_S=1
SHADOW_SW=2
SHADOW_E=3
SHADOW_W=4
SHADOW_NE=5
SHADOW_N=6
SHADOW_NW=7
SHADOW_SIDEW=8

shadowType[SHADOW_SE]=pygame.image.load('PlanetCute PNG\Shadow South East.png')
shadowType[SHADOW_S]=pygame.image.load('PlanetCute PNG\Shadow South.png')
shadowType[SHADOW_SW]=pygame.image.load('PlanetCute PNG\Shadow South West.png')
shadowType[SHADOW_E]=pygame.image.load('PlanetCute PNG\Shadow East.png')
shadowType[SHADOW_W]=pygame.image.load('PlanetCute PNG\Shadow West.png')
shadowType[SHADOW_NE]=pygame.image.load('PlanetCute PNG\Shadow North East.png')
shadowType[SHADOW_N]=pygame.image.load('PlanetCute PNG\Shadow North.png')
shadowType[SHADOW_NW]=pygame.image.load('PlanetCute PNG\Shadow North West.png')
shadowType[SHADOW_SIDEW]=pygame.image.load('PlanetCute PNG\Shadow Side West.png')

numObjects=9
objectType=[None]*numObjects


BOY=1
CATGIRL=2
HORNGIRL=3
PINKGIRL=4
PRINCESS=5
KEY=6
ENEMYBUG=7
STAR=8

objectType[BOY]=pygame.image.load('PlanetCute PNG\Character Boy.png')
objectType[CATGIRL]=pygame.image.load('PlanetCute PNG\Character Cat Girl.png')
objectType[HORNGIRL]=pygame.image.load('PlanetCute PNG\Character Horn Girl.png')
objectType[PINKGIRL]=pygame.image.load('PlanetCute PNG\Character Pink Girl.png')
objectType[PRINCESS]=pygame.image.load('PlanetCute PNG\Character Princess Girl.png')
objectType[KEY]=pygame.image.load('PlanetCute PNG\Key.png')
objectType[ENEMYBUG]=pygame.image.load('PlanetCute PNG\Enemy Bug.png')
objectType[STAR]=pygame.image.load('PlanetCute PNG\Star.png')


QwikQwests=pygame.image.load('QwikQwests.png')

BLACK = (0,0,0)
WHITE = (255,255,255)
LIGHTBLUE = (100,150,255)
BROWN = (150,100,50)
ORANGE = (255,140,0)

titleCenter = QwikQwests.get_rect()
titleCenter.center=(400,50)

#numpy.zeros((8,8,8))

#blockType[0]=Brown_Block

testLevel=[None]*6

testLevel[0]=[
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [DIRTBLOCK,DIRTBLOCK,DIRTBLOCK,DIRTBLOCK,DIRTBLOCK,DIRTBLOCK,DIRTBLOCK,DIRTBLOCK]
            ]

testLevel[1]=[
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,DIRTBLOCK],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,STONEBLOCK,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,STONEBLOCK,STONEBLOCK,STONEBLOCK],
            [GRASSBLOCK,GRASSBLOCK,GRASSBLOCK,GRASSBLOCK,GRASSBLOCK,STONEBLOCK,STONEBLOCK,STONEBLOCK]
            ]

testLevel[2]=[
            [STONEBLOCK,STONEBLOCK,WATERBLOCK,WATERBLOCK,STONEBLOCK,STONEBLOCK,STONEBLOCK,EMPTY],
            [STONEBLOCK,EMPTY,EMPTY,EMPTY,EMPTY,STONEBLOCK,STONEBLOCK,RAMP_N],
            [STONEBLOCK,STONEBLOCK,WATERBLOCK,WATERBLOCK,STONEBLOCK,STONEBLOCK,STONEBLOCK,STONEBLOCK],
            [GRASSBLOCK,GRASSBLOCK,WATERBLOCK,WATERBLOCK,GRASSBLOCK,EMPTY,EMPTY,EMPTY],
            [GRASSBLOCK,GRASSBLOCK,WATERBLOCK,WATERBLOCK,GRASSBLOCK,EMPTY,STONEBLOCK,EMPTY]
            ]

testLevel[3]=[
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,WALLBLOCK,PLAINBLOCK,EMPTY],
            [EMPTY,RAMP_W,STONEBLOCK,STONEBLOCK,RAMP_E,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,TREESHORT,EMPTY,EMPTY,ROCK,EMPTY,STONEBLOCK,EMPTY],
            ]

testLevel[4]=[
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,WALLBLOCK,EMPTY,EMPTY], 
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,STONEBLOCK,EMPTY]
            ]

testLevel[5]=[
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,WALLBLOCK,EMPTY,EMPTY], 
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,STONEBLOCK,EMPTY]
            ]
       
blockOffset=40
screenOffset=220
blockWidth=100
blockHeight=80

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
max_x=9
max_y=5
max_z=5
# work this out based on size of level read in

playerObj=1



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
    
    for z in range (0,(max_z+1)):
        offset=(z*-1*blockOffset)+screenOffset
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
                    SCREEN.blit(image, ((x*blockWidth),(y*blockHeight+(offset))))
                
                # shadow processing
                if (z < max_z) and (testLevel[z+1][y][x] == 0) and (RAMP_W < block < ROCK):
                    # South East
                    if (z < max_z) and (y < max_y) and (x < max_x) and (RAMP_W < testLevel[z+1][y+1][x+1] < ROCK) and (testLevel[z+1][y][x+1] == EMPTY) and (testLevel[z+1][y+1][x] == EMPTY):
                       SCREEN.blit(shadowType[SHADOW_SE], ((x*blockWidth),(y*blockHeight+(offset))))
                       #print("Placing SE shadow at {0},{1},{2}".format(x,y,z))
                    # South - needs check to see if we're the top block - purely a waste of cycles - nothing cosmetic AFAIK
                    if (z < max_z) and (y < max_y) and (RAMP_W < testLevel[z+1][y+1][x] < ROCK):
                       SCREEN.blit(shadowType[SHADOW_S], ((x*blockWidth),(y*blockHeight+(offset))))
                    # South West
                    if (z < max_z) and (y < max_y) and (x > min_x) and (RAMP_W < testLevel[z+1][y+1][x-1] < ROCK) and (testLevel[z+1][y][x-1] == EMPTY) and (testLevel[z+1][y+1][x] == EMPTY):
                       SCREEN.blit(shadowType[SHADOW_SW], ((x*blockWidth),(y*blockHeight+(offset))))
                    # East
                    if (z < max_z) and (x < max_x) and (RAMP_W < testLevel[z+1][y][x+1] < ROCK):
                       SCREEN.blit(shadowType[SHADOW_E], ((x*blockWidth),(y*blockHeight+(offset))))
                    # West
                    if (z < max_z) and (x > min_x) and (RAMP_W < testLevel[z+1][y][x-1] < ROCK):
                       SCREEN.blit(shadowType[SHADOW_W], ((x*blockWidth),(y*blockHeight+(offset))))
                    # North East
                    if (z < max_z) and (y > min_y) and (x < max_x) and (RAMP_W < testLevel[z+1][y-1][x+1] < ROCK) and (testLevel[z+1][y][x+1] == EMPTY) and (testLevel[z+1][y-1][x] == EMPTY):
                       SCREEN.blit(shadowType[SHADOW_NE], ((x*blockWidth),(y*blockHeight+(offset))))
                    # North
                    if (z < max_z) and (y > min_y) and (RAMP_W < testLevel[z+1][y-1][x] < ROCK):
                       SCREEN.blit(shadowType[SHADOW_N], ((x*blockWidth),(y*blockHeight+(offset))))
                    # North West
                    if (z < max_z) and (y > min_y) and (x > min_x) and (RAMP_W < testLevel[z+1][y-1][x-1] < ROCK) and (testLevel[z+1][y][x-1] == EMPTY) and (testLevel[z+1][y-1][x] == EMPTY):
                       SCREEN.blit(shadowType[SHADOW_NW], ((x*blockWidth),(y*blockHeight+(offset))))
                    # Side West
                    if (z < max_z) and (x > min_x) and (y < max_y) and (RAMP_W < testLevel[z][y+1][x-1] < ROCK) and (testLevel[z][y+1][x] == EMPTY) and (testLevel[z+1][y+1][x] == EMPTY):
                       SCREEN.blit(shadowType[SHADOW_SIDEW], ((x*blockWidth),(y*blockHeight+(offset))))

                    # **BUG** - not totally happy with this processing - particularly on ramps/static objects
                    # need to detect empty space behind it and not render
                    # South (top)
                    if (z < y + 3 )and (z < max_z) and (y > min_y) and (testLevel[z+1][y][x] == EMPTY) and (testLevel[z][y-1][x] == EMPTY) and (testLevel[z+1][y-1][x] == EMPTY):
                       SCREEN.blit(shadowType[SHADOW_S], ((x*blockWidth),(y*blockHeight+(offset)-blockOffset-tallBlockOffset)))
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
                        ramp = 20
                    player=objectType[playerObj]
                    SCREEN.blit(player, ((x*blockWidth),y*blockHeight+(offset)+ramp))

    #screen_x=player_x*blockWidth
    #screen_y=(player_y*blockHeight)+(screenOffset)-(player_z*blockOffset)
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

    
    #SCREEN.blit(objectType[obj], (player_x, player_y+screenOffset))
    #render_object(SCREEN,obj,player_x,player_y,player_z)
    
        
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if (event.type == KEYDOWN):
            if (event.key == K_UP) and (canMoveUp(player_x,player_y,player_z) == True):
                # Going down a North Ramp
                if (testLevel[player_z-1][player_y][player_x] == RAMP_N):
                    player_z-=1
                # Going up a South Ramp
                if (testLevel[player_z][player_y-1][player_x] == RAMP_S):
                    player_z+=1
                player_y-=1
                #print("moved to x:{0}, y:{1}, z:{2}".format(player_x,player_y,player_z))
                
            if (event.key == K_DOWN) and (canMoveDown(player_x,player_y,player_z) == True):
                # Going up a North Ramp
                if (testLevel[player_z][player_y+1][player_x] == RAMP_N):
                    player_z+=1
                # Going down a South Ramp
                if (testLevel[player_z-1][player_y][player_x] == RAMP_S):
                    player_z-=1
                player_y+=1
                #print("moved to x:{0}, y:{1}, z:{2}".format(player_x,player_y,player_z))

            if (event.key == K_LEFT) and (canMoveLeft(player_x,player_y,player_z) == True):
                # Going up an East Ramp
                if (testLevel[player_z][player_y][player_x-1] == RAMP_E):
                    player_z+=1
                # Going down a West Ramp
                if (testLevel[player_z-1][player_y][player_x] == RAMP_W):
                    player_z-=1
                player_x-=1
                #print("moved to x:{0}, y:{1}, z:{2}".format(player_x,player_y,player_z))
                
            if (event.key == K_RIGHT) and (canMoveRight(player_x,player_y,player_z) == True):
                # Going down an East Ramp
                if (testLevel[player_z-1][player_y][player_x] == RAMP_E):
                    player_z-=1
                # Going up a West Ramp
                if (testLevel[player_z][player_y][player_x+1] == RAMP_W):
                    player_z+=1
                player_x+=1
                #print("moved to x:{0}, y:{1}, z:{2}".format(player_x,player_y,player_z))
            #if(event.key == K_RIGHTBRACKET):
                #return True
                #goToNextLevel()
            #if (event.key == K_PAGEUP) and (player_z < max_z) and (canMove(0,0,1,player_x,player_y,player_z) == True):
            #    #print("x:{0}, y:{1}, z:{2}".format(player_x,player_y,player_z))
            #    player_z=player_z + 1

            #if (event.key == K_PAGEDOWN) and (player_z > min_z) and (canMove(0,0,-1,player_x,player_y,player_z) == True):
            #    #print("x:{0}, y:{1}, z:{2}".format(player_x,player_y,player_z))
            #    player_z=player_z - 1

            if (event.key == K_l):
                level = (level + 1) % 2
                print("Loading level {0} - {1}".format(levelList[level][0],levelList[level][1]))
                (testLevel,spawn,objective)=load_level(levelList[level][2])
                player_x=spawn[0]
                player_y=spawn[1]
                player_z=spawn[2]
                
            
            draw_screen()

    pygame.display.update()
