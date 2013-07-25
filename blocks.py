import pygame, numpy as np, weakref

numBlocks=36
blockType=[None]*numBlocks


EMPTY=0
blockType[EMPTY]=pygame.Surface((50,40))
blockType[EMPTY].fill((0,0,0))
blockType[EMPTY].set_alpha(0)

iPath='PlanetCuteSmall\\'

screenHeight=800
screenWidth=1200

SCREEN=pygame.display.set_mode((screenWidth,screenHeight),0,32)
bubble=pygame.image.load(iPath+'Speech Bubble.png').convert_alpha()

# ramps
RAMP_N=1
RAMP_S=2
RAMP_E=3
RAMP_W=4
blockType[RAMP_N]=pygame.image.load(iPath+'Ramp North.png').convert_alpha() #6
blockType[RAMP_S]=pygame.image.load(iPath+'Ramp South.png').convert_alpha() #7
blockType[RAMP_E]=pygame.image.load(iPath+'Ramp East.png').convert_alpha() #8
blockType[RAMP_W]=pygame.image.load(iPath+'Ramp West.png').convert_alpha() #9

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
blockType[GRASSBLOCK]=pygame.image.load(iPath+'Grass Block.png').convert_alpha()
blockType[STONEBLOCK]=pygame.image.load(iPath+'Stone Block.png').convert_alpha()
blockType[PLAINBLOCK]=pygame.image.load(iPath+'Plain Block.png').convert_alpha()
blockType[DIRTBLOCK]=pygame.image.load(iPath+'Dirt Block.png').convert_alpha()
blockType[WALLBLOCK]=pygame.image.load(iPath+'Wall Block.png').convert_alpha()
blockType[BROWNBLOCK]=pygame.image.load(iPath+'Brown Block.png').convert_alpha()
blockType[WOODBLOCK]=pygame.image.load(iPath+'Wood Block.png').convert_alpha()
blockType[WATERBLOCK]=pygame.image.load(iPath+'Water Block.png').convert_alpha()
blockType[DOORTALLC]=pygame.image.load(iPath+'Door Tall Closed.png').convert_alpha()

# static scenery Items
ROCK=14
TREESHORT=15
TREETALL=16
TREEUGLY=17
blockType[ROCK]=pygame.image.load(iPath+'Rock.png').convert_alpha()
blockType[TREESHORT]=pygame.image.load(iPath+'Tree Short.png').convert_alpha()
blockType[TREETALL]=pygame.image.load(iPath+'Tree Tall.png').convert_alpha()
blockType[TREEUGLY]=pygame.image.load(iPath+'Tree Ugly.png').convert_alpha()

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
blockType[BUG]=pygame.image.load((iPath+'Enemy Bug.png')).convert_alpha()
blockType[GEMBLUE]=pygame.image.load((iPath+'Gem Blue.png')).convert_alpha()
blockType[GEMGREEN]=pygame.image.load((iPath+'Gem Green.png')).convert_alpha()
blockType[GEMORANGE]=pygame.image.load((iPath+'Gem Orange.png')).convert_alpha()
blockType[KEY]=pygame.image.load((iPath+'Key.png')).convert_alpha()
blockType[HEART]=pygame.image.load((iPath+'Heart.png')).convert_alpha()
blockType[CHESTC]=pygame.image.load((iPath+'Chest Closed.png')).convert_alpha()
blockType[CHESTL]=pygame.image.load((iPath+'Chest Lid.png')).convert_alpha()
blockType[CHESTO]=pygame.image.load((iPath+'Chest Open.png')).convert_alpha()


SELECTOR=27
BOY=28
CATGIRL=29
HORNGIRL=30
PINKGIRL=31
PRINCESS=32
KEY=33
ENEMYBUG=34
STAR=35
blockType[SELECTOR]=pygame.image.load(iPath+'Selector.png')
blockType[BOY]=pygame.image.load(iPath+'Character Boy.png').convert_alpha()
blockType[CATGIRL]=pygame.image.load(iPath+'Character Cat Girl.png').convert_alpha()
blockType[HORNGIRL]=pygame.image.load(iPath+'Character Horn Girl.png').convert_alpha()
blockType[PINKGIRL]=pygame.image.load(iPath+'Character Pink Girl.png').convert_alpha()
blockType[PRINCESS]=pygame.image.load(iPath+'Character Princess Girl.png').convert_alpha()
blockType[KEY]=pygame.image.load(iPath+'Key.png').convert_alpha()
blockType[ENEMYBUG]=pygame.image.load(iPath+'Enemy Bug.png').convert_alpha()
blockType[STAR]=pygame.image.load(iPath+'Star.png').convert_alpha()

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

