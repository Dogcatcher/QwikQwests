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

blockType=[None]*14

GRASSBLOCK=1
STONEBLOCK=2
WATERBLOCK=3
PLAINBLOCK=4

blockType[1]=pygame.image.load('PlanetCute PNG\Grass Block.png')
blockType[2]=pygame.image.load('PlanetCute PNG\Stone Block.png')
blockType[3]=pygame.image.load('PlanetCute PNG\Water Block.png')
blockType[4]=pygame.image.load('PlanetCute PNG\Plain Block.png')
blockType[5]=pygame.image.load('PlanetCute PNG\Dirt Block.png')
blockType[6]=pygame.image.load('PlanetCute PNG\Ramp North.png')
blockType[7]=pygame.image.load('PlanetCute PNG\Ramp South.png')
blockType[8]=pygame.image.load('PlanetCute PNG\Ramp East.png')
blockType[9]=pygame.image.load('PlanetCute PNG\Ramp West.png')
blockType[10]=pygame.image.load('PlanetCute PNG\Wall Block.png')
blockType[11]=pygame.image.load('PlanetCute PNG\Door Tall Closed.png')
blockType[12]=pygame.image.load('PlanetCute PNG\Rock.png')
blockType[13]=pygame.image.load('PlanetCute PNG\Tree Short.png')


objectType=[None]*3



objectType[0]=pygame.image.load('PlanetCute PNG\Character Boy.png')
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
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [5,5,5,5,5,5,5,5]
            ]

testLevel[1]=[
            [0,0,0,0,0,0,0,5],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,2,5,5],
            [0,1,1,1,1,2,5,5]
            ]

testLevel[2]=[
            [2,2,3,3,2,2,2,0],
            [2,0,0,0,0,2,2,6],
            [2,2,3,3,2,2,2,2],
            [1,1,3,3,1,0,0,7],
            [1,1,3,3,1,0,0,0]
            ]

testLevel[3]=[
            [0,0,0,0,0,10,11,0],
            [0,9,2,2,8,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,13,0,0,12,0,0,0],
            ]

testLevel[4]=[
            [0,0,0,0,0,10,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]           
            ]

