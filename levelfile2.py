
import pickle

numLevels=1
levels=[None]*numLevels

filename='levellist.pkl'

# level number, title, filename, description

levels[0]=[1,"first level",'level001','open the box']

##levels[0]=[1,"Slope Test",'slopetest3','up and down']
##levels[1]=[2,"All Along the WatchTower",'watchtower8','open the chest']
##levels[2]=[3,"There Must be Some Kinda Way Outta Here",'maze2','just escape as quickly as possible']
##levels[1]=[2,"When the Levy Breaks",'cavern10','find the gems']


FH=open(filename,'wb')
for l in range(0,numLevels):
    print("Level {0} is called {1} and the filename is {2}".format(levels[l][0],levels[l][1],levels[l][2]))
    pickle.dump(levels,FH)
FH.close()
