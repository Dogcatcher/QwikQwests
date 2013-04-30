# Weekend Game - Qwik Qwests

import pygame, sys
from pygame.locals import *

pygame.init()

FPS=60
fpsClock = pygame.time.Clock()

screenHeight=800
screenWidth=800

SCREEN=pygame.display.set_mode((screenWidth,screenHeight),0,32)
pygame.display.set_caption('Qwik Qwests')

# load sprites

blockType=[None]*16

EMPTY=0

RAMP_N=1
RAMP_S=2
RAMP_E=3
RAMP_W=4

GRASSBLOCK=5
STONEBLOCK=6
WATERBLOCK=7
PLAINBLOCK=8
DIRTBLOCK=9
WALLBLOCK=10
DOORTALLC=11
BROWNBLOCK=12
WOODBLOCK=13

# ramps
blockType[RAMP_N]=pygame.image.load('PlanetCute PNG\Ramp North.png') #6
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

# objects
blockType[ROCK]=pygame.image.load('PlanetCute PNG\Rock.png')
blockType[TREESHORT]=pygame.image.load('PlanetCute PNG\Tree Short.png')

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

objectType=[None]*3

objectType[0]=pygame.image.load('PlanetCute PNG\Character Boy.png')
#objectType[0]=pygame.image.load('PlanetCute PNG\Character Cat Girl.png')
#objectType[0]=pygame.image.load('PlanetCute PNG\Character Horn Girl.png')
#objectType[0]=pygame.image.load('PlanetCute PNG\Character Pink Girl.png')
#objectType[0]=pygame.image.load('PlanetCute PNG\Character Princess Girl.png')
objectType[1]=pygame.image.load('PlanetCute PNG\Key.png')
objectType[2]=pygame.image.load('PlanetCute PNG\Enemy Bug.png')


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

testLevel[0]=[
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [DIRTBLOCK,DIRTBLOCK,DIRTBLOCK,DIRTBLOCK,DIRTBLOCK,DIRTBLOCK,DIRTBLOCK,DIRTBLOCK]
            ]

testLevel[1]=[
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,DIRTBLOCK],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,BROWNBLOCK],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,STONEBLOCK,STONEBLOCK,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,STONEBLOCK,STONEBLOCK,STONEBLOCK],
            [GRASSBLOCK,GRASSBLOCK,GRASSBLOCK,GRASSBLOCK,GRASSBLOCK,STONEBLOCK,STONEBLOCK,STONEBLOCK]
            ]

testLevel[2]=[
            [STONEBLOCK,STONEBLOCK,WATERBLOCK,WATERBLOCK,STONEBLOCK,STONEBLOCK,STONEBLOCK,STONEBLOCK],
            [STONEBLOCK,EMPTY,EMPTY,EMPTY,EMPTY,STONEBLOCK,STONEBLOCK,BROWNBLOCK],
            [STONEBLOCK,STONEBLOCK,WATERBLOCK,WATERBLOCK,STONEBLOCK,EMPTY,EMPTY,EMPTY],
            [GRASSBLOCK,GRASSBLOCK,WATERBLOCK,WATERBLOCK,GRASSBLOCK,EMPTY,EMPTY,EMPTY],
            [GRASSBLOCK,GRASSBLOCK,WATERBLOCK,WATERBLOCK,GRASSBLOCK,STONEBLOCK,EMPTY,EMPTY]
            ]

testLevel[3]=[
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,WALLBLOCK,EMPTY,EMPTY],
            [EMPTY,RAMP_W,STONEBLOCK,STONEBLOCK,RAMP_E,EMPTY,EMPTY,BROWNBLOCK],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,TREESHORT,EMPTY,EMPTY,ROCK,EMPTY,EMPTY,EMPTY],
            ]

testLevel[4]=[
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,WALLBLOCK,EMPTY,EMPTY], 
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY]
            ]

testLevel[5]=[
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,WALLBLOCK,EMPTY,EMPTY], 
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY]
            ]
       
#def render (s,l,x,y):
    # s=surface l=3d level array, x=x, y=y
    # pass 3d array into function
    

    #s.blit

def fill_gradient(surface, color, gradient, rect=None, vertical=True, forward=True):
    """fill a surface with a gradient pattern
    Parameters:
    color -> starting color
    gradient -> final color
    rect -> area to fill; default is surface's rect
    vertical -> True=vertical; False=horizontal
    forward -> True=forward; False=reverse
    
    Pygame recipe: http://www.pygame.org/wiki/GradientCode
    """
    if rect is None: rect = surface.get_rect()
    x1,x2 = rect.left, rect.right
    y1,y2 = rect.top, rect.bottom
    if vertical: h = y2-y1
    else:        h = x2-x1
    if forward: a, b = color, gradient
    else:       b, a = color, gradient
    rate = (
        float(b[0]-a[0])/h,
        float(b[1]-a[1])/h,
        float(b[2]-a[2])/h
    )
    fn_line = pygame.draw.line
    if vertical:
        for line in range(y1,y2):
            color = (
                min(max(a[0]+(rate[0]*(line-y1)),0),255),
                min(max(a[1]+(rate[1]*(line-y1)),0),255),
                min(max(a[2]+(rate[2]*(line-y1)),0),255)
            )
            fn_line(surface, color, (x1,line), (x2,line))
    else:
        for col in range(x1,x2):
            color = (
                min(max(a[0]+(rate[0]*(col-x1)),0),255),
                min(max(a[1]+(rate[1]*(col-x1)),0),255),
                min(max(a[2]+(rate[2]*(col-x1)),0),255)
            )
            fn_line(surface, color, (col,y1), (col,y2))

