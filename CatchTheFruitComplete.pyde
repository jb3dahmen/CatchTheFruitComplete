#OpenProcessing Tweak of *@*http://www.openprocessing.org/sketch/112419*@*
#!do not delete the line above, required for linking your tweak if you upload again

#import processing libraries
add_library('sound')

#import user defined classes
from GameManager import *
from Player import *
from Timer import *

def setup():
    global gameManager
    
    size(640,380)
    
    playerimage = loadImage("playerimages/Luma.png")
    backgroundimage = loadImage("backgroundimages/spacebg.png")
    fruitimage = loadImage("fruitimages/starfruit.png")
    
    framerate = 30
    
    fruitimage.resize(50,50)
    playerimage.resize(100,100)
    player = Player(playerimage, width/2, height - 100)
    gametimer = Timer(width - 200,60)
   
    gameManager = GameManager(backgroundimage, framerate, player, gametimer)
    
    gameManager.timer.start()
    

    sf = SoundFile(this,"backgroundmusic/Hyperbola.mp3")
    sf.play()

def keyPressed():
    if (key == CODED):
       
       #/**********************************/
       
       #finish this conditional statement to make the player move left and right
       
       #/**********************************/
       
       if(keyCode == LEFT):
         gameManager.player.moveLeft()
       
       if(keyCode == RIGHT):
         gameManager.player.moveRight()

def draw():
    background(gameManager.backgroundimage)
    frameRate(gameManager.framerate)
    
    gameDurationSeconds = 30
    gameManager.timer.DisplayTime(gameDurationSeconds)
    
    if(not gameManager.done):
        gameManager.playGame()

    
       
    
  
    

    