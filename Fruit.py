from Item import *

class Fruit(Item):
    def __init__(self, animage, xlocation, aspeed, value):
        Item.__init__(self, animage, xlocation, 0, animage.width, animage.height)
        self.speed = aspeed
        self.value = value
    
    def move(self):
        self.ylocation = self.ylocation + self.speed