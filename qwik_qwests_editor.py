# Weekend Game - Qwik Qwests

import pygame, sys, pickle, tkinter, numpy as np
from pygame.locals import *
from blocks import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import operator
from common import getmax

pygame.init()

FPS=30
fpsClock = pygame.time.Clock()

cursorBlock=1
fileMode=0

layerHide=False

(BLOCK,OBJECT,SPAWN)=(0,1,2)
mode=BLOCK
modetext={BLOCK:('Block',1,17),OBJECT:('Object',18,26),SPAWN:('Spawn',28,32)}
cursorBlock=1

numBlocks=numObjects=numSpawns=0

BLACK = (0,0,0)
WHITE = (255,255,255)
LIGHTBLUE = (100,150,255)
BROWN = (150,100,50)

titleCenter = QwikQwests.get_rect()
titleCenter.center=(400,50)

min_x=0
min_y=0
min_z=0
max_x=5
max_y=5
max_z=5
limit_x=19
limit_y=11
limit_z=11

def fill_gradient(surface, color, gradient, rect=None, vertical=True, forward=True):
    return True

blockOffset=20
screenOffset=220
blockWidth=50
blockHeight=40

spawn=[[0,0,1],[4,4,1],[0,4,1],[4,0,1]]
Objective=[4,4,1]

spawnPoint=0
player_x=spawn[1][0]
player_y=spawn[1][1]
player_z=spawn[1][2]


sdebug=2

gradientRect=pygame.Rect(0,0,screenWidth,375)


SCREEN.blit(QwikQwests, titleCenter)

def cull_blocks():
    # remove block from dictionary which aren't visible
    # do at point of save but ensure only static blocks are considered
    # plan is to have Object blocks which can be moved, picked up etc
    # don't want to leave holes in the world
    return True

def draw_screen():
    SCREEN.fill(WHITE)
    fill_gradient(SCREEN,LIGHTBLUE,WHITE,gradientRect,True,True)

    # Merge Blocks, Objects, Characters, Cursor into one list/dict

    
    renderDict=Cursor.instances.copy()
    renderDict.update(SpawnPoint.instances)
    renderDict.update(Object.instances)
    renderDict.update(Block.instances)
    
    
    for i in sorted(iter(renderDict.keys())):
        b=renderDict[i]
        (x,y,z)=b.pos
        offset=(z*-1*blockOffset)+screenOffset
        # Cursor
        if (z <= player_z) or (layerHide == False):
            if (z == player_z) and (x == player_x) and (y == player_y):
                SCREEN.blit(blockType[cursorBlock], ((x*blockWidth),y*blockHeight+offset))
                SCREEN.blit(blockType[SELECTOR], ((x*blockWidth),y*blockHeight+offset-blockOffset))
            else:

                # Block
                SCREEN.blit(blockType[b.blocknum], ((x*blockWidth),(y*blockHeight+(offset))))
            

draw_screen()                
while True:

    
      
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

        (old_x,old_y,old_z) = (player_x,player_y,player_z)
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
                cursorBlock=cursorBlock-1
                if (cursorBlock < modetext[mode][1]):
                    cursorBlock = modetext[mode][2]
                print("cursorBlock {0}".format(cursorBlock))

            if (event.key == K_PERIOD):
                cursorBlock=cursorBlock+1
                if (cursorBlock > modetext[mode][2]):
                    cursorBlock = modetext[mode][1]
                print("cursorBlock {0}".format(cursorBlock))

            if (event.key == K_m):
                # change mode - block/Object/character
                mode=(mode+1) %3
                cursorBlock=modetext[mode][1]
                
            if (event.key == K_QUOTE):
                if (mode == BLOCK):
                    print("deleting block")
                    if (player_z,player_y,player_x) in Block.instances.keys():
                        del Block.instances[(player_z,player_y,player_x)]
                        numBlocks=len(Block.instances)
                    else:
                        print("no block to delete")
                elif (mode == OBJECT):
                    print("deleting Object")
                    if (player_z,player_y,player_x) in Object.instances.keys():
                        del Object.instances[(player_z,player_y,player_x)]
                        numObjects=len(Object.instances)
                    else:
                        print("no Object to delete")
                elif (mode == SPAWN):
                    print("deleting spawn")
                    if (player_z,player_y,player_x) in SpawnPoint.instances.keys():
                        del SpawnPoint.instances[(player_z,player_y,player_x)]
                        numSpawns=len(SpawnPoint.instances)
