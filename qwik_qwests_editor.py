# Weekend Game - Qwik Qwests

import pygame, sys, pickle, tkinter, numpy as np
from pygame.locals import *
from blocks import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

pygame.init()

FPS=30
fpsClock = pygame.time.Clock()

cursorBlock=0


BLACK = (0,0,0)
WHITE = (255,255,255)
LIGHTBLUE = (100,150,255)
BROWN = (150,100,50)

titleCenter = QwikQwests.get_rect()
titleCenter.center=(400,50)

min_x=0
min_y=0
min_z=0
max_x=9
max_y=5
max_z=5
limit_x=19
limit_y=11
limit_z=11

testLevel=np.zeros(((max_z+1),(max_y+1),(max_x+1)),dtype=np.int)

emptyLayer=[
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY], 
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY]
            ]

def fill_gradient(surface, color, gradient, rect=None, vertical=True, forward=True):
    return True

blockOffset=20
screenOffset=220
blockWidth=50
blockHeight=40

spawn=[[0,0,3],[10,10,3],[0,10,3],[10,0,3]]
objective=[9,5,5]

spawnPoint=0
player_x=spawn[1][0]
player_y=spawn[1][1]
player_z=spawn[1][2]


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

                        # South (top)
                        if (showS2 == True)  and (z < y + 3 )and (z < max_z) and (y > min_y) and (testLevel[z+1][y][x] == EMPTY) and (testLevel[z][y-1][x] == EMPTY) and (testLevel[z+1][y-1][x] == EMPTY):
                           SCREEN.blit(shadowType[SHADOW_S], ((x*blockWidth),(y*blockHeight+(offset)-blockOffset-tallBlockOffset)))
                    # South (top ceiling)
                    if (showS5 == True)  and (z < y + 3) and (z == max_z) and (y > min_y) and (testLevel[z][y-1][x] == EMPTY):
                       SCREEN.blit(shadowType[SHADOW_S], ((x*blockWidth),(y*blockHeight+(offset)-blockOffset-tallBlockOffset)))                   
                # spawn point
                for a in range (0,4):
                    if (z == spawn[a][2]) and (y == spawn[a][1]) and (x == spawn[a][0]):
                        SCREEN.blit(objectType[BOY+a], ((x*blockWidth),y*blockHeight+offset))                    

                # objective point
                if (z == objective[2]) and (y == objective[1]) and (x == objective[0]):
                    SCREEN.blit(objectType[STAR], ((x*blockWidth),y*blockHeight+offset))                    

                # Cursor 
                if (z == player_z) and (x == player_x) and (y == player_y):
                    if (cursorBlock > 0):
                        SCREEN.blit(blockType[cursorBlock], ((x*blockWidth),y*blockHeight+offset))
                    SCREEN.blit(objectType[SELECTOR], ((x*blockWidth),y*blockHeight+offset-blockOffset))


def canMoveRight(px,py,pz):
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







