def getmax(d,maxi):
    (mx,my,mz)=maxi
    for pos in d.values():
    #    print("x:{0} y:{1} z:{2}".format(i.x,i.y,i.z))
         if (pos.x > mx):
             mx = pos.x
         if (pos.y > my):
             my = pos.y
         if (pos.z > mz):
             mz = pos.z
    return (mx,my,mz)
