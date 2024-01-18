import random
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Vector import Vector
from EnemyBullet import EnemyBullet
import math

canvasWidth = 1000
canvasHeight = 616

class EnemyVentrilo:
    def __init__(self, canvasWidth, canvasHeight, player, clock):
        #initialising variables for the enemy collider
        self.phase1 = True #correlates to the first phase of the enemy
        self.phase2 = False #correlates to the second phase of the enemy
        self.phaseVictory = False #correlates to whether the user or enemy has died

        self.moveCirc = 0 #the intervals at which the circles will move in during phase 2

        self.counter = 1 #keeps track of the phase that the enemy is currently on 

        self.clock = clock #intitialising the clock
        self.player = player #intitialising the player
        self.enemyPosition = Vector(850, 300) #initialising the starting position of the enemy
        self.radius = 50 #initialising the radius of the enemy
        self.canvasWidth = canvasWidth #initialising the canvas width of the canvas
        self.canvasHeight = canvasHeight #initialising the canvas height of the canvas
        self.projWeapon = [] #an array holding all the bullet objects for all phases
        self.IMG_POS_TEMP = [self.enemyPosition.x, self.enemyPosition.y] #the temporary position of the image, stored as a tuple

        self.facingRight = True #checking if the enemy is facing the right

        self.isGrounded = True #a boolean that checks whether the variable is on the ground
        self.gravity = Vector(0,5) #the gravity vector

        self.health = 300 #the intitial amount of health the ventriloquist enemy has

        self.currentPhase = 0 #the current phase of the enemy, initialised at 0
        self.background1 = simplegui.load_image("https://www.cs.rhul.ac.uk/home/zlac239/background4.png") #the first background
        self.background2 = simplegui.load_image("https://www.cs.rhul.ac.uk/home/zlac239/background5.png") #the second background
        self.background = self.background1 

        self.toothImage = simplegui.load_image("https://www.cs.rhul.ac.uk/home/zlac239/tooth.png")

    def getEnemyHitBox(self, position, radius):
        #the calculation for whether the enemy has been hit by the player's bullet. If so, return true. Otherwise, return false
        if (position.x+radius > self.enemyPosition.x-self.radius*0.5) and (position.x-radius < self.enemyPosition.x+self.radius*0.5) and (position.y+radius > self.enemyPosition.y-self.radius*0.5) and (position.y-radius < self.enemyPosition.y+self.radius*0.5):
            return True
        return False

    def isDead(self): #checking if the health array has reached zero
        if (self.health <= 0):
            self.health = 0
            self.counter += 1
            # changing of the phases, triggered by how many times enemy has died
            if (self.counter == 2): # if the second phase has been reached...
                self.projWeapon = [] #reset the enemy weapon array, so no bullets from the previous scene remain on scene
                self.background = self.background2 #changing the current background
                self.health = 150 #the enemy health is set to 150, half of its original value

                #this is phase 2, so the phase 2 variable will be set to true with all the others set to false
                self.phase1 = False
                self.phase2 = True
                self.phaseVictory = False
            elif (self.counter == 3): #if the enemy has been defeated, the counter has incremented. this is reflected in which variables are true
                self.health = 0
                self.phase1 = False
                self.phase2 = False
                self.phaseVictory = True
            return True
        return False
    
    #calculating the points when the enemy has been hit
    def enemyDamage(self, position, radius):
        if (self.clock.transition(25)) and (self.isDead() == False): #should only be true if there have been 25 frames gone past and the enemy is not dead
            if self.getEnemyHitBox(position, radius):
                #calculations for the type of hits which will affect how many points the user obtains 
                if (position.x+radius > self.enemyPosition.x-self.radius*0.25) and (position.x-radius < self.enemyPosition.x+self.radius*0.25) and (position.y+radius > self.enemyPosition.y-self.radius*0.25) and (position.y-radius < self.enemyPosition.y+self.radius*0.25):
                    self.health -= 15
                    self.player.points += 30 # critical hit
                else:
                    self.health -= 10
                    self.player.points += 10 # damaging hit

    #drawing the bullets onto the canvas
    def draw(self, canvas):
        if (self.phase1 == True): #if the first phase has been reached...
            canvas.draw_circle((self.enemyPosition.x, self.enemyPosition.y), self.radius, 1, "Red", "Red") #draw the enemy at its default position

            if(len(self.projWeapon) > 0):  #drawing all bullets and maintaining the list, so long as the weapon is not empty
                for x in range(len(self.projWeapon)-1): #for all the bullets in the list
                    self.projWeapon[x].launch() #launch the bullet
                    # canvas.draw_circle((self.projWeapon[x].launchPos.x, self.projWeapon[x].launchPos.y), self.projWeapon[x].radius, self.projWeapon[x].border, self.projWeapon[x].colour,self.projWeapon[x].colour) 
                    self.projWeapon[x].draw(canvas)#draw the bullet
                    if (self.player.getPlayerHitBox(self.projWeapon[x].launchPos, self.projWeapon[x].radius) == True): #if the enemy bullet has collided with the player...
                        self.player.takeDamage() #the player will take damage
                        self.projWeapon.remove(self.projWeapon[x]) #there is no more use for the bullet. Remove it from the screen.


        elif (self.phase2 == True): #if the second phase has been reached...
            if (self.enemyPosition.x < (canvasWidth)): #Until the circle has visually moved off the screen
                self.moveCirc += 2.5 #this is the variable that increments 2.5, so the circle gradually moves off of the screen
                canvas.draw_circle(((self.enemyPosition.x + self.moveCirc), self.enemyPosition.y), self.radius, 1, "Red", "Red") #draw the circle with its everchanging position

            if(len(self.projWeapon) > 0):  #drawing all bullets and maintaining the list, so long as the weapon is not empty
                for x in range(len(self.projWeapon)-1): #for all the bullets in the list
                    self.projWeapon[x].launch() #launch the bullet
                    # canvas.draw_circle((self.projWeapon[x].launchPos.x, self.projWeapon[x].launchPos.y), self.projWeapon[x].radius, self.projWeapon[x].border, self.projWeapon[x].colour,self.projWeapon[x].colour) #draw the bullet
                    self.projWeapon[x].draw(canvas)
                    if (self.player.getPlayerHitBox(self.projWeapon[x].launchPos, self.projWeapon[x].radius) == True): #if the enemy bullet has collided with the player...
                        self.player.takeDamage() #the player will take damage
                        self.projWeapon.remove(self.projWeapon[x]) #there is no more use for the bullet. Remove it from the screen.

    def getEnemyCurrentPos(self): #getting the current position of the enemy, returns a tuple
        return (self.enemyPosition.x, self.enemyPosition.y)

    def shootBullet(self):
        #the method for shooting the enemy bullet

        playerLocation = self.player.getPlayerCurrentPos() #getting the users location
        
        if (self.phase1 == True): #if we are currently in the first phase
            
            if self.clock.transition(5):
                bulletPosition = Vector(self.enemyPosition.x, self.enemyPosition.y) #set the bullet position to a vector
            
                if (playerLocation[0] > (self.enemyPosition.x)): #if player is on the right of the enemy
                    bulletDirection = Vector(5, 0) #send the bullet to the right
                else:
                    bulletDirection = Vector(-5, 0) #send the bullet to the left
                newBullet = EnemyBullet(bulletPosition, bulletDirection, self.toothImage) #creating the new bullet object
                self.projWeapon.append(newBullet) #adding the new bullet object to the weapon's array
        
        elif (self.phase2 == True): #if we are currently in the second phase
            
            bulletPosition = random.randrange((playerLocation[0] - 500), (playerLocation[0] + 500)) #the position of the bullet will be random within a certain range of the player
            bulletPosition = Vector(bulletPosition) #change the bullet position into a vector
            bulletVelo = random.randrange(2, 15) #randomly changing the velocity within the range of (2, 15)
            bulletDirection = Vector(0, (bulletVelo)) #the bullet direction will be shooting down at the speed of the velocity
            if (self.clock.transition(10)):
                newBullet = EnemyBullet(bulletPosition, bulletDirection, self.toothImage) #create a new bullet by calling the enemy bullet class
                self.projWeapon.append(newBullet) #add the bullet to the weapon array

    def setBackground(self, canvas):
        canvas.draw_image(self.background, (125,77), (250,154), (self.canvasWidth/2,self.canvasHeight/2), (1000,616))
    
    def update(self):
        playerLocationTuple = (self.player).getPlayerCurrentPos()
        playerLocation = Vector(playerLocationTuple[0], playerLocationTuple[1])

        # finding the distance from the enemy to the player
        enemyToPlayer = playerLocation - self.enemyPosition
        distanceToPlayer = enemyToPlayer.length()

        if (self.phase1 == True): #if we are in phase 1...

            if distanceToPlayer < 301: 
                #if the distance to the player is less than the boundary...
                if (self.facingRight == True):
                    self.enemyPosition = self.enemyPosition + (Vector(5, 0)) #move right
                    
                elif (self.facingRight != True):
                    self.enemyPosition = self.enemyPosition + (Vector(-5, 0)) #move left


            if distanceToPlayer > 301:
                #if distance to the player is more than 301, move closer to the player
                if (self.facingRight == True):
                    self.enemyPosition = self.enemyPosition + Vector(-5, 0)
                elif (self.facingRight != True):
                    self.enemyPosition = self.enemyPosition + Vector(5, 0)

            # changing the position vector to move in the correct position
            for y in range(len(self.projWeapon)-1): #going throught the weapon's array and removing any bullets that are no longer within the canvas
                if (self.projWeapon[y].launchPos.x > self.canvasWidth): #only checking the x coord as the bullets only move vertically
                    self.projWeapon.remove(self.projWeapon[y])

            #keeping the enemy on screen
            if ((self.enemyPosition.x - self.radius) < 0):
                self.enemyPosition.x = self.radius
            if ((self.enemyPosition.x + self.radius) > self.canvasWidth):
                self.enemyPosition.x = (self.canvasWidth - self.radius)

            # if the wheel y position is greater than the floor, it is no longer grounded 
            if(self.enemyPosition.y < (self.canvasHeight-(self.radius))):
                self.isGrounded = False

            # if the wheel y position is on the floor, the wheel is grounded and the jump counter is reset 
            if (self.enemyPosition.y >= (self.canvasHeight- (self.radius))):
                self.isGrounded = True

            # if the wheel is not grounded and not jumping, apply gravity 
            if (self.isGrounded == False):
                self.enemyPosition.add(self.gravity)  

    # return function for the radius
    def getRadius(self):
        return [self.IMG_radius[0], self.IMG_radius[1]]
   
    # returning function for the img_pos 
    def getIMG_POS(self):
        return(self.enemyPosition.x, self.enemyPosition.y)