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


numBlocks=27
blockType=[None]*numBlocks

EMPTY=0

cursorBlock=0

RAMP_N=1
RAMP_S=2
RAMP_E=3
RAMP_W=4

GRASSBLOCK=5
STONEBLOCK=6
WATERBLOCK=13
PLAINBLOCK=8
DIRTBLOCK=9
WALLBLOCK=10
DOORTALLC=11
BROWNBLOCK=12
WOODBLOCK=7

iPath='PlanetCute PNG'

# ramps
blockType[RAMP_N]=pygame.image.load((iPath+'\Ramp North.png')) #6
blockType[RAMP_S]=pygame.image.load('PlanetCute PNG\Ramp South.png') #7
blockType[RAMP_E]=pygame.image.load('PlanetCute PNG\Ramp East.png') #8
blockType[RAMP_W]=pygame.image.load('PlanetCute PNG\Ramp West.png') #9

# blocks
blockType[GRASSBLOCK]=pygame.image.load('PlanetCute PNG\Grass Block.png')
blockType[STONEBLOCK]=pygame.image.load('PlanetCute PNG\Stone Block.png')
blockType[WATERBLOCK]=pygame.image.load('PlanetCute PNG\Water Block.png')
blockType[PLAINBLOCK]=pygame.image.load('PlanetCute PNG\Plain Block.png')
blockType[DIRTBLOCK]=pygame.image.load('PlanetCute PNG\Dirt Block.png')
blockType[WALLBLOCK]=pygame.image.load('PlanetCute PNG\Wall Block.png')
blockType[BROWNBLOCK]=pygame.image.load('PlanetCute PNG\Brown Block.png')
blockType[WOODBLOCK]=pygame.image.load('PlanetCute PNG\Wood Block.png')

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

itemType=[None]*6

BUG=18
GEMBLUE=19
GEMGREEN=20
GEMORANGE=21
KEY=22
HEART=23
CHESTC=24
CHESTL=25
CHESTO=26


#item
blockType[BUG]=pygame.image.load((iPath+'\Enemy Bug.png'))
blockType[GEMBLUE]=pygame.image.load((iPath+'\Gem Blue.png'))
blockType[GEMGREEN]=pygame.image.load((iPath+'\Gem Green.png'))
blockType[GEMORANGE]=pygame.image.load((iPath+'\Gem Orange.png'))
blockType[KEY]=pygame.image.load((iPath+'\Key.png'))
blockType[HEART]=pygame.image.load((iPath+'\Heart.png'))
blockType[CHESTC]=pygame.image.load((iPath+'\Chest Closed.png'))
blockType[CHESTL]=pygame.image.load((iPath+'\Chest Lid.png'))
blockType[CHESTO]=pygame.image.load((iPath+'\Chest Open.png'))


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


SELECTOR=0
BOY=1
CATGIRL=2
HORNGIRL=3
PINKGIRL=4
PRINCESS=5
KEY=6
ENEMYBUG=7
STAR=8

objectType[SELECTOR]=pygame.image.load('PlanetCute PNG\Selector.png')
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

titleCenter = QwikQwests.get_rect()
titleCenter.center=(400,50)

#numpy.zeros((8,8,8))

#blockType[0]=Brown_Block

testLevel=[None]*6



emptyLayer=[
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY], 
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY]
            ]

testLevel[0]=[
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [DIRTBLOCK,DIRTBLOCK,DIRTBLOCK,DIRTBLOCK,DIRTBLOCK,DIRTBLOCK,DIRTBLOCK,DIRTBLOCK,DIRTBLOCK,DIRTBLOCK]
            ]

