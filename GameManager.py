add_library('sound')

from Fruit import *

class GameManager:
    def __init__(self, bgimage, framerate, player, timer, fruitimage, itemCatchMusicPlayer):
        self.backgroundimage = bgimage
        self.framerate = framerate
        self.player = player
        self.timer = timer
        
        self.done = False
        self.scorefont = loadFont("Sansation-Bold-35.vlw");
        self.pointsfont = loadFont("Sansation-Bold-35.vlw");
        self.score = 0
        self.fruitspeed = 7
        self.time = 0
        self.items = []
        self.pointsValue = 0
        self.pointsx = 0
        self.pointsy = 0
        self.pointsOn = False
        self.pointsFrameCount = 0
        self.gameDurationSeconds = 30
        
        self.fruitimage = fruitimage
        
        self.itemCatchMusicPlayer = itemCatchMusicPlayer
        
        
    
    def playGame(self):
        
        self.difficultyChange()
        self.spawn()
        self.moveFruit()
        self.drawWorld()
        self.checkEnd()
        self.checkCollision()
        self.displayScore()
        self.displaySpeed()
        
        self.time = self.time + 1

    def drawWorld(self):
       
        #draw all the fruits that have been spawned
        for i in range(len(self.items)):
            aFruit = self.items[i]
            aFruit.draw()
            
        #draw the player on the screen
        self.player.draw()
        
    def spawn(self):
        if(self.time == self.framerate / 2):
        
            self.time = 0
            aFruit = Fruit(self.fruitimage, int(random(30,470)), self.fruitspeed, 3)
            
            #CHALLENGE1: Add a new type of fruit
            
            #CHALLENGE2: Add a powerup
            
            self.items.append(aFruit)
        
        
    def moveFruit(self):
        #/**********************************/
  
        #Finish this for loop to make the fruits fall 
        
        #/**********************************/
        
        
        for i in range(len(self.items)):
            #inside the loop
            aFruit = self.items[i]
            aFruit.move()
    
    def checkEnd(self):
        if(self.timer.currentTime() == self.gameDurationSeconds):
            self.done = True
            self.timer.pause()
            
    def difficultyChange(self):
        #Increase the difficulty every 5 seconds
        if(self.timer.currentTime() % 5 == 0 and self.timer.currentTime() != 0 and frameCount % self.framerate == 0 and frameCount != 0):
            self.fruitspeed = self.fruitspeed + 1
        
    def checkCollision(self):
        
        #store items you want removed in this list, never a good idea to modify a list you are iterating over in python
        itemsToRemove = []
        
        for i in range(len(self.items)):
        
            aFruit = self.items[i]
            
            if(self.player.Intersects(aFruit)):
            
                self.score = self.score + aFruit.value
                self.pointsValue = aFruit.value
                self.pointsx = aFruit.xlocation
                self.pointsy = aFruit.ylocation
                
                self.pointsOn = True
                
                itemsToRemove.append(aFruit)
                
                #print("CAUGHT!")
                self.itemCatchMusicPlayer.play()
            
            self.displayPoints(self.pointsValue, self.pointsx, self.pointsy)
        
        #remove caught fruits from the list  
        #TODO: maybe remove fruits that move off screen?
        for i in range(len(itemsToRemove)):
            itemToRemove = itemsToRemove[i]
            self.items.remove(itemToRemove)
            
    def displayPoints(self, value, x, y):
       
        if(self.pointsOn and self.pointsFrameCount < 90):
            textFont(self.pointsfont, 30)
            fill(255)
            text("+" + str(value), x, y)
            self.pointsFrameCount = self.pointsFrameCount + 1
        else:
            self.pointsOn = False
            self.pointsFrameCount = 0
        
    def displaySpeed(self):
        fill(255)
        textFont(self.scorefont, 20)
        text("Speed: " + str(self.fruitspeed), 10,31)
    
    def displayScore(self):
        fill(255)
        textFont(self.scorefont, 20)
        text("Score: " + str(self.score), 10,15)
        
    def displayGameOverMessage(self):
        textFont(self.scorefont, 40)
        text("Good Job!",10,40)
        textFont(self.scorefont,20)
        text("SCORE: " + str(self.score),10,70)