testLevel[5]=[
            [0,0,0,0,0,10,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]
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
min_z=3
max_x=7
max_y=4
max_z=5

playerObj=0

def draw_screen():
    SCREEN.fill(BLACK)
    gradientRect=pygame.Rect(0,0,800,375)
    fill_gradient(SCREEN,LIGHTBLUE,WHITE,gradientRect,True,True)
    SCREEN.blit(QwikQwests, titleCenter)

    for l in range (0,6):
        offset=(l*-1*blockOffset)+screenOffset
        for x in range (0,5):
            for y in range (0,8):
                block=testLevel[l][x][y]
                if block > 0:
                    image=blockType[block]
                    SCREEN.blit(image, ((y*blockWidth),(x*blockHeight+(offset))))

                if (l == player_z) and (y == player_x) and (x == player_y):
                    # visual adjustment for when player is on a ramp
                    ramp = 0
                    below=testLevel[l-1][x][y]
                    if (below == 6) or (below == 7) or (below == 8) or (below == 9):
                        ramp = 20
                    player=objectType[playerObj]
                    SCREEN.blit(player, ((y*blockWidth),x*blockHeight+(offset)+ramp))

    #screen_x=player_x*blockWidth
    #screen_y=(player_y*blockHeight)+(screenOffset)-(player_z*blockOffset)
    #s.blit(objectType[playerObj], (screen_x, screen_y))


def canMoveRight(px,py,pz):
    #print("px:{0} py:{1} pz:{2} max_x:{3} block:{4}".format(px,py,pz,max_x,testLevel[pz][py][px+1]))
    if (px < max_x):
        print("Not at the far right edge")
        if (testLevel[pz][py][px + 1] == 0) and (testLevel[pz-1][py][px+1] != 3):
            print("Can move right")
            if (testLevel[pz-1][py][px+1] == 0):
                print("But there's a drop")
                print("We're on a {0}".format(testLevel[pz-1][py][px]))
                if (testLevel[pz-1][py][px] == 8):  
                    print("so that's ok because we're on an East ramp")
                    return True
                return False
            return True
        if (testLevel[pz][py][px+1] == 9):
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
        if (testLevel[pz][py][px-1] == 0) and (testLevel[pz-1][py][px-1] != 3):
            print("Can move left")
            if (testLevel[pz-1][py][px-1] == 0):
                print("But there's a drop")
                print("We're on a {0}".format(testLevel[pz-1][py][px]))
                if (testLevel[pz-1][py][px] == 9):  
                    print("so that's ok because we're on an West ramp")
                    return True
                return False
            return True
        if (testLevel[pz][py][px-1] == 8):
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
        if (testLevel[pz][py-1][px] == 0) and (testLevel[pz-1][py-1][px] != 3):
            print("Can move up")
            if (testLevel[pz-1][py-1][px] == 0):
                print("But there's a drop")
                print("We're on a {0}".format(testLevel[pz-1][py][px]))
                if (testLevel[pz-1][py][px] == 6):  
                    print("so that's ok because we're on a North ramp")
                    return True
                return False
            return True
        if (testLevel[pz][py-1][px] == 7):
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
        if (testLevel[pz][py+1][px] == 0) and (testLevel[pz-1][py+1][px] != 3):
            print("Can move down")
            if (testLevel[pz-1][py+1][px] == 0):
                print("But there's a drop")
                print("We're on a {0}".format(testLevel[pz-1][py][px]))
                if (testLevel[pz-1][py][px] == 7):  
                    print("so that's ok because we're on a South ramp")
                    return True
                return False
            return True
        if (testLevel[pz][py+1][px] == 6):
            print("Up onto the North ramp")
            return True
        print("Something in the way")
        return False
    print("At the far bottom edge")
    return False







#obj = 0

#render_object(SCREEN,obj,player_x,player_y,player_z)
                
while True:

    
    #SCREEN.blit(objectType[obj], (player_x, player_y+screenOffset))
    #render_object(SCREEN,obj,player_x,player_y,player_z)
    draw_screen()
        
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if (event.type == KEYDOWN):
            if (event.key == K_UP) and (canMoveUp(player_x,player_y,player_z) == True):
                # Going down a North Ramp
                if (testLevel[player_z-1][player_y][player_x] == 6):
                    player_z-=1
                # Going up a South Ramp
                if (testLevel[player_z][player_y-1][player_x] == 7):
                    player_z+=1
                player_y-=1
                print("moved to x:{0}, y:{1}, z:{2}".format(player_x,player_y,player_z))
                
            if (event.key == K_DOWN) and (canMoveDown(player_x,player_y,player_z) == True):
                # Going up a North Ramp
                if (testLevel[player_z][player_y+1][player_x] == 6):
                    player_z+=1
                # Going down a South Ramp
                if (testLevel[player_z-1][player_y][player_x] == 7):
                    player_z-=1
                player_y+=1
                print("moved to x:{0}, y:{1}, z:{2}".format(player_x,player_y,player_z))

            if (event.key == K_LEFT) and (canMoveLeft(player_x,player_y,player_z) == True):
                # Going up an East Ramp
                if (testLevel[player_z][player_y][player_x-1] == 8):
                    player_z+=1
                # Going down a West Ramp
                if (testLevel[player_z-1][player_y][player_x] == 9):
                    player_z-=1
                player_x-=1
                print("moved to x:{0}, y:{1}, z:{2}".format(player_x,player_y,player_z))
                
            if (event.key == K_RIGHT) and (canMoveRight(player_x,player_y,player_z) == True):
                # Going down an East Ramp
                if (testLevel[player_z-1][player_y][player_x] == 8):
                    player_z-=1
                # Going up a West Ramp
                if (testLevel[player_z][player_y][player_x+1] == 9):
                    player_z+=1
                player_x+=1
                print("moved to x:{0}, y:{1}, z:{2}".format(player_x,player_y,player_z))

            #if (event.key == K_PAGEUP) and (player_z < max_z) and (canMove(0,0,1,player_x,player_y,player_z) == True):
            #    print("x:{0}, y:{1}, z:{2}".format(player_x,player_y,player_z))
            #    player_z=player_z + 1

            #if (event.key == K_PAGEDOWN) and (player_z > min_z) and (canMove(0,0,-1,player_x,player_y,player_z) == True):
            #    print("x:{0}, y:{1}, z:{2}".format(player_x,player_y,player_z))
            #    player_z=player_z - 1

    pygame.display.update()