testLevel[1]=[
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,DIRTBLOCK,DIRTBLOCK,DIRTBLOCK],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,DIRTBLOCK,DIRTBLOCK,DIRTBLOCK],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,DIRTBLOCK,DIRTBLOCK,DIRTBLOCK],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,BROWNBLOCK,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,STONEBLOCK,STONEBLOCK,STONEBLOCK,STONEBLOCK,STONEBLOCK],
            [GRASSBLOCK,GRASSBLOCK,GRASSBLOCK,GRASSBLOCK,GRASSBLOCK,STONEBLOCK,STONEBLOCK,STONEBLOCK,STONEBLOCK,STONEBLOCK]
            ]

testLevel[2]=[
            [STONEBLOCK,STONEBLOCK,WATERBLOCK,WATERBLOCK,STONEBLOCK,STONEBLOCK,STONEBLOCK,STONEBLOCK,STONEBLOCK,STONEBLOCK],
            [STONEBLOCK,EMPTY,EMPTY,EMPTY,EMPTY,STONEBLOCK,STONEBLOCK,BROWNBLOCK,BROWNBLOCK,BROWNBLOCK],
            [STONEBLOCK,STONEBLOCK,WATERBLOCK,WATERBLOCK,STONEBLOCK,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [GRASSBLOCK,GRASSBLOCK,WATERBLOCK,WATERBLOCK,GRASSBLOCK,EMPTY,WOODBLOCK,EMPTY,EMPTY,EMPTY],
            [GRASSBLOCK,GRASSBLOCK,WATERBLOCK,WATERBLOCK,GRASSBLOCK,STONEBLOCK,EMPTY,EMPTY,EMPTY,EMPTY],
            [GRASSBLOCK,GRASSBLOCK,WATERBLOCK,WATERBLOCK,GRASSBLOCK,STONEBLOCK,EMPTY,EMPTY,EMPTY,EMPTY]
            ]

testLevel[3]=[
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,WALLBLOCK,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,RAMP_W,STONEBLOCK,STONEBLOCK,RAMP_E,EMPTY,EMPTY,BROWNBLOCK,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,WOODBLOCK,EMPTY,EMPTY,EMPTY],
            [EMPTY,TREESHORT,EMPTY,EMPTY,ROCK,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY]
            ]

testLevel[4]=[
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,WALLBLOCK,EMPTY,EMPTY,EMPTY,EMPTY], 
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,BROWNBLOCK,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,WOODBLOCK,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY]
            ]

testLevel[5]=[
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,WALLBLOCK,EMPTY,EMPTY,EMPTY,EMPTY], 
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,WATERBLOCK,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY]
            ]
       
#def render (s,l,x,y):
    # s=surface l=3d level array, x=x, y=y
    # pass 3d array into function
    

    #s.blit

def fill_gradient(surface, color, gradient, rect=None, vertical=True, forward=True):
    return True

blockOffset=40
screenOffset=220
blockWidth=100
blockHeight=80

spawn=[0,0,3]
objective=[9,5,5]

player_x=spawn[0]
player_y=spawn[1]
player_z=spawn[2]

min_x=0
min_y=0
min_z=0
max_x=9
max_y=5
max_z=5

sdebug=2

gradientRect=pygame.Rect(0,0,screenWidth,375)


SCREEN.blit(QwikQwests, titleCenter)

