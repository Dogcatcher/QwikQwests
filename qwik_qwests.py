# Weekend Game - Qwik Qwests

import pygame, sys, pickle, numpy as np
from blocks import *
from pygame.locals import *

pygame.init()

FPS=30
fpsClock = pygame.time.Clock()

screenHeight=800
screenWidth=1200

SCREEN=pygame.display.set_mode((screenWidth,screenHeight),0,32)
pygame.display.set_caption('Qwik Qwests')

# load sprites

class Character:
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
    def setkeys(self,up,down,left,right,action):
        self.upkey = up
        self.downkey = down
        self.leftkey = left
        self.rightkey = right
        self.actionkey = action


P1=Character()
P1.setidx(1)
P1.setname('Inky')
P1.setimage(BOY)
P1.setpos(0,0,1)
P1.setkeys(K_UP,K_DOWN,K_LEFT,K_RIGHT,K_RCTRL)


P2=Character()
P2.setidx(2)
P2.setname('Stinky')
P2.setimage(CATGIRL)
P2.setpos(10,10,1)
P2.setkeys(K_w,K_s,K_a,K_d,K_LCTRL)

P3=Character()
P3.setidx(3)
P3.setname('Winky')
P3.setimage(HORNGIRL)
P3.setpos(10,0,1)
P3.setkeys(K_i,K_k,K_j,K_l,K_SPACE)

P4=Character()
P4.setidx(4)
P4.setname('Pinky')
P4.setimage(PINKGIRL)
P4.setpos(0,10,1)
P4.setkeys(K_KP8,K_KP2,K_KP4,K_KP6,K_KP_ENTER)
   
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


spawn=[0,0,0]
objective=[9,5,5]

# load level

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
    
print("Loading level {0} - {1}".format(levelList[level][0],levelList[level][1]))
(testLevel,spawn,objective)=load_level(levelList[level][2])

for player in (P1,P2,P3,P4):
    (player.x,player.y,player.z) = (spawn[player.idx-1][0],spawn[player.idx-1][1],spawn[player.idx-1][2])
##player_x=spawn[0]
##player_y=spawn[1]
##player_z=spawn[2]

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
#playerInv=[None]*10


indexInv=0

def draw_inventory():
    print("Drawing inventory")
    invOffset=120
    for i in range (1,11):
        blockId=playerInv[i-1]
        SCREEN.blit(blockType[blockId], (1050,((i*(20+blockHeight))+invOffset)))
        print("Slot {0} = {1}".format(i,blockId))

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


                for player in (P1,P2,P3,P4):
                    if (player.x,player.y,player.z) == (x,y,z):
                        ramp = 0
                        below=testLevel[z-1][y][x]
                        if (below == RAMP_N) or (below == RAMP_S) or (below == RAMP_E) or (below == RAMP_W):
                            ramp = 10
                        SCREEN.blit(player.image,((x*blockWidth+screenOffsetX),y*blockHeight+offset+ramp))                        

              
