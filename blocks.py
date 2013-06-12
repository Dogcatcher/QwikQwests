import pygame

numBlocks=27
blockType=[None]*numBlocks

EMPTY=0
iPath='PlanetCuteSmall\\'

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
objectType[BOY]=pygame.image.load(iPath+'Character Boy.png')
objectType[CATGIRL]=pygame.image.load(iPath+'Character Cat Girl.png')
objectType[HORNGIRL]=pygame.image.load(iPath+'Character Horn Girl.png')
objectType[PINKGIRL]=pygame.image.load(iPath+'Character Pink Girl.png')
objectType[PRINCESS]=pygame.image.load(iPath+'Character Princess Girl.png')
objectType[KEY]=pygame.image.load(iPath+'Key.png')
objectType[ENEMYBUG]=pygame.image.load(iPath+'Enemy Bug.png')
objectType[STAR]=pygame.image.load(iPath+'Star.png')

QwikQwests=pygame.image.load('images/QwikQwests.png')

number=[None]*4

number[0]=pygame.image.load('images/zero.png')
number[1]=pygame.image.load('images/one.png')
number[2]=pygame.image.load('images/two.png')
number[3]=pygame.image.load('images/three.png')
levelText=pygame.image.load('images/level.png')