def draw_screen():
    SCREEN.fill(WHITE)
    fill_gradient(SCREEN,LIGHTBLUE,WHITE,gradientRect,True,True)
    for z in range (0,(player_z+1)):
        offset=(z*-1*blockOffset)+screenOffset
        for y in range (0,(max_y+1)):
            for x in range (0,(max_x+1)):
                block=testLevel[z][y][x]
                
                tallBlockOffset=0
                if (block == DOORTALLC):
                    tallBlockoffset=2*blockOffset

                # possile bug with high south shadow at back of tall blocks - well tall blocks in general
                # suspect need shadow shift for all tall blocks - fix another day
                
                if (block > 0):

                    
                    paintBlock=0
                    if (sdebug==1):
                        paintBlock=PLAINBLOCK
                    if (sdebug==2):
                        paintBlock=block

                    if (sdebug > 0):
                        image=blockType[paintBlock]                   
                        SCREEN.blit(image, ((x*blockWidth),(y*blockHeight+(offset))))

                    showSE=True
                    showS=True
                    showSW=True
                    showE=True
                    showW=True
                    showNE=True
                    showN=True
                    showNW=True
                    showSIDEW=True
                    showS2=True
                    showS5=True

                    # shadow processing
                    if (z < max_z) and (testLevel[z+1][y][x] == 0) and (RAMP_W < block < ROCK):
                        # South East
                        if (showSE == True) and (z < max_z) and (y < max_y) and (x < max_x) and (RAMP_W < testLevel[z+1][y+1][x+1] < ROCK) and (testLevel[z+1][y][x+1] == EMPTY) and (testLevel[z+1][y+1][x] == EMPTY):
                           SCREEN.blit(shadowType[SHADOW_SE], ((x*blockWidth),(y*blockHeight+(offset))))
                           print("Placing SE shadow at {0},{1},{2}".format(x,y,z))
                        # South - needs check to see if we're the top block - purely a waste of cycles - nothing cosmetic AFAIK
                        if (showS == True) and (z < max_z) and (y < max_y) and (RAMP_W < testLevel[z+1][y+1][x] < ROCK):
                           SCREEN.blit(shadowType[SHADOW_S], ((x*blockWidth),(y*blockHeight+(offset))))
                        # South West
                        if (showSW == True) and (z < max_z) and (y < max_y) and (x > min_x) and (RAMP_W < testLevel[z+1][y+1][x-1] < ROCK) and (testLevel[z+1][y][x-1] == EMPTY) and (testLevel[z+1][y+1][x] == EMPTY):
                           SCREEN.blit(shadowType[SHADOW_SW], ((x*blockWidth),(y*blockHeight+(offset))))
                        # East
                        if (showE == True)  and (z < max_z) and (x < max_x) and (RAMP_W < testLevel[z+1][y][x+1] < ROCK):
                           SCREEN.blit(shadowType[SHADOW_E], ((x*blockWidth),(y*blockHeight+(offset))))
                        # West
                        if (showW == True)  and (z < max_z) and (x > min_x) and (RAMP_W < testLevel[z+1][y][x-1] < ROCK):
                           SCREEN.blit(shadowType[SHADOW_W], ((x*blockWidth),(y*blockHeight+(offset))))
                        # North East
                        if (showNE == True)  and (z < max_z) and (y > min_y) and (x < max_x) and (RAMP_W < testLevel[z+1][y-1][x+1] < ROCK) and (testLevel[z+1][y][x+1] == EMPTY) and (testLevel[z+1][y-1][x] == EMPTY):
                           SCREEN.blit(shadowType[SHADOW_NE], ((x*blockWidth),(y*blockHeight+(offset))))
                        # North
                        if (showN == True)  and (z < max_z) and (y > min_y) and (RAMP_W < testLevel[z+1][y-1][x] < ROCK):
                           SCREEN.blit(shadowType[SHADOW_N], ((x*blockWidth),(y*blockHeight+(offset))))
                        # North West
                        if (showNW == True)  and (z < max_z) and (y > min_y) and (x > min_x) and (RAMP_W < testLevel[z+1][y-1][x-1] < ROCK) and (testLevel[z+1][y][x-1] == EMPTY) and (testLevel[z+1][y-1][x] == EMPTY):
                           SCREEN.blit(shadowType[SHADOW_NW], ((x*blockWidth),(y*blockHeight+(offset))))
                        # Side West
                        if (showSIDEW == True) and (z < max_z) and (x > min_x) and (y < max_y) and (RAMP_W < testLevel[z][y+1][x-1] < ROCK) and (testLevel[z][y+1][x] == EMPTY) and (testLevel[z+1][y+1][x] == EMPTY):
                           SCREEN.blit(shadowType[SHADOW_SIDEW], ((x*blockWidth),(y*blockHeight+(offset))))

                        # **BUG** - not totally happy with this processing - particularly on ramps/static objects
                        # need to detect empty space behind it and not render
                        # South (top)
                        if (showS2 == True)  and (z < y + 3 )and (z < max_z) and (y > min_y) and (testLevel[z+1][y][x] == EMPTY) and (testLevel[z][y-1][x] == EMPTY) and (testLevel[z+1][y-1][x] == EMPTY):
                           SCREEN.blit(shadowType[SHADOW_S], ((x*blockWidth),(y*blockHeight+(offset)-blockOffset-tallBlockOffset)))
                    # South (top ceiling)
                    #if (x == 6) and (y == 3) and (z == 5):
                    #    print("DEBUG: block {0}".format(testLevel[z][y-1][x]))
                    if (showS5 == True)  and (z < y + 3) and (z == max_z) and (y > min_y) and (testLevel[z][y-1][x] == EMPTY):
                       SCREEN.blit(shadowType[SHADOW_S], ((x*blockWidth),(y*blockHeight+(offset)-blockOffset-tallBlockOffset)))                   
                # spawn point
                if (z == spawn[2]) and (y == spawn[1]) and (x == spawn[0]):
                    SCREEN.blit(objectType[BOY], ((x*blockWidth),y*blockHeight+offset))                    

                # objective point
                if (z == objective[2]) and (y == objective[1]) and (x == objective[0]):
                    SCREEN.blit(objectType[STAR], ((x*blockWidth),y*blockHeight+offset))                    

                # Cursor 
                if (z == player_z) and (x == player_x) and (y == player_y):
                    #below=testLevel[z-1][y][x]
                    #if (below == RAMP_N) or (below == RAMP_S) or (below == RAMP_E) or (below == RAMP_W):
                    #    ramp = 20
                    if (cursorBlock > 0):
                        SCREEN.blit(blockType[cursorBlock], ((x*blockWidth),y*blockHeight+offset))
                    SCREEN.blit(objectType[SELECTOR], ((x*blockWidth),y*blockHeight+offset-blockOffset))

    #screen_x=player_x*blockWidth
    #screen_y=(player_y*blockHeight)+(screenOffset)-(player_z*blockOffset)
    #s.blit(objectType[playerObj], (screen_x, screen_y))


