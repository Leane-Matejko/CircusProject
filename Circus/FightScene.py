import random
from Vector import Vector

canvasWidth = 1000
canvasHeight = 616

class FightScene:
    def __init__(self, player, clock, playerSprites, keyboard, canvasWidth, enemyVentrilo,frame):
        #declaring the object variables
        self.player = player
        self.keyboard = keyboard
        self.canvasWidth = canvasWidth
        self.clock = clock
        self.playerSprites = playerSprites
        self.enemyVentrilo = enemyVentrilo

        self.points = 0

        
        frame.add_label('') 
        frame.add_label('Welcome to the Circus!') 
        frame.add_label('You must now fight your troupe members.')
        frame.add_label('')
        frame.add_label('Controls:')
        frame.add_label('A = Move left')
        frame.add_label('W = Jump')
        frame.add_label('D = Move right')
        frame.add_label('Right arrow key = Shoot Horizontally')
        frame.add_label('')

        self.finished = False
        self.playerDead = False

    
    max = canvasWidth
    min = 0

    def addPoints(self):
        self.points = self.player.points

    def setPlayersprite(self):
        if(self.keyboard.shoot):
            if(self.player.facingRight):
                return 6
            return 5 
        elif (self.keyboard.jump):
            if(self.player.facingRight):
                return 4
            return 3
        if ((self.keyboard.right) or (self.player.getPlayerCurrentPos()[0] <= (70))):
            return 2
        elif ((self.keyboard.left) or (self.player.getPlayerCurrentPos()[0] >= (self.canvasWidth - (self.player.radius/2)))):
            return 1
        return 0

    def draw(self, canvas):
        canvas.draw_text(str(self.points),(32,522), 30, "White")

    def update(self, canvas):
        self.enemyVentrilo.setBackground(canvas)
        self.clock.tick() #incrementing the clock each cycle
        self.addPoints()
        self.draw(canvas)

        if (self.player.isDead() == False) and (self.enemyVentrilo.isDead() == False):
            if (self.enemyVentrilo.phase1 == True):
                bulletTimer = random.randrange(20, 50)
                if self.clock.transition(bulletTimer): #adding a delay to shooting the bullets
                    self.enemyVentrilo.shootBullet()
            elif(self.enemyVentrilo.phase2 == True):
                self.enemyVentrilo.shootBullet()
            if ((self.keyboard.right) or (self.player.getPlayerCurrentPos()[0] <= (70))): # makes the player move right so long it is within boundary 
                self.player.facingRight = True #marking to check if the player is facing right
                self.player.playerPosition.add(Vector(2, 0)) #moving the character to the right
                if (self.player.getPlayerCurrentPos()[0] <= (75)):
                    self.player.playerPosition.add(Vector(2,0))
            if ((self.keyboard.left) or (self.player.getPlayerCurrentPos()[0] >= (self.canvasWidth - (self.player.radius/2)))): # makes the player move left so long it is within boundary 
                self.player.facingRight = False #marking to check if the player is facing left
                self.player.playerPosition.add(Vector(-2, 0))
                if (self.player.getPlayerCurrentPos()[0] >= (530)):
                    self.player.playerPosition.add(Vector(-2,0))
            if (self.keyboard.jump):
                    if (self.player.jumpCounter <= 30): # if the jump counter is not exceeded, add the jump height vector to the player's position
                        self.player.isJumping = True
                        self.player.playerPosition.add(-(self.player.jumpHeight))
                        self.player.jumpCounter += 1
                        self.player.on_ground = False
                # used to prevent the response from the w button from being too sensitive
            if(self.keyboard.shoot):
                    if self.clock.transition(5): #adding a delay to shooting the bullets
                        self.player.shootBullet() #creating a new bullet
            self.playerSprites.currentSprite = self.setPlayersprite()
            self.player.isJumping = False 
        else:
            if (self.player.isDead()):
                self.playerDead = True
            if (self.enemyVentrilo.phaseVictory == True):
                canvas.draw_text("Victory!!!!",(canvasWidth/2,canvasHeight/2), 36, "Black")
            self.finished = True