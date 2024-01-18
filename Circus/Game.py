import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Screens import StartScene
from Dialogue import DialogueScene
from Keyboard import Keyboard
from Player import Player
from Clock import Clock
from PlayerSprites import PlayerSprites
from EnemyVentrilo import EnemyVentrilo
from FightScene import FightScene
from Vector import Vector
from FightScene2 import FightScene2
from EnemyAerialists import EnemyAerialists
from Screens import EndingScreen
from Screens import DeathScreen
import os

class Game:
    def __init__(self, canvasWidth, canvasHeight, frame):
        self.frame = frame

        self.canvasWidth = canvasWidth
        self.canvasHeight = canvasHeight

        self.startWindow = StartScene(canvasWidth, canvasHeight, frame)

        self.currentScene = 0

        self.currentGameObject = self.startWindow 

        #for the start window initialisation
        self.name = None

        #for the dialogue scene initialisation
        self.startDialogue = False
        self.dialogueScene = None
        self.keyboard = Keyboard()

        #for Fight Scene 1 initialisation
        self.player = None
        self.clock = Clock()
        self.playerSprites = None
        self.enemyVentrilo = None
        self.fightScene1 = None

        #for Fight Scene 2 initialisation
        self.enemyAerialists = None
        self.fightScene2 = None
        
        #for the Death window initialisation
        self.deathWindow = None
        self.createDeathScreen = False

        #for the Victory window initialisation
        self.victoryWindow = None
        self.createVictoryScreen = False

    
    def draw(self, canvas): #checking if the scene needs to change, then updating the current object
        self.update(canvas)
        self.currentGameObject.draw(canvas)
        
    def update(self, canvas):
        if self.currentScene == 0: #running the start window and waiting to move on 
            if self.startDialogue == True:
                if (self.name  != None): #preparing the dialogue scene with a name from the user 
                    self.dialogueScene = DialogueScene(self.keyboard, self.canvasWidth, self.canvasHeight, self.frame, self.name) #initialising the dialogue scene
                    self.currentGameObject = self.dialogueScene #setting the new current game object
                    self.currentScene += 1
                else: #preparing the dialogue scene without a name from the user 
                    self.dialogueScene = DialogueScene(self.keyboard, self.canvasWidth, self.canvasHeight, self.frame)
                    self.currentGameObject = self.dialogueScene
                    self.currentScene += 1
            else:
                gameValues = self.currentGameObject.startGame()
                self.startDialogue = gameValues[0] #checking if the game should be started
                self.name = gameValues[1] #checking if a name has been entered by the user
        elif self.currentScene == 1: #running the dialogue scene and waiting to move on 
            if self.dialogueScene.finished == True: #preparing the first fight scene
                self.player = Player((Vector(self.canvasWidth/2,self.canvasHeight/2)), self.canvasWidth, self.canvasHeight, self.clock)
                self.playerSprites = PlayerSprites(self.player, self.clock)
                self.enemyVentrilo = EnemyVentrilo(self.canvasWidth, self.canvasHeight, self.player, self.clock)
                self.fightScene1 = FightScene(self.player, self.clock, self.playerSprites, self.keyboard, self.canvasWidth, self.enemyVentrilo, self.frame)
                self.currentGameObject = self.fightScene1 #setting the new current game object
                self.currentScene +=1
        elif(self.currentScene == 2): #running fight scene 1 and waiting to move on 
            if(self.fightScene1.finished == True): 
                if(self.fightScene1.playerDead == True): #preparing the death window
                    self.deathWindow = DeathScreen(self.player.points, self.canvasWidth, self.canvasHeight, self.frame)
                    self.currentGameObject = self.deathWindow #setting the new current game object
                    self.currentScene =  4
                else: #preparing the second fight scene
                    self.enemyAerialists = EnemyAerialists(self.canvasWidth, self.canvasHeight, self.player, self.clock)
                    self.fightScene2 = FightScene2(self.player, self.enemyAerialists, self.clock, self.playerSprites, self.keyboard, self.canvasWidth, self.player.points, self.frame)
                    self.currentGameObject = self.fightScene2 #setting the new current game object
                    self.currentScene += 1
            else: #updating the first fight scene
                self.fightScene1.update(canvas)
                self.player.update(self.enemyVentrilo)
                self.player.draw(canvas)
                self.playerSprites.draw(canvas)
                self.enemyVentrilo.update()
                self.enemyVentrilo.draw(canvas)
        elif(self.currentScene == 3): #running fight scene 2 and waiting to move on 
            if(self.fightScene2.finished == True):
                if(self.fightScene2.playerDead == True): #preparing the death window
                    self.deathWindow = DeathScreen(self.player.points, self.canvasWidth, self.canvasHeight, self.frame)
                    self.currentGameObject = self.deathWindow #setting the new current game object
                    self.currentScene +=  1
                else: #preparing the victory window
                    self.victoryWindow = EndingScreen(self.player.points, self.canvasWidth, self.canvasHeight, self.frame)
                    self.currentGameObject = self.victoryWindow #setting the new current game object
                    self.currentScene = 5
            else: #updating the second fighting scene
                self.enemyAerialists.setBackground(canvas)
                self.fightScene2.update(canvas)
                self.player.update(self.enemyAerialists)
                self.player.draw(canvas)
                self.playerSprites.draw(canvas)
                if(self.player.isDead() or self.enemyAerialists.isDead()):
                    self.fightScene2.timer.stop()
        elif(self.currentScene == 4): #running the death window and waiting to either restart the game loop or close the game
            if(self.deathWindow.startGame() == True):
                self.currentScene = 1 #restarting the game loop
            elif(self.deathWindow.closeGame() == True):
                os._exit(1) #closing the game
        elif(self.currentScene == 5): #running the victory window and waiting to either restart the game loop or close the game
            if(self.victoryWindow.startGame() == True):
                self.currentScene = 1 #restarting the game loop
            elif(self.victoryWindow.closeGame() == True):
                os._exit(1) #closing the game

#setting up the game scene
canvasWidth = 1000
canvasHeight = 616

frame = simplegui.create_frame("Start - Circus", canvasWidth, canvasHeight)

gameCircus = Game(canvasWidth, canvasHeight, frame) 

frame.set_draw_handler(gameCircus.draw)

frame.start()