##                        print("These are the blocks ")
##                        for instance in SpawnPoint.instances.values():
##                            print("del spawn pos:{0} blocknum:{1}".format(instance.pos,instance.blocknum))
                    else:
                        print("no spawn to delete")
                        
            if (event.key == K_SLASH):

                if (mode == BLOCK):
                
                    print("setting x:{0} y:{1} z:{2} to block {3}".format(player_x,player_y,player_z,cursorBlock))
                    #testLevel[player_z][player_y][player_x] = cursorBlock
                    if (player_z,player_y,player_x) in Block.instances.keys():
                        print("block already exists in dictionary - removing old block")
                        del Block.instances[(player_z,player_y,player_x)]
                    else:
                        print("new block - adding to dictionary")
                        newblock = Block((player_x,player_y,player_z))
                        numBlocks=len(Block.instances)
                        newblock.setblock(cursorBlock)
                            
                elif (mode == OBJECT):
                    print("setting Object")
                    if (player_z,player_y,player_x) in Object.instances.keys():
                        print("Object already exists in dictionary - removing old Object")
                        del Object.instances[(player_z,player_y,player_x)]
                    else:
                        print("new Object - adding to dictionary")
                        newObject = Object((player_x,player_y,player_z))
                        numObjects=len(Object.instances)
                        newObject.setblock(cursorBlock)

                    
                elif (mode == SPAWN):
                    print("setting player spawn point")
                    if (player_z,player_y,player_x) in SpawnPoint.instances.keys():
                        del SpawnPoint.instances[(player_z,player_y,player_x)]
                    else:
                        newspawn=SpawnPoint((player_x,player_y,player_z))
                        numSpawns=len(SpawnPoint.instances)
                        newspawn.setblock(cursorBlock)
                    print("These are the spawnpoints ")
                    for instance in SpawnPoint.instances.values():
                        print("add spawn pos:{0} blocknum:{1}".format(instance.pos,instance.blocknum))
                
                
##                if (cursorBlock != 0):
####                    print("new block - adding to dictionary")
##                    newBlock = Block((player_x,player_y,player_z))
##                    newBlock.setblock(cursorBlock)
                    
##                print("These are the blocks ")
##                for instance in Block.instances.values():
##                    print("pos:{0} blocknum:{1}".format(instance.pos,instance.blocknum))

            if (event.key == K_c):
                # convert 3d array to class instances
                for z in range (0,(max_z+1)):
                    for y in range (0,(max_y+1)):
                        for x in range (0,(max_x+1)):
                            if (z,y,x) in Block.instances.keys():
                                print("block already exists in dictionary - removing old block")
                                del Block.instances[(z,y,x)]                                                       
                            if (testLevel[z][y][x] != 0):
                                print("new block - adding to dictionary")
                                newBlock = Block((x,y,z))
                                newBlock.setblock(testLevel[z][y][x])
                print("These are the blocks ")
                for instance in Block.instances.values():
                    print("pos:{0} blocknum:{1}".format(instance.pos,instance.blocknum))

            if (event.key == K_0):
                fileMode=(fileMode + 1) % 2
                                                        
            if (event.key == K_1) and (max_x > 0):
##                newLevel=np.delete(testLevel,max_x,axis=2)
##                testLevel=newLevel
                max_x-=1
                if (player_x > max_x):
                    player_x = max_x
                for a in range (0,4):
                    if (spawn[a][0] > max_x):
                        spawn[a][0] = max_x
                if (Objective[0] > max_x):
                    Objective[0] = max_x
            if (event.key == K_2) and (max_x < limit_x):
