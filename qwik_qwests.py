# Weekend Game - Qwik Qwests   

import pygame, sys, pickle, numpy as np
import time
#from blocks import *
from pygame.locals import *

pygame.init()

FPS=30
fpsClock = pygame.time.Clock()

screenHeight=800
screenWidth=1200

iPath='PlanetCuteSmall\\'

SCREEN=pygame.display.set_mode((screenWidth,screenHeight),0,32)
pygame.display.set_caption('Qwik Qwests')
bubble=pygame.image.load(iPath+'Speech Bubble.png')

numBlocks=27
blockType=[None]*numBlocks


EMPTY=0
blockType[EMPTY]=pygame.Surface((50,40))
blockType[EMPTY].fill((0,0,0))
blockType[EMPTY].set_alpha(0)


# ramps
RAMP_N=1
RAMP_S=2
RAMP_E=3
RAMP_W=4
blockType[RAMP_N]=pygame.image.load(iPath+'Ramp North.png') #6
blockType[RAMP_S]=pygame.image.load(iPath+'Ramp South.png') #7
blockType[RAMP_E]=pygame.image.load(iPath+'Ramp East.png') #8
blockType[RAMP_W]=pygame.image.load(iPath+'Ramp West.png') #9

# scenery blocks
GRASSBLOCK=5
STONEBLOCK=6
WOODBLOCK=7
PLAINBLOCK=8
DIRTBLOCK=9
WALLBLOCK=10
DOORTALLC=11
BROWNBLOCK=12
WATERBLOCK=13
blockType[GRASSBLOCK]=pygame.image.load(iPath+'Grass Block.png')
blockType[STONEBLOCK]=pygame.image.load(iPath+'Stone Block.png')
blockType[PLAINBLOCK]=pygame.image.load(iPath+'Plain Block.png')
blockType[DIRTBLOCK]=pygame.image.load(iPath+'Dirt Block.png')
blockType[WALLBLOCK]=pygame.image.load(iPath+'Wall Block.png')
blockType[BROWNBLOCK]=pygame.image.load(iPath+'Brown Block.png')
blockType[WOODBLOCK]=pygame.image.load(iPath+'Wood Block.png')
blockType[WATERBLOCK]=pygame.image.load(iPath+'Water Block.png')
blockType[DOORTALLC]=pygame.image.load(iPath+'Door Tall Closed.png')

# static scenery objects
ROCK=14
TREESHORT=15
TREETALL=16
TREEUGLY=17
blockType[ROCK]=pygame.image.load(iPath+'Rock.png')
blockType[TREESHORT]=pygame.image.load(iPath+'Tree Short.png')
blockType[TREETALL]=pygame.image.load(iPath+'Tree Tall.png')
blockType[TREEUGLY]=pygame.image.load(iPath+'Tree Ugly.png')

# items
BUG=18
GEMBLUE=19
GEMGREEN=20
GEMORANGE=21
KEY=22
HEART=23
CHESTC=24
CHESTL=25
CHESTO=26
blockType[BUG]=pygame.image.load((iPath+'Enemy Bug.png'))
blockType[GEMBLUE]=pygame.image.load((iPath+'Gem Blue.png'))
blockType[GEMGREEN]=pygame.image.load((iPath+'Gem Green.png'))
blockType[GEMORANGE]=pygame.image.load((iPath+'Gem Orange.png'))
blockType[KEY]=pygame.image.load((iPath+'Key.png'))
blockType[HEART]=pygame.image.load((iPath+'Heart.png'))
blockType[CHESTC]=pygame.image.load((iPath+'Chest Closed.png'))
blockType[CHESTL]=pygame.image.load((iPath+'Chest Lid.png'))
blockType[CHESTO]=pygame.image.load((iPath+'Chest Open.png'))

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

shadowType[SHADOW_SE]=pygame.image.load(iPath+'Shadow Top South East.png')
shadowType[SHADOW_S]=pygame.image.load(iPath+'Shadow Top South.png')
shadowType[SHADOW_SW]=pygame.image.load(iPath+'Shadow Top South West.png')
shadowType[SHADOW_E]=pygame.image.load(iPath+'Shadow Top East.png')
shadowType[SHADOW_W]=pygame.image.load(iPath+'Shadow Top West.png')
shadowType[SHADOW_NE]=pygame.image.load(iPath+'Shadow Top North East.png')
shadowType[SHADOW_N]=pygame.image.load(iPath+'Shadow Top North.png')
shadowType[SHADOW_NW]=pygame.image.load(iPath+'Shadow Top North West.png')
shadowType[SHADOW_SIDEW]=pygame.image.load(iPath+'Shadow Side West.png')

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

