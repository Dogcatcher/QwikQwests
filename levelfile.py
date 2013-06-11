
import pickle

numLevels=3
levels=[None]*numLevels

filename='levellist.pkl'

# level number, title, filename, description

levels[0]=[1,"All Along the WatchTower",'watchtower7','open the chest']
levels[1]=[2,"There Must be Some Kinda Way Outta Here",'maze','just escape as quickly as possible']
levels[2]=[3,"When the Levy Breaks",'cavern4','find the gems']


FH=open(filename,'wb')
for l in range(0,numLevels):
    print("Level {0} is called {1} and the filename is {2}".format(levels[l][0],levels[l][1],levels[l][2]))
    pickle.dump(levels,FH)
FH.close()