def canMoveRight(px,py,pz):
    #print("px:{0} py:{1} pz:{2} max_x:{3} block:{4}".format(px,py,pz,max_x,testLevel[pz][py][px+1]))
    if (px < max_x):
        print("Not at the far right edge")
        if (testLevel[pz][py][px + 1] == EMPTY) and (testLevel[pz-1][py][px+1] != WATERBLOCK):
            print("Can move right")
            if (testLevel[pz-1][py][px+1] == EMPTY):
                print("But there's a drop")
                print("We're on a {0}".format(testLevel[pz-1][py][px]))
                if (testLevel[pz-1][py][px] == RAMP_E):  
                    print("so that's ok because we're on an East ramp")
                    return True
                return False
            return True
        if (testLevel[pz][py][px+1] == RAMP_W):
            print("Up onto the West ramp")
            return True
        print("Something in the way")
        return False
    print("At the far right edge")
    return False

def canMoveLeft(px,py,pz):
    #print("px:{0} py:{1} pz:{2} min_x:{3} block:{4}".format(px,py,pz,min_x,testLevel[pz][py][px-1]))
    if (px > min_x):
        print("Not at the far left edge")
        if (testLevel[pz][py][px-1] == EMPTY) and (testLevel[pz-1][py][px-1] != WATERBLOCK):
            print("Can move left")
            if (testLevel[pz-1][py][px-1] == EMPTY):
                print("But there's a drop")
                print("We're on a {0}".format(testLevel[pz-1][py][px]))
                if (testLevel[pz-1][py][px] == RAMP_W):  
                    print("so that's ok because we're on an West ramp")
                    return True
                return False
            return True
        if (testLevel[pz][py][px-1] == RAMP_E):
            print("Up onto the East ramp")
            return True
        print("Something in the way")
        return False
    print("At the far left edge")
    return False