objectType[SELECTOR]=pygame.image.load(iPath+'Selector.png')
objectType[BOY]=pygame.image.load(iPath+'Character Boy.png').convert_alpha()
objectType[CATGIRL]=pygame.image.load(iPath+'Character Cat Girl.png')
objectType[HORNGIRL]=pygame.image.load(iPath+'Character Horn Girl.png')
objectType[PINKGIRL]=pygame.image.load(iPath+'Character Pink Girl.png')
objectType[PRINCESS]=pygame.image.load(iPath+'Character Princess Girl.png')
objectType[KEY]=pygame.image.load(iPath+'Key.png')
objectType[ENEMYBUG]=pygame.image.load(iPath+'Enemy Bug.png')
objectType[STAR]=pygame.image.load(iPath+'Star.png')

QwikQwests=pygame.image.load('images/QwikQwests.png')

number=[None]*5

number[0]=pygame.image.load('images/zero.png')
number[1]=pygame.image.load('images/one.png')
number[2]=pygame.image.load('images/two.png')
number[3]=pygame.image.load('images/three.png')
number[4]=pygame.image.load('images/four.png')
levelText=pygame.image.load('images/level.png')

class Block:
    # the base class
    def setname(self, name):
        self.name = name
    def setidx(self,idx):
        self.idx = idx
    def setimage(self, image):
        self.image = objectType[image]
    def setpos(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.position=(self.x,self,y,self.z)
    def __init__(self):
        self.static=True

class Object(Block):
    # Objects inherit from blocks but can be moved
    def __init__(self):
        self.static=False
        self.owner=None

class Character(Object):
    # characters inherit from objects but can walk, talk, and grab objects
    def __init__(self):
        self.speaking=False
    def setkeys(self,up,down,left,right,action):
        self.upkey = up
        self.downkey = down
        self.leftkey = left
        self.rightkey = right
        self.actionkey = action
    def initinv(self):
        self.invidx=0
        self.inventory=np.zeros(10,dtype=np.int)
    def speak(self,say,secs):
        self.speaking = True
        self.say = say
        self.saysecs = secs
        self.sayage = time.mktime(time.gmtime())
        
P1=Character()
P1.setidx(1)
P1.setname('Inky')
P1.setimage(BOY)
P1.setpos(0,0,1)
P1.setkeys(K_UP,K_DOWN,K_LEFT,K_RIGHT,K_RCTRL)
P1.initinv()
#P1.speak('hello',5)

P2=Character()
P2.setidx(2)
P2.setname('Stinky')
P2.setimage(CATGIRL)
P2.setpos(10,10,1)
P2.setkeys(K_w,K_s,K_a,K_d,K_LCTRL)
P2.initinv()
#P2.speak('bonjour',5)

P3=Character()
P3.setidx(3)
P3.setname('Winky')
P3.setimage(HORNGIRL)
P3.setpos(10,0,1)
P3.setkeys(K_i,K_k,K_j,K_l,K_SPACE)
P3.initinv()
#P3.speak('hola',5)

P4=Character()
P4.setidx(4)
P4.setname('Pinky')
P4.setimage(PINKGIRL)
P4.setpos(0,10,1)
P4.setkeys(K_KP8,K_KP2,K_KP4,K_KP6,K_KP_ENTER)
P4.initinv()
#P4.speak('guten tag',5)

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

listFH=open('levellist.pkl','rb')
levelList=pickle.load(listFH)
listFH.close()

level=0
playerInv=np.zeros(10,dtype=np.int)

def load_level(p):
    i='levels\\' + p
    FH=open(i,'rb') # add error if doesn't exist
    l=pickle.load(FH)
    s=pickle.load(FH)
    o=pickle.load(FH)
    FH.close()
    playerInv=np.zeros(10,dtype=np.int)
    return(l,s,o)
    
(testLevel,spawn,objective)=load_level(levelList[level][2])

for player in players:
    (player.x,player.y,player.z) = (spawn[player.idx-1][0],spawn[player.idx-1][1],spawn[player.idx-1][2])

min_x=0
min_y=0
min_z=0

max_x=len(testLevel[0][0])
max_y=len(testLevel[0])
max_z=len(testLevel)
max_x -= 1
max_y -= 1
max_z -= 1

screenOffsetX=0 + ((limit_x - max_x) / 2 * blockWidth)
screenOffsetY=274 + ((limit_y - max_y) / 2 * blockHeight)

playerObj=1

indexInv=0

def draw_inventory():
    invOffset=120
    for player in players:
        for i in range (1,11):
            blockId=player.inventory[i-1]
            SCREEN.blit(blockType[blockId], (900+(50*player.idx),((i*(20+blockHeight))+invOffset)))

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
    
    for z in range (0,(max_z+1)):
        offset=(z*-1*blockOffset)+screenOffsetY
        for y in range (0,(max_y+1)):
            for x in range (0,(max_x+1)):
                block=testLevel[z][y][x]
                
                tallBlockOffset=0
                if (block == DOORTALLC):
                    tallBlockoffset=2*blockOffset

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
                    # South (top)
                    if (z < y + 3 )and (z < max_z) and (y > min_y) and (testLevel[z+1][y][x] == EMPTY) and (testLevel[z][y-1][x] == EMPTY) and (testLevel[z+1][y-1][x] == EMPTY):
                       SCREEN.blit(shadowType[SHADOW_S], ((x*blockWidth+screenOffsetX),(y*blockHeight+(offset)-blockOffset-tallBlockOffset)))

                for player in players:
                    if (player.x,player.y,player.z) == (x,y,z):
                        ramp = 0
                        below=testLevel[z-1][y][x]
                        if (below == RAMP_N) or (below == RAMP_S) or (below == RAMP_E) or (below == RAMP_W):
                            ramp = 10
                        SCREEN.blit(player.image,((x*blockWidth+screenOffsetX),y*blockHeight+offset+ramp))
                        if (player.speaking == True):
                            if (time.mktime(time.gmtime()) > (player.sayage + player.saysecs)):
                                player.say=''
                                player.sayage=0
                                player.saysecs=0
                                player.speaking = False
                            else:
                                bubbleText=bubbleFont.render(player.say,1,BLACK)
                                SCREEN.blit(bubble,((x*blockWidth+screenOffsetX+35),y*blockHeight+offset+ramp-30))
                                SCREEN.blit(bubbleText,((x*blockWidth+screenOffsetX+45),y*blockHeight+offset+ramp+15))
                    
                if (z == objective[2] ) and (y == objective[1]) and (x == objective[0]):
                    SCREEN.blit(objectType[STAR], ((x*blockWidth+screenOffsetX),y*blockHeight+offset))

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
                new_x = player.x
                new_y = player.y
                new_z = player.z
                if (event.key == player.upkey) and (canMoveUp(player.x,player.y,player.z) == True):
                    if (testLevel[player.z-1][player.y][player.x] == RAMP_N): # Going down a North Ramp
                        new_z = player.z-1
                    if (testLevel[player.z][player.y-1][player.x] == RAMP_S): # Going up a South Ramp
                        new_z = player.z+1
                    new_y = player.y-1
                    vacant=True
                    for occupied in players:
                        if (occupied != player):
                            if (new_x == occupied.x and new_y == occupied.y and new_z == occupied.z):
                                vacant=False
                    if (vacant == True):
                        player.x = new_x
                        player.y = new_y
                        player.z = new_z
                                
                if (event.key == player.downkey) and (canMoveDown(player.x,player.y,player.z) == True):
                    if (testLevel[player.z][player.y+1][player.x] == RAMP_N): # Going up a North Ramp
                        new_z = player.z+1
                    if (testLevel[player.z-1][player.y][player.x] == RAMP_S): # Going down a South Ramp
                        new_z = player.z-1
                    new_y = player.y+1
                    vacant=True
                    for occupied in players:
                        if (occupied != player):
                            if (new_x == occupied.x and new_y == occupied.y and new_z == occupied.z):
                                vacant=False
                    if (vacant == True):
                        player.x = new_x
                        player.y = new_y
                        player.z = new_z

                if (event.key == player.leftkey) and (canMoveLeft(player.x,player.y,player.z) == True):
                    if (testLevel[player.z][player.y][player.x-1] == RAMP_E): # Going up an East Ramp
                        new_z = player.z+1
                    if (testLevel[player.z-1][player.y][player.x] == RAMP_W): # Going down a West Ramp
                        new_z = player.z-1
                    new_x = player.x-1
                    vacant=True
                    for occupied in players:
                        if (occupied != player):
                            if (new_x == occupied.x and new_y == occupied.y and new_z == occupied.z):
                                vacant=False
                    if (vacant == True):
                        player.x = new_x
                        player.y = new_y
                        player.z = new_z
                        
                if (event.key == player.rightkey) and (canMoveRight(player.x,player.y,player.z) == True):
                    if (testLevel[player.z-1][player.y][player.x] == RAMP_E): # Going down an East Ramp
                        new_z = player.z-1
                    if (testLevel[player.z][player.y][player.x+1] == RAMP_W): # Going up a West Ramp
                        new_z = player.z+1
                    new_x = player.x+1
                    vacant=True
                    for occupied in players:
                        if (occupied != player):
                            if (new_x == occupied.x and new_y == occupied.y and new_z == occupied.z):
                                vacant=False
                    if (vacant == True):
                        player.x = new_x
                        player.y = new_y
                        player.z = new_z
                        
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