##                newLevel=np.append(testLevel,np.zeros(((max_z+1),(max_y+1),1),dtype=np.int),axis=2)
##                testLevel=newLevel
                max_x+=1
            if (event.key == K_3) and (max_y > 0):
##                newLevel=np.delete(testLevel,max_y,axis=1)
##                testLevel=newLevel
                max_y-=1
                if (player_y > max_y):
                    player_y = max_y
                for a in range [0,4]:
                    if (spawn[a][1] > max_y):
                        spawn[a][1] = max_y
                if (Objective[1] > max_y):
                    Objective[1] = max_y            
            if (event.key == K_4) and (max_y < limit_y):
##                newLevel=np.append(testLevel,np.zeros(((max_z+1),1,(max_x+1)),dtype=np.int),axis=1)
##                testLevel=newLevel
                max_y+=1
            if (event.key == K_5) and (max_z > 0):
##                newLevel=np.delete(testLevel,max_z,axis=0)
##                testLevel=newLevel
                max_z-=1
                if (player_z > max_z):
                    player_z = max_z
                for a in range (0,4):
                    if (spawn[a][2] > max_z):
                        spawn[a][2] = max_z
                if (Objective[2] > max_z):
                    Objective[2] = max_z            
            if (event.key == K_6) and (max_z < limit_z):
##                newLevel=np.append(testLevel,np.zeros((1,(max_y+1),(max_x+1)),dtype=np.int),axis=0)
##                testLevel=newLevel
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
                    pickle.dump(Objective,saveFile)
                    saveFile.close()
                    print("level saved as array")
                    
            if (event.key == K_a):
                root=tkinter.Tk()
                root.withdraw()
                fileName = asksaveasfilename(parent=root)
                root.destroy()
                if (fileName):
                    saveFile=open(fileName,'wb')
                    pickle.dump(Block.instances,saveFile)
                    #saveFile.close()
                    if (fileMode == 1):
                        #fileName2=fileName+'O'
                        #saveFile=open(fileName2,'wb')
                        pickle.dump(Object.instances,saveFile)
                        #saveFile.close()
                        #fileName2=fileName+'S'
                        #saveFile=open(fileName2,'wb')
                        pickle.dump(SpawnPoint.instances,saveFile)
                        #saveFile.close()
                    #pickle.dump(testLevel,saveFile)
                    #pickle.dump(spawn,saveFile)
                    #pickle.dump(Objective,saveFile)
                    saveFile.close()
                    print("level saved as class instance dictionary")
                    
            if (event.key == K_w):
                root=tkinter.Tk()
                root.withdraw()
                fileName = askopenfilename(parent=root)
                root.destroy()
                if (fileName):
                    loadFile=open(fileName,'rb')
                    testLevel=pickle.load(loadFile)
                    spawn=pickle.load(loadFile)
                    Objective=pickle.load(loadFile)
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
                    if (Objective[0] > max_x):
                        Objective[0] = max_x
                    if (player_y > max_y):
                        player_y = max_y
                    if (Objective[1] > max_y):
                        Objective[1] = max_y
                    if (player_z > max_z):
                        player_z = max_z
                    if (Objective[2] > max_z):
                        Objective[2] = max_z
                        
            if (event.key == K_q):
                root=tkinter.Tk()
                root.withdraw()
                fileName = askopenfilename(parent=root)
                root.destroy()
                if (fileName):
                    loadFile=open(fileName,'rb')
                    #testLevel=pickle.load(loadFile)
                    #spawn=pickle.load(loadFile)
                    #Objective=pickle.load(loadFile)
                    Block.instances=pickle.load(loadFile)
                    #loadFile.close()
                    numBlocks=len(Block.instances.keys())
                    if (fileMode == 1):
                        #fileName2=fileName+'O'
                        #loadFile=open(fileName2,'rb')
                        Object.instances=pickle.load(loadFile)
                        #loadFile.close()
                        numObjects=len(Object.instances.keys())
                        #fileName2=fileName+'S'
                        #loadFile=open(fileName2,'rb')
                        SpawnPoint.instances=pickle.load(loadFile)
                        #loadFile.close()
                        numSpawns=len(SpawnPoint.instances.keys())
                    loadFile.close()
                    #max_x=len(testLevel[0][0])
                    #max_y=len(testLevel[0])
                    #max_z=len(testLevel)
                        
                    (max_x,max_y,max_z)=getmax(Block.instances,(0,0,0))
                    (max_x,max_y,max_z)=getmax(Object.instances,(max_x,max_y,max_z))
                    (max_x,max_y,max_z)=getmax(SpawnPoint.instances,(max_x,max_y,max_z))
                    
                    print("level is size x:{0} y:{1} z:{2}".format(max_x,max_y,max_z))