shadowType[SHADOW_SE]=pygame.image.load(iPath+'Shadow Top South East.png').convert_alpha()
shadowType[SHADOW_S]=pygame.image.load(iPath+'Shadow Top South.png').convert_alpha()
shadowType[SHADOW_SW]=pygame.image.load(iPath+'Shadow Top South West.png').convert_alpha()
shadowType[SHADOW_E]=pygame.image.load(iPath+'Shadow Top East.png').convert_alpha()
shadowType[SHADOW_W]=pygame.image.load(iPath+'Shadow Top West.png').convert_alpha()
shadowType[SHADOW_NE]=pygame.image.load(iPath+'Shadow Top North East.png').convert_alpha()
shadowType[SHADOW_N]=pygame.image.load(iPath+'Shadow Top North.png').convert_alpha()
shadowType[SHADOW_NW]=pygame.image.load(iPath+'Shadow Top North West.png').convert_alpha()
shadowType[SHADOW_SIDEW]=pygame.image.load(iPath+'Shadow Side West.png').convert_alpha()

##numItems=9
##ItemType=[None]*numItems
##SELECTOR=0
##BOY=1
##CATGIRL=2
##HORNGIRL=3
##PINKGIRL=4
##PRINCESS=5
##KEY=6
##ENEMYBUG=7
##STAR=8
##
##ItemType[SELECTOR]=pygame.image.load(iPath+'Selector.png')
##ItemType[BOY]=pygame.image.load(iPath+'Character Boy.png').convert_alpha()
##ItemType[CATGIRL]=pygame.image.load(iPath+'Character Cat Girl.png').convert_alpha()
##ItemType[HORNGIRL]=pygame.image.load(iPath+'Character Horn Girl.png').convert_alpha()
##ItemType[PINKGIRL]=pygame.image.load(iPath+'Character Pink Girl.png').convert_alpha()
##ItemType[PRINCESS]=pygame.image.load(iPath+'Character Princess Girl.png').convert_alpha()
##ItemType[KEY]=pygame.image.load(iPath+'Key.png').convert_alpha()
##ItemType[ENEMYBUG]=pygame.image.load(iPath+'Enemy Bug.png').convert_alpha()
##ItemType[STAR]=pygame.image.load(iPath+'Star.png').convert_alpha()

QwikQwests=pygame.image.load('images/QwikQwests.png').convert_alpha()

number=[None]*5

number[0]=pygame.image.load('images/zero.png').convert_alpha()
number[1]=pygame.image.load('images/one.png').convert_alpha()
number[2]=pygame.image.load('images/two.png').convert_alpha()
number[3]=pygame.image.load('images/three.png').convert_alpha()
number[4]=pygame.image.load('images/four.png').convert_alpha()
levelText=pygame.image.load('images/level.png').convert_alpha()

class Block:
    # the base class
    def setidx(self,idx):
        self.idx = idx
    def setblock(self, block):
        self.blocknum = block
    def setpos(self,pos):
        (x,y,z) = pos
        self.pos = (x,y,z)
        self.x = x
        self.y = y
        self.z = z
    instances = {}
    def __init__(self, pos, name=None):
        #print("new Block instance")
        self.pos = pos
        (x,y,z) = pos
        self.x = x
        self.y = y
        self.z = z
        self.name = name
        poskey=(z,y,x)
        self.__class__.instances.update({poskey : self})
        
    speaking = False
    static=True

class Cursor(Block):
    name="cursor"
    instances = {}
    def __init__(self, pos, name=None):
        print("new Cursor instance")
        self.pos = pos
        (x,y,z) = pos
        self.x = x
        self.y = y
        self.z = z
        self.name = name
        poskey=(z,y,x)
        self.__class__.instances.update({poskey : self})
    #blocknum = SELECTOR

#class Shadow(Block):

class SpawnPoint(Block):
    name="spawnpoint"
    instances = {}
    def __init__(self, pos, name=None):
        print("new SpawnPoint instance")
        self.pos = pos
        (x,y,z) = pos
        self.x = x
        self.y = y
        self.z = z
        self.name = name
        poskey=(z,y,x)
        self.__class__.instances.update({poskey : self})

class Object(Block):
    # Items inherit from blocks but can be moved
    name="Object"
    instances = {}
    def __init__(self, pos, name=None):
        print("new Object instance")
        self.pos = pos
        (x,y,z) = pos
        self.x = x
        self.y = y
        self.z = z
        self.name = name
        poskey=(z,y,x)
        self.__class__.instances.update({poskey : self})
    
class Character(Block):
    # characters inherit from Items but can walk, talk, and grab Items
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
    static=False
    instances={}
    def __init__(self, pos, name=None):
        print("new Character instance")
        self.pos = pos
        (x,y,z) = pos
        self.x = x
        self.y = y
        self.z = z
        self.name = name
        poskey=(z,y,x)
        self.__class__.instances.update({poskey : self})