blockOffset=40
screenOffset=310
blockWidth=100
blockHeight=80

player_x=0
player_y=0
player_z=3

min_x=0
min_y=0
min_z=0
max_x=7
max_y=4
max_z=5

playerObj=0
sdebug=0

gradientRect=pygame.Rect(0,0,800,375)


SCREEN.blit(QwikQwests, titleCenter)

def draw_screen():
    SCREEN.fill(WHITE)
    fill_gradient(SCREEN,LIGHTBLUE,WHITE,gradientRect,True,True)
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
                
                if (block > 0):

                    
                    paintBlock=0
                    if (sdebug==1):
                        paintBlock=PLAINBLOCK
                    if (sdebug==2):
                        paintBlock=block

                    if (sdebug > 0):
                        image=blockType[paintBlock]                   
                        SCREEN.blit(image, ((x*blockWidth),(y*blockHeight+(offset))))

                    showSE=False
                    showS=False
                    showSW=False
                    showE=False
                    showW=False
                    showNE=False
                    showN=False
                    showNW=False
                    showSIDEW=False
                    showS2=True
                    showS5=False

                    # shadow processing
                    if (z < max_z) and (testLevel[z+1][y][x] == 0) and (RAMP_W < block < ROCK):
                        # South East
                        if (showSE == True) and (z < max_z) and (y < max_y) and (x < max_x) and (RAMP_W < testLevel[z+1][y+1][x+1] < ROCK) and (testLevel[z+1][y][x+1] == EMPTY) and (testLevel[z+1][y+1][x] == EMPTY):
                           SCREEN.blit(shadowType[SHADOW_SE], ((x*blockWidth),(y*blockHeight+(offset))))
                           print("Placing SE shadow at {0},{1},{2}".format(x,y,z))
                        # South
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
                        if (showS2 == True)  and (z < max_z) and (y > min_y) and (testLevel[z+1][y][x] == EMPTY) and (testLevel[z][y-1][x] == EMPTY) and (testLevel[z+1][y-1][x] == EMPTY):
                           SCREEN.blit(shadowType[SHADOW_S], ((x*blockWidth),(y*blockHeight+(offset)-blockOffset-tallBlockOffset)))
                        # South (top ceiling)
                        if (showS5 == True)  and (z == max_z) and (y > min_y) and (testLevel[z][y-1][x] == EMPTY):
                           SCREEN.blit(shadowType[SHADOW_S], ((x*blockWidth),(y*blockHeight+(offset)-blockOffset-tallBlockOffset)))                   
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
            if (event.key == K_UP) and (canMoveUp(player_x,player_y,player_z) == True):
                # Going down a North Ramp
                if (testLevel[player_z-1][player_y][player_x] == RAMP_N):
                    player_z-=1
                # Going up a South Ramp
                if (testLevel[player_z][player_y-1][player_x] == RAMP_S):
                    player_z+=1
                player_y-=1
                print("moved to x:{0}, y:{1}, z:{2}".format(player_x,player_y,player_z))
                
            if (event.key == K_DOWN) and (canMoveDown(player_x,player_y,player_z) == True):
                # Going up a North Ramp
                if (testLevel[player_z][player_y+1][player_x] == RAMP_N):
                    player_z+=1
                # Going down a South Ramp
                if (testLevel[player_z-1][player_y][player_x] == RAMP_S):
                    player_z-=1
                player_y+=1
                print("moved to x:{0}, y:{1}, z:{2}".format(player_x,player_y,player_z))
                
            if (event.key == K_LEFT) and (canMoveLeft(player_x,player_y,player_z) == True):
                # Going up an East Ramp
                if (testLevel[player_z][player_y][player_x-1] == RAMP_E):
                    player_z+=1
                # Going down a West Ramp
                if (testLevel[player_z-1][player_y][player_x] == RAMP_W):
                    player_z-=1
                player_x-=1
                print("moved to x:{0}, y:{1}, z:{2}".format(player_x,player_y,player_z))
                
            if (event.key == K_RIGHT) and (canMoveRight(player_x,player_y,player_z) == True):
                # Going down an East Ramp
                if (testLevel[player_z-1][player_y][player_x] == RAMP_E):
                    player_z-=1
                # Going up a West Ramp
                if (testLevel[player_z][player_y][player_x+1] == RAMP_W):
                    player_z+=1
                player_x+=1
                print("moved to x:{0}, y:{1}, z:{2}".format(player_x,player_y,player_z))

            if (event.key == K_d):
                sdebug+=1
                if (sdebug==3):
                    sdebug=0

            #if (event.key == K_PAGEUP) and (player_z < max_z) and (canMove(0,0,1,player_x,player_y,player_z) == True):
            #    print("x:{0}, y:{1}, z:{2}".format(player_x,player_y,player_z))
            #    player_z=player_z + 1

            #if (event.key == K_PAGEDOWN) and (player_z > min_z) and (canMove(0,0,-1,player_x,player_y,player_z) == True):
            #    print("x:{0}, y:{1}, z:{2}".format(player_x,player_y,player_z))
            #    player_z=player_z - 1
            draw_screen()
    fpsClock.tick(FPS)
    pygame.display.set_caption("FPS {0}".format(fpsClock.get_fps()))
    pygame.display.update()
