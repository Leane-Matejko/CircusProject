
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui, math 
from Vector import Vector
from Heart import Heart
from Bullet import Bullet

class Player:
    def __init__(self, position, canvasWidth, canvasHeight, clock):
        #initialising variables for the circle collider
        self.playerPosition = position
        self.speed = Vector()
        self.radius = 50
        self.canvasWidth = canvasWidth
        self.canvasHeight = canvasHeight

        self.IMG_POS_TEMP = [self.playerPosition.x, self.playerPosition.y]

        #initialising the variable for the sprite to jump
        self.isGrounded = True
        self.gravity = Vector(0,5)
        self.jumpHeight = Vector(0,10)
        self.isJumping = False
        self.jumpCounter = 0

        self.facingRight = True #checking if the player is facing the right

        self.points = 0

        self.delay = simplegui.create_timer(250,self.delay_handler)
        self.delay.start()
        self.delayBool = False

        self.health = [Heart((40,576)),Heart((100,576)),Heart((160,576)), Heart((220,576)), Heart((280,576))] #the player's health
        self.projWeapon = [] #an array holding all the bullet objects
        self.clock = clock

    def delay_handler(self):
        self.delayBool = False
        self.delay.start()

    #drawing the bullets and hearts onto the canvas
    def draw(self, canvas):
        if(self.isDead() == True): #chekcing if the dead window needs to be shown
            canvas.draw_text('You are Dead :(',(self.canvasWidth/2,self.canvasHeight/2), 64, 'Black')
        if(len(self.health) > 0): #drawing the hearts to the screen
            for i in range(len(self.health)): #drawing all possible hearts to the canvas
                self.health[i].draw(canvas)
        if(len(self.projWeapon) > 0):  #drawing all bullets and maintaining the list, so long as the weapon is not empty
            for x in range(len(self.projWeapon)):
                self.projWeapon[x].launch()
                self.projWeapon[x].draw(canvas) #updating the bullet's animation

    def getPlayerHitBox(self, position, radius):
        if (position.x+radius > self.playerPosition.x-self.radius*0.6) and (position.x-radius < self.playerPosition.x+self.radius*0.6) and (position.y+radius > self.playerPosition.y-self.radius*0.6) and (position.y-radius < self.playerPosition.y+self.radius*0.6):
            return True
        return False
    
    def takeDamage(self):
        if (self.delayBool == False):
            self.delayBool = True
            if(len(self.health) > 0): #preventing a null pointer error
                self.health.pop(len(self.health)-1) #removing the heart from the health array

    def getPlayerCurrentPos(self): #getting the current position of the player, returns a tuple
        return (self.playerPosition.x, self.playerPosition.y)
    
    def shootBullet(self): #creates a new bullet object and adds it to the rest of the weapon's array
        bulletPosition = Vector(self.getPlayerCurrentPos()[0], self.getPlayerCurrentPos()[1]) #starting the bullet from the player's position
        if self.facingRight == True: #sending bullets in the right direction
            bulletDirection = Vector(10,0)
        else: #sending bullets in the left direction
            bulletDirection = Vector(-10, 0)
        newBullet = Bullet(bulletPosition, bulletDirection, self.clock) #creating the new bullet object
        self.projWeapon.append(newBullet) #adding the new bullet object to the weapon's array

    def shootVerticalBullet(self): #creates a new bullet object and adds it to the rest of the weapon's array
        bulletPosition = Vector(self.getPlayerCurrentPos()[0], self.getPlayerCurrentPos()[1]) #starting the bullet from the player's position
        newBullet = Bullet(bulletPosition, Vector(0, -10), self.clock) #creating the new bullet object
        self.projWeapon.append(newBullet) #adding the new bullet object to the weapon's array

    def isDead(self): #checking if the health array ha reached zero
        self.delay.stop()
        return (len(self.health) == 0)
    
    def update(self, enemy):
        # changing the position vector to move in the correct position
        self.delayBool = False
        for y in range(len(self.projWeapon)-2): #going throught the weapon's array and removing any bullets that are no longer within the canvas
            if (self.projWeapon[y].launchPos.x > self.canvasWidth) or (self.projWeapon[y].launchPos.y < 0) or (self.projWeapon[y].launchPos.x < 0) or (enemy.enemyDamage(self.projWeapon[y].launchPos, self.radius)): #only checking the x coord as the bullets only move vertically
                self.projWeapon.remove(self.projWeapon[y])

        self.playerPosition.add(self.speed) #moving the player arrow the canvas
        self.IMG_POS_TEMP = (self.playerPosition.x, self.playerPosition.y)

        # if the wheel y position is greater than the floor, it is no longer grounded 
        if(self.playerPosition.y < (self.canvasHeight-(self.radius/2) )):
            self.isGrounded = False

        # if the wheel y position is on the floor, the wheel is grounded and the jump counter is reset 
        if (self.playerPosition.y >= (self.canvasHeight- (self.radius))):
            self.isGrounded = True
            self.jumpCounter = 0

        # if the wheel is not grounded and not jumping, apply gravity 
        if (self.isGrounded == False) and (self.isJumping==False):
            self.playerPosition.add(self.gravity)
   
    # returning function for the img_pos 
    def getIMG_POS(self):
        return(self.playerPosition.x, self.playerPosition.y)