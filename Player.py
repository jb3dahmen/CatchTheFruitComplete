from Item import *

class Player(Item):
    
    def __init__(self, animage, xlocation, ylocation):
        Item.__init__(self, animage, xlocation, ylocation, animage.width, animage.height)
        
    def moveLeft(self):
        #print("Move Left");
        if(self.xlocation - 10 > 0):
            #/**********************************/
            
            #Make the player move to the left
            
            #/**********************************/
            #PUT SOME CODE HERE
            self.xlocation -= 10
    
    def moveRight(self):
        #print("Move Right");
        if(self.xlocation + 10 < width):
        
            #/**********************************/
        
            #make the player move to the right
        
            #/**********************************/
            #PUT SOME CODE HERE
            self.xlocation += 10
        
        
        