draw_screen()                
while True:

    
      
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
            
        if (event.type == KEYDOWN):
            if (event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if (event.key == K_UP) and (player_y > min_y):
                player_y-=1
                print("moved to x:{0}, y:{1}, z:{2}".format(player_x,player_y,player_z))
                
            if (event.key == K_DOWN) and (player_y < max_y):
                player_y+=1
                print("moved to x:{0}, y:{1}, z:{2}".format(player_x,player_y,player_z))
                
            if (event.key == K_LEFT) and (player_x > min_x):
                player_x-=1
                print("moved to x:{0}, y:{1}, z:{2}".format(player_x,player_y,player_z))
                
            if (event.key == K_RIGHT) and (player_x < max_x):
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
                if (player_x,player_y,player_z) in Block.instances.keys():
                    print("block already exists in dictionary - removing old block")
                    del Block.instances[(player_x,player_y,player_z)]
                
                print("new block - adding to dictionary")
                newBlock = Block((player_x,player_y,player_z))
                newBlock.setblock(cursorBlock)
                    
                print("These are the blocks ")
                for instance in Block.instances.values():
                    print("pos:{0} blocknum:{1}".format(instance.pos,instance.blocknum))
                
            
            if (event.key == K_1) and (max_x > 0):
                newLevel=np.delete(testLevel,max_x,axis=2)
                testLevel=newLevel
                max_x-=1
                if (player_x > max_x):
                    player_x = max_x
                for a in range (0,4):
                    if (spawn[a][0] > max_x):
                        spawn[a][0] = max_x
                if (objective[0] > max_x):
                    objective[0] = max_x
            if (event.key == K_2) and (max_x < limit_x):
                newLevel=np.append(testLevel,np.zeros(((max_z+1),(max_y+1),1),dtype=np.int),axis=2)
                testLevel=newLevel
                max_x+=1
            if (event.key == K_3) and (max_y > 0):
                newLevel=np.delete(testLevel,max_y,axis=1)
                testLevel=newLevel
                max_y-=1
                if (player_y > max_y):
                    player_y = max_y
                for a in range [0,4]:
                    if (spawn[a][1] > max_y):
                        spawn[a][1] = max_y
                if (objective[1] > max_y):
                    objective[1] = max_y            
            if (event.key == K_4) and (max_y < limit_y):
                newLevel=np.append(testLevel,np.zeros(((max_z+1),1,(max_x+1)),dtype=np.int),axis=1)
                testLevel=newLevel
                max_y+=1
            if (event.key == K_5) and (max_z > 0):
                newLevel=np.delete(testLevel,max_z,axis=0)
                testLevel=newLevel
                max_z-=1
                if (player_z > max_z):
                    player_z = max_z
                for a in range (0,4):
                    if (spawn[a][2] > max_z):
                        spawn[a][2] = max_z
                if (objective[2] > max_z):
                    objective[2] = max_z            
            if (event.key == K_6) and (max_z < limit_z):
                newLevel=np.append(testLevel,np.zeros((1,(max_y+1),(max_x+1)),dtype=np.int),axis=0)
                testLevel=newLevel
                max_z+=1
                
            if (event.key == K_s):
                root=tkinter.Tk()
                root.withdraw()
                fileName = asksaveasfilename(parent=root)
                root.destroy()
                if (fileName):
                    saveFile=open(fileName,'wb')
                    pickle.dump(testLevel,saveFile)
                    pickle.dump(spawn,saveFile)
                    pickle.dump(objective,saveFile)
                    saveFile.close()
                    print("level saved")

            if (event.key == K_w):
                root=tkinter.Tk()
                root.withdraw()
                fileName = askopenfilename(parent=root)
                root.destroy()
                if (fileName):
                    loadFile=open(fileName,'rb')
                    testLevel=pickle.load(loadFile)
                    spawn=pickle.load(loadFile)
                    objective=pickle.load(loadFile)
                    loadFile.close()
                    max_x=len(testLevel[0][0])
                    max_y=len(testLevel[0])
                    max_z=len(testLevel)
                    print("level is size x:{0} y:{1} z:{2}".format(max_x,max_y,max_z))
                    max_x -= 1
                    max_y -= 1
                    max_z -= 1

                    for a in range (0,4):
                        if (spawn[a][0] > max_x):
                            spawn[a][0] = max_x
                        if (spawn[a][1] > max_y):
                            spawn[a][1] = max_y
                        if (spawn[a][2] > max_z):
                            spawn[a][2] = max_z
                    if (player_x > max_x):
                        player_x = max_x                            
                    if (objective[0] > max_x):
                        objective[0] = max_x
                    if (player_y > max_y):
                        player_y = max_y
                    if (objective[1] > max_y):
                        objective[1] = max_y
                    if (player_z > max_z):
                        player_z = max_z
                    if (objective[2] > max_z):
                        objective[2] = max_z                    
            if (event.key == K_x):
                print("clearing block")
                testLevel[player_z][player_y][player_x] = 0

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
                spawn[spawnPoint][0] = player_x
                spawn[spawnPoint][1] = player_y
                spawn[spawnPoint][2] = player_z
                spawnPoint = (spawnPoint + 1) %4

            if (event.key == K_o):
                print("setting player objective point")
                objective[0] = player_x
                objective[1] = player_y
                objective[2] = player_z

            if (event.key == K_f):
                print("filling layer {0} with block {1}".format(player_z,cursorBlock))
                testLevel[player_z]=[[cursorBlock for x in range(max_x+1)]for y in range(max_y+1)]
                
            draw_screen()
    fpsClock.tick(FPS)
    pygame.display.set_caption("FPS {0} x:{1} y:{2} z:{3}".format(int(fpsClock.get_fps()),player_x,player_y,player_z))
    pygame.display.flip()