##                if (z == player_z) and (x == player_x) and (y == player_y):
##                    # visual adjustment for when player is on a ramp
##                    ramp = 0
##                    below=testLevel[z-1][y][x]
##                    if (below == RAMP_N) or (below == RAMP_S) or (below == RAMP_E) or (below == RAMP_W):
##                        ramp = 10
##                    player=objectType[playerObj]
##                    SCREEN.blit(player, ((x*blockWidth+screenOffsetX),y*blockHeight+offset+ramp))
                    
                if (z == objective[2] ) and (y == objective[1]) and (x == objective[0]):
                    SCREEN.blit(objectType[STAR], ((x*blockWidth+screenOffsetX),y*blockHeight+offset))

    #screen_x=player_x*blockWidth
    #screen_y=(player_y*blockHeight)+(screenOffsetY)-(player_z*blockOffset)
    #s.blit(objectType[playerObj], (screen_x, screen_y))
    draw_inventory()


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
    #SCREEN.blit(objectType[obj], (player_x, player_y+screenOffsetY))
    #render_object(SCREEN,obj,player_x,player_y,player_z)
    
        
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if (event.type == KEYDOWN):
            if (event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            for player in (P1,P2,P3,P4):
                if (event.key == player.upkey) and (canMoveUp(player.x,player.y,player.z) == True):
                    if (testLevel[player.z-1][player.y][player.x] == RAMP_N): # Going down a North Ramp
                        player.z-=1
                    if (testLevel[player.z][player.y-1][player.x] == RAMP_S): # Going up a South Ramp
                        player.z+=1
                    player.y-=1
                    
                if (event.key == player.downkey) and (canMoveDown(player.x,player.y,player.z) == True):
                    if (testLevel[player.z][player.y+1][player.x] == RAMP_N): # Going up a North Ramp
                        player.z+=1
                    if (testLevel[player.z-1][player.y][player.x] == RAMP_S): # Going down a South Ramp
                        player.z-=1
                    player.y+=1

                if (event.key == player.leftkey) and (canMoveLeft(player.x,player.y,player.z) == True):
                    if (testLevel[player.z][player.y][player.x-1] == RAMP_E): # Going up an East Ramp
                        player.z+=1
                    if (testLevel[player.z-1][player.y][player.x] == RAMP_W): # Going down a West Ramp
                        player.z-=1
                    player.x-=1
                    
                if (event.key == player.rightkey) and (canMoveRight(player.x,player.y,player.z) == True):
                    if (testLevel[player.z-1][player.y][player.x] == RAMP_E): # Going down an East Ramp
                        player.z-=1
                    if (testLevel[player.z][player.y][player.x+1] == RAMP_W): # Going up a West Ramp
                        player.z+=1
                    player.x+=1

            #if(event.key == K_RIGHTBRACKET):
                #return True
                #goToNextLevel()
            #if (event.key == K_PAGEUP) and (player_z < max_z) and (canMove(0,0,1,player_x,player_y,player_z) == True):
            #    #print("x:{0}, y:{1}, z:{2}".format(player_x,player_y,player_z))
            #    player_z=player_z + 1

            #if (event.key == K_PAGEDOWN) and (player_z > min_z) and (canMove(0,0,-1,player_x,player_y,player_z) == True):
            #    #print("x:{0}, y:{1}, z:{2}".format(player_x,player_y,player_z))
            #    player_z=player_z - 1

            if (event.key == K_i and object_down(player_x,player_y,player_z)):
                playerInv[indexInv] = testLevel[player_z][player_y+1][player_x]
                testLevel[player_z][player_y+1][player_x] = EMPTY
                indexInv += 1
                

            if (event.key == K_i and object_up(player_x,player_y,player_z)):
                playerInv[indexInv] = testLevel[player_z][player_y-1][player_x]
                testLevel[player_z][player_y-1][player_x] = EMPTY
                indexInv += 1
                    

            if (event.key == K_i and object_left(player_x,player_y,player_z)):
                playerInv[indexInv] = testLevel[player_z][player_y][player_x-1]
                testLevel[player_z][player_y][player_x-1] = EMPTY
                indexInv += 1
                

            if (event.key == K_i and object_right(player_x,player_y,player_z)):
                playerInv[indexInv] = testLevel[player_z][player_y][player_x+1]
                testLevel[player_z][player_y][player_x+1] = EMPTY
                indexInv += 1
                
                
##            if (event.key == K_o and indexInv > 0):
##                indexInv -= 1
##                testLevel[player_z][player_y+1][player_x] = playerInv[indexInv]
##                playerInv[indexInv] = EMPTY
##                draw_inventory()
                
            if (event.key == K_EQUALS):
                level = (level + 1) % len(levelList)
                print("Loading level {0} - {1}".format(levelList[level][0],levelList[level][1]))
                (testLevel,spawn,objective)=load_level(levelList[level][2])
##                player_x=spawn[0]
##                player_y=spawn[1]
##                player_z=spawn[2]
                for player in (P1,P2,P3,P4):
                    (player.x,player.y,player.z) = (spawn[player.idx-1][0],spawn[player.idx-1][1],spawn[player.idx-1][2])                
                max_x=len(testLevel[0][0])
                max_y=len(testLevel[0])
                max_z=len(testLevel)
                print("level is size x:{0} y:{1} z:{2}".format(max_x,max_y,max_z))
                max_x -= 1
                max_y -= 1
                max_z -= 1
                screenOffsetX=0 + ((limit_x - max_x) / 2 * blockWidth)
                screenOffsetY=274 + ((limit_y - max_y) / 2 * blockHeight)
                playerInv=np.zeros(10,dtype=np.int)
##            if (player_x == objective[0]) and (player_y == objective[1]) and (player_z == objective[2]):
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
                
            
            draw_screen()

    pygame.display.flip()
