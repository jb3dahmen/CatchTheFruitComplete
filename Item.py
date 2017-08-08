class Item:
    
    def __init__(self, animage, xlocation, ylocation, mywidth, myheight):
        self.myimage = animage
        self.xlocation = xlocation
        self.ylocation = ylocation
        self.mywidth = mywidth
        self.myheight = myheight
        
    def draw(self):
        image(self.myimage, self.xlocation, self.ylocation)
        
    #This is where we can check if two items have collided or intersected
    def Intersects(anitem):
        itemwidth = anitem.mywidth
        itemheight = anitem.myheight
        itemxloc = anitem.xlocation
        itemyloc = anitem.ylocation
    
        if(itemxloc < self.xlocation + self.mywidth and 
        itemxloc + itemwidth > self.xlocation and 
        itemyloc < self.ylocation + self.myheight and 
        itemheight + itemyloc > self.ylocation):
            return True
    
        return False