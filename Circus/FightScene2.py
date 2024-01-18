import SimpleGUICS2Pygame.simpleguics2pygame as simplegui, math
from Vector import Vector

canvasWidth = 1000
canvasHeight = 616

class FightScene2:
    def __init__(self, player, aerialists, clock, playerSprites, keyboard, canvasWidth, points, frame):
        #declaring the object variables
        self.player = player
        self.aerialists = aerialists
        self.keyboard = keyboard
        self.canvasWidth = canvasWidth
        self.clock = clock
        self.playerSprites = playerSprites
        
        frame.set_canvas_background("Black")
        self.timer = simplegui.create_timer(6000, self.aerialists.timer_handler)
        self.timer.start()

        frame.add_label('Up arrow key = Shoot upwards')

        self.delayBool = False

        self.delay = simplegui.create_timer(500,self.timer_handler) #adding a delay to the player's weapon
        self.delay.start()
        self.points = points

        self.playerDead = False
        self.finished = False
    
    max = canvasWidth
    min = 0

    def timer_handler(self): #resetting the delay for the player's weapon
        self.delayBool = False
        self.delay.start()

    def addPoints(self): #getting all the player's points
        self.points = self.player.points 

    def draw(self, canvas): #drawing the points to the canvas
        canvas.draw_text(str(self.points),(32,522), 30, "White")
        # self.aerialists.draw(canvas)

    def setPlayersprite(self): #setting the player's current sprite
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
    

    def update(self, canvas):
        self.clock.tick() #incrementing the clock each cycle
        self.addPoints() #getting the players points 
        self.draw(canvas)

        if(self.player.isDead() == False) and (self.aerialists.isDead() == False): #checking is the player is dead
            self.aerialists.draw(canvas) #updating the aerialists
            if ((self.keyboard.right) or (self.player.getPlayerCurrentPos()[0] <= (70))):
                self.player.facingRight = True #marking to check if the player is facing right
                self.player.playerPosition.add(Vector(5, 0)) #moving the character to the right
            # makes the player move left so long it is within boundary 
            if ((self.keyboard.left) or (self.player.getPlayerCurrentPos()[0] >= (self.canvasWidth - (self.player.radius/2)))):
                self.player.facingRight = False #marking to check if the player is facing left
                self.player.playerPosition.add(Vector(-5, 0))

            # if the jump counter is not exceeded, add the jump height vector to the player's position
            if (self.keyboard.jump):
                if (self.player.jumpCounter <= 30): #setting the jumping sprite object
                    self.player.isJumping = True
                    self.player.playerPosition.add(-(self.player.jumpHeight))
                    self.player.jumpCounter += 1
                    self.player.on_ground = False #allowing for gravity to be added the player
            if(self.keyboard.damage):
                if self.delayBool == False: #adding a delay to the damage
                    self.player.takeDamage() #removing one of the hearts 
            if(self.keyboard.shoot):
                if self.delayBool == False:  #adding a delay to shooting the bullets
                    self.delayBool = True
                    self.player.shootBullet() #creating a new bullet
            if(self.keyboard.shootUp):
                if self.delayBool == False:  #adding a delay to shooting the bullets
                    self.delayBool = True
                    self.player.shootVerticalBullet() #creating a new bullet
            self.playerSprites.currentSprite = self.setPlayersprite() #setting the player's current sprite
            self.player.isJumping = False #allowing gravity to be applied
        else:
            if (self.player.isDead()== True): #setting the death screen
                self.delay.stop()
                self.aerialists.stopAreialists()
                self.playerDead = True
                self.finished = True
            else:
                self.delay.stop()
                self.aerialists.stopAreialists()
                self.finished = True #setting the victory screen