##                    max_x -= 1
##                    max_y -= 1
##                    max_z -= 1

                    for a in range (0,4):
                        if (spawn[a][0] > max_x):
                            spawn[a][0] = max_x
                        if (spawn[a][1] > max_y):
                            spawn[a][1] = max_y
                        if (spawn[a][2] > max_z):
                            spawn[a][2] = max_z
                    if (player_x > max_x):
                        player_x = max_x                            
                    if (Objective[0] > max_x):
                        Objective[0] = max_x
                    if (player_y > max_y):
                        player_y = max_y
                    if (Objective[1] > max_y):
                        Objective[1] = max_y
                    if (player_z > max_z):
                        player_z = max_z
                    if (Objective[2] > max_z):
                        Objective[2] = max_z
                        
##            if (event.key == K_x):
##                print("clearing block")
##                testLevel[player_z][player_y][player_x] = 0
##
##            if (event.key == K_u):
##                print("shifting everything up")
##                for n in range (5,0,-1):
##                    testLevel[n] = testLevel[n-1]
##                testLevel[0]=emptyLayer
##
##            if (event.key == K_d):
##                print("shifting everything down")
##                for n in range (0,5):
##                    testLevel[n] = testLevel[n+1]
##                testLevel[5]=emptyLayer

##            if (event.key == K_p):
##                print("setting player spawn point")
##                if (player_z,player_y,player_x) is SpawnPoint:
##                    del SpawnPoint[(player_z,player_y,player_x)]
##                else:
##                    newspawn=SpawnPoint((player_x,player_y,player_z))
##                    newspawn.setblock(BOY)
                    
##                spawn[spawnPoint][0] = player_x
##                spawn[spawnPoint][1] = player_y
##                spawn[spawnPoint][2] = player_z
##                spawnPoint = (spawnPoint + 1) %4

##            if (event.key == K_o):
##                print("setting player Objective point")
##                Objective[0] = player_x
##                Objective[1] = player_y
##                Objective[2] = player_z

##            if (event.key == K_f):
##                print("filling layer {0} with block {1}".format(player_z,cursorBlock))
##                testLevel[player_z]=[[cursorBlock for x in range(max_x+1)]for y in range(max_y+1)]

            if (event.key == K_l):
                # layerHide toggle
                if (layerHide == True):
                    layerHide = False
                else:
                    layerHide = True
                
            if ((player_x,player_y,player_z) != (old_x,old_y,old_z)):
                if (old_z,old_y,old_x) in Cursor.instances:
                    del Cursor.instances[(old_z,old_y,old_x)]
                newCursor = Cursor((player_x,player_y,player_z),"cursor")
                newCursor.setblock(EMPTY)

                
            draw_screen()
    fpsClock.tick(FPS)
    pygame.display.set_caption("FPS {0} x:{1} y:{2} z:{3} Mode:{4} LayerHide:{5} cursorBlock:{6} fileMode:{7} #Blocks:{8} #Objects{9} #Spawns{10}".format(int(fpsClock.get_fps()),player_x,player_y,player_z,modetext[mode][0],layerHide,cursorBlock,fileMode,numBlocks,numObjects,numSpawns))
    pygame.display.flip()
