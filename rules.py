class Rule:
    ruleid=0
    instances={}
    def __init__(self,name):
        self.name=name
        self.id=Rule.ruleid
        Rule.ruleid+=1
        self.__class__.instances.update({self.id : self})
        
    def settype(self,ruletype):
        self.ruletype=ruletype

    ##    p (c,(x,y,z)) - player c must be at position
    ##    n (c,object) - player c must be next to object (to pick it up or use it)
    ##    i (c, object) - player c must have object in inventory
    ##    g(c, object) - player c gets object
    ##    u(c,object) - player uses object
    ##    c(object1, object2) - change object1 to object2 - example - open a chest

    def setpos(self,pos):
        self.pos=pos

    def setobj1(self,obj1):
        self.obj1=obj1

    def setobj2(self,obj2):
        self.obj2=obj2

    def setlink(self,linkid):
        self.link=linkid

R1=Rule('Rule1')
R1.settype('p')
R1.setpos((1,2,3))

R2=Rule('Rule2')
R2.settype('p')
R2.setpos((5,6,7))

for r in Rule.instances.values():   
    print(r.id,r.name,r.pos)