def canMoveUp(px,py,pz):
    #print("px:{0} py:{1} pz:{2} max_y:{3} block:{4}".format(px,py,pz,max_y,testLevel[pz][py-1][px]))
    if (py > min_y):
        print("Not at the far top edge")
        if (testLevel[pz][py-1][px] == EMPTY) and (testLevel[pz-1][py-1][px] != WATERBLOCK):
            print("Can move up")
            if (testLevel[pz-1][py-1][px] == EMPTY):
                print("But there's a drop")
                print("We're on a {0}".format(testLevel[pz-1][py][px]))
                if (testLevel[pz-1][py][px] == RAMP_N):  
                    print("so that's ok because we're on a North ramp")
                    return True
                return False
            return True
        if (testLevel[pz][py-1][px] == RAMP_S):
            print("Up onto the South ramp")
            return True
        print("Something in the way")
        return False
    print("At the far top edge")
    return False

def canMoveDown(px,py,pz):
    #print("px:{0} py:{1} pz:{2} max_y:{3} block:{4}".format(px,py,pz,max_y,testLevel[pz][py+1][px]))
    if (py < max_y):
        print("Not at the far bottom edge")
        if (testLevel[pz][py+1][px] == EMPTY) and (testLevel[pz-1][py+1][px] != WATERBLOCK):
            print("Can move down")
            if (testLevel[pz-1][py+1][px] == EMPTY):
                print("But there's a drop")
                print("We're on a {0}".format(testLevel[pz-1][py][px]))
                if (testLevel[pz-1][py][px] == RAMP_S):  
                    print("so that's ok because we're on a South ramp")
                    return True
                return False
            return True
        if (testLevel[pz][py+1][px] == RAMP_N):
            print("Up onto the North ramp")
            return True
        print("Something in the way")
        return False
    print("At the far bottom edge")
    return False







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
            if (event.key == K_UP) and (player_y > min_y):
                # Going down a North Ramp
                #if (testLevel[player_z-1][player_y][player_x] == RAMP_N):
                #    player_z-=1
                # Going up a South Ramp
                #if (testLevel[player_z][player_y-1][player_x] == RAMP_S):
                #    player_z+=1
                player_y-=1
                print("moved to x:{0}, y:{1}, z:{2}".format(player_x,player_y,player_z))
                
            if (event.key == K_DOWN) and (player_y < max_y):
                # Going up a North Ramp
                #if (testLevel[player_z][player_y+1][player_x] == RAMP_N):
                #    player_z+=1
                # Going down a South Ramp
                #if (testLevel[player_z-1][player_y][player_x] == RAMP_S):
                #    player_z-=1
                player_y+=1
                print("moved to x:{0}, y:{1}, z:{2}".format(player_x,player_y,player_z))
                
            if (event.key == K_LEFT) and (player_x > min_x):
                # Going up an East Ramp
                #if (testLevel[player_z][player_y][player_x-1] == RAMP_E):
                #    player_z+=1
                # Going down a West Ramp
                #if (testLevel[player_z-1][player_y][player_x] == RAMP_W):
                #    player_z-=1
                player_x-=1
                print("moved to x:{0}, y:{1}, z:{2}".format(player_x,player_y,player_z))
                
            if (event.key == K_RIGHT) and (player_x < max_x):
                # Going down an East Ramp
                #if (testLevel[player_z-1][player_y][player_x] == RAMP_E):
                #    player_z-=1
                # Going up a West Ramp
                #if (testLevel[player_z][player_y][player_x+1] == RAMP_W):
                #    player_z+=1
                player_x+=1
                print("moved to x:{0}, y:{1}, z:{2}".format(player_x,player_y,player_z))

            if (event.key == K_d):
                sdebug+=1
                if (sdebug==3):
                    sdebug=0

            if (event.key == K_PAGEUP) and (player_z < max_z):
                print("x:{0}, y:{1}, z:{2}".format(player_x,player_y,player_z))
                player_z=player_z + 1

            if (event.key == K_PAGEDOWN) and (player_z > min_z):
                print("x:{0}, y:{1}, z:{2}".format(player_x,player_y,player_z))
                player_z=player_z - 1

            if (event.key == K_COMMA):
                cursorBlock=(cursorBlock-1) % numBlocks
                print("cursorBlock {0}".format(cursorBlock))

            if (event.key == K_PERIOD):
                cursorBlock=(cursorBlock+1) % numBlocks
                print("cursorBlock {0}".format(cursorBlock))

            if (event.key == K_SLASH):
                print("setting x:{0} y:{1} z:{2} to block {3}".format(player_x,player_y,player_z,cursorBlock))
                testLevel[player_z][player_y][player_x] = cursorBlock
            
            #if (event.key >= K_0) and (event.key <= K_9):
            #    keyChar = pygame.key.name(event.key)
            #    testLevel[player_z][player_y][player_x] = int(keyChar)
            #    print("setting x:{0} y:{1} z{2} to {3}".format(player_x,player_y,player_z,keyChar))

            if (event.key == K_0):
                print("test level layer {0} {1}".format(0,testLevel[0]))
            if (event.key == K_1):
                print("test level layer {0} {1}".format(1,testLevel[1]))
            if (event.key == K_2):
                print("test level layer {0} {1}".format(2,testLevel[2]))
            if (event.key == K_3):
                print("test level layer {0} {1}".format(3,testLevel[3]))
            if (event.key == K_4):
                print("test level layer {0} {1}".format(4,testLevel[4]))
            if (event.key == K_5):
                print("test level layer {0} {1}".format(5,testLevel[5]))

            if (event.key == K_s):
                fileName=input('Save file name? ')
                path='levels\\' + fileName
                saveFile=open(path,'wb')
                pickle.dump(testLevel,saveFile)
                pickle.dump(spawn,saveFile)
                pickle.dump(objective,saveFile)
                saveFile.close()
                print("level saved")

            if (event.key == K_w):
                fileName=input('Load file name? ')
                path='levels\\' + fileName
                loadFile=open(path,'rb')
                testLevel=pickle.load(loadFile)
                spawn=pickle.load(loadFile)
                objective=pickle.load(loadFile)
                loadFile.close()

            if (event.key == K_x):
                print("clearing block")
                testLevel[player_z][player_y][player_x] = 0

            #if (event.key == K_c):
            #    print("clearing layer {0}".format(player_z))
            #    testLevel[player_z]=emptyLayer

            if (event.key == K_q):
                print("shifting everything up")
                for n in range (5,0,-1):
                    testLevel[n] = testLevel[n-1]
                testLevel[0]=emptyLayer

            if (event.key == K_a):
                print("shifting everything down")
                for n in range (0,5):
                    testLevel[n] = testLevel[n+1]
                testLevel[5]=emptyLayer

            if (event.key == K_p):
                print("setting player spawn point")
                spawn[0] = player_x
                spawn[1] = player_y
                spawn[2] = player_z

            if (event.key == K_o):
                print("setting player objective point")
                objective[0] = player_x
                objective[1] = player_y
                objective[2] = player_z

            if (event.key == K_f):
                print("filling layer {0} with block {1}".format(player_z,cursorBlock))
                testLevel[player_z]=[
                    [cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock],
                    [cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock],
                    [cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock],                                
                    [cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock],
                    [cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock],
                    [cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock,cursorBlock]
                ]
                
            draw_screen()
    fpsClock.tick(FPS)
    pygame.display.set_caption("FPS {0} x:{1} y:{2} z:{3}".format(int(fpsClock.get_fps()),player_x,player_y,player_z))
    pygame.display.update()
