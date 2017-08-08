class GameManager:
    def __init__(self, bgimage, framerate, player, timer):
        self.backgroundimage = bgimage
        self.framerate = framerate
        self.player = player
        self.timer = timer
        
        self.done = False
        self.scorefont = loadFont("Sansation-Bold-35.vlw");
        self.pointsfont = loadFont("Sansation-Bold-35.vlw");
        self.score = 0
        self.fruitspeed = 7
    
    def playGame(self):
        self.moveFruit()
        self.drawWorld()
        self.checkEnd()
        self.checkCollision()
        self.displayScore()
        self.displaySpeed()

    def drawWorld(self):
        self.player.draw()
        
    def moveFruit(self):
        pass
    
    def checkEnd(self):
        pass
    
    def checkCollision(self):
        pass
        
    def displaySpeed(self):
        fill(255)
        textFont(self.scorefont, 20)
        text("Speed: " + str(self.fruitspeed), 10,31)
    
    def displayScore(self):
        fill(255)
        textFont(self.scorefont, 20)
        text("Score: " + str(self.score), 10,15)