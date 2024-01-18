import SimpleGUICS2Pygame.simpleguics2pygame as simplegui, random
from Vector import Vector

class EnemyAerialists:
    def __init__(self, canvasWidth, canvasHeight, player, clock):
        
        self.speed = Vector()
        self.radius = 75
        self.player = player
        self.clock = clock
        self.canvasWidth = canvasWidth
        self.canvasHeight = canvasHeight

        #images for the aerialist's weapons
        self.lyraImage = simplegui.load_image("https://www.cs.rhul.ac.uk/home/zlac239/lyraSprite.png")
        self.silkImage = simplegui.load_image("https://www.cs.rhul.ac.uk/home/zlac239/silkSprite.png")
        self.webImage = simplegui.load_image("https://www.cs.rhul.ac.uk/home/zlac239/webSprite.png")

        self.aerialPosition = Vector(canvasWidth-(self.radius), canvasHeight-self.radius)
        self.health = 500

        self.currentPhase = 0
        #the backgrounds for the different phases
        self.background1 = simplegui.load_image("https://www.cs.rhul.ac.uk/home/zlac239/background1.png")
        self.background2 = simplegui.load_image("https://www.cs.rhul.ac.uk/home/zlac239/background2.png")
        self.background3 = simplegui.load_image("https://www.cs.rhul.ac.uk/home/zlac239/background3.png")
        self.background = self.background1
        
        self.weapon1 = [] #for phase 1's weapon
        self.weapon2 = None #for phase 2's weapon
        self.weapon3 = [] #for phase 3's weapon

        self.delay = simplegui.create_timer(250,self.delay_handler) #a delay for the enemy taking damage
        self.delay.start()
        self.weaponDelay = simplegui.create_timer(1000,self.weaponDelay_handler) #a delay for the enemy first and third enemy's weapon
        self.weaponDelay.start()
        self.newSilkDelay = simplegui.create_timer(1000,self.newSilkDelay_handler)#a delay for creating a new weapon for phase 2

        #boolean variables to track the enemies variables 
        self.delayBool = False
        self.weaponDelayBool = False
        self.newSilkDelayBool = True
        self.facingUpwards = True
        self.facingRight = False

    def delay_handler(self):#resetting the delay for the enemy damage
        self.delayBool = False
        self.delay.start()

    def weaponDelay_handler(self):#resetting the delay for the enemy's weapon
        self.weaponDelayBool = False
        self.weaponDelay.start()

    def newSilkDelay_handler(self):#resetting the delay for the phase 2 weapon
        self.newSilkDelayBool = True
        self.newSilkDelay.start()
    
    def timer_handler(self):#changing the phase the enemy is in and repositioning/resetting the enemy for the new current phase
        self.currentPhase += 1
        if (self.currentPhase % 3 == 2):#resetting the position and background
            self.aerialPosition = Vector(self.canvasWidth-(self.radius), self.radius)
            self.background = self.background3
        elif(self.currentPhase % 3 == 1):#resetting the first phase's weapon and background and starting the delay for the second weapon
            self.newSilkDelay.start()
            self.weapon1 = []
            self.background = self.background2
        elif(self.currentPhase % 3 == 0):#resetting the position, background and phase 2 and 3's weapons
            self.newSilkDelay.stop()
            self.weapon3 = []
            self.weapon2 = None
            self.background = self.background1
            self.aerialPosition = Vector(self.canvasWidth-(self.radius), self.canvasHeight-self.radius)

    def updatePhase(self):#updating the appropriate phase
        if(self.currentPhase % 3 == 0):
            self.updatePhase1()
        elif(self.currentPhase % 3 == 1):
            self.updatePhase2()
        elif(self.currentPhase % 3 == 2):
            self.updatePhase3()

    def movingUpwards(self):#moving the aerialist along the right side of the canvas
        if ((self.aerialPosition.y + self.radius) >= self.canvasHeight):
            self.facingUpwards = True
        if (self.aerialPosition.y - self.radius < 0):
            self.facingUpwards = False
    
        if (self.facingUpwards == True):
            self.speed = Vector(0, -2) #moving upwards
        else:
            self.speed= Vector(0, 2) #moving downwards
        
        self.aerialPosition.add(self.speed) #repositioning the enemy
    
    def movingSideways(self):#moving the aerialist along the top of the canvas
        if ((self.aerialPosition.x + self.radius) == self.canvasWidth):
            self.facingRight = False
        if (self.aerialPosition.x - self.radius < 0):
            self.facingRight = True
    
        if (self.facingRight == True):
            self.speed = Vector(2, 0) #moving right
        else:
            self.speed= Vector(-2, 0) #moving left
        
        self.aerialPosition.add(self.speed) #repositioning the enemy
    
    def updatePhase1(self):
        self.movingUpwards()
        if self.weaponDelayBool == False: #creating a new lyra if the delay has stopped
            self.weaponDelayBool = True
            newLyra = Lyra(Vector(self.aerialPosition.x, self.aerialPosition.y), self.lyraImage) #creating the new lyra object
            self.weapon1.append(newLyra)
    
    def updatePhase2(self): 
        self.movingUpwards()
        if(self.newSilkDelayBool == True): #creating a new silk if the delay has stopped
            self.newSilkDelayBool = False
            self.newSilkDelay.stop()
            newSilk = Silk(Vector(self.aerialPosition.x, self.aerialPosition.y), self.silkImage)
            self.weapon2 = newSilk
    
    def updatePhase3(self):
        self.movingSideways()
        if self.weaponDelayBool == False: #creating a new web if the delay has stopped
            self.weaponDelayBool = True
            newWeb = Web(Vector(self.aerialPosition.x, self.aerialPosition.y), self.webImage) #creating the new lyra object
            self.weapon3.append(newWeb)

    def getEnemyHitBox(self, position, radius): #checking if another object is interacting with the aerialist's hitbox
        if (position.x+radius > self.aerialPosition.x-self.radius*0.5) and (position.x-radius < self.aerialPosition.x+self.radius*0.5) and (position.y+radius > self.aerialPosition.y-self.radius*0.5) and (position.y-radius < self.aerialPosition.y+self.radius*0.5):
            return True
        return False

    def isDead(self): #checking if the health amount has reached zero
        if (self.health <= 0):
            self.health = 0
        return self.health == 0
    
    def enemyDamage(self, position, radius): #checking if the enemy can be damaged and awarding the appropriate points
        if (self.delayBool == False):
            if self.getEnemyHitBox(position, radius):
                if (position.x+radius > self.aerialPosition.x-self.radius*0.25) and (position.x-radius < self.aerialPosition.x+self.radius*0.25) and (position.y+radius > self.aerialPosition.y-self.radius*0.25) and (position.y+radius < self.aerialPosition.y+self.radius*0.25):
                    self.health -= 15
                    self.delayBool = True
                    self.player.points += 30 # critical hit (within 25% of the aerialist's position)
                else:
                    self.delayBool = True
                    self.health -= 10
                    self.player.points += 10  # damaging hit (within 50% of the aerialist's position)

    def setBackground(self, canvas): #drawing the background image to the canvas
        canvas.draw_image(self.background, (125,77), (250,154), (self.canvasWidth/2,self.canvasHeight/2), (1000,616))

    def stopAreialists(self): #stopping all possible timers
        self.delay.stop()
        self.weaponDelay.stop()
        self.newSilkDelay.stop()

    def draw(self, canvas):
        if(self.isDead() == False) or (self.player.isDead() == False): #checking if either the player or aerialists are dead
            self.updatePhase() #updating the aerialist's information
            canvas.draw_circle((self.aerialPosition.x,self.aerialPosition.y), self.radius, 1, "Black","Black") #drawing the enemy to the screen
            if(self.currentPhase%3 == 0) and (len(self.weapon1) > 0):  #drawing all bullets and maintaining the list, so long as the weapon is not empty
                for x in range(len(self.weapon1)-1): #drawing all the lyras to the screen and checking if they have damaged the player
                    self.weapon1[x].launch()
                    self.weapon1[x].draw(canvas)
                    if(self.player.getPlayerHitBox(self.weapon1[x].launchPos, self.weapon1[x].radius)):
                        self.player.takeDamage()
                        self.weapon1.remove(self.weapon1[x])
                    elif(self.weapon1[x].launchPos.x - self.weapon1[x].radius < 0 or self.weapon1[x].launchPos.x +self.weapon1[x].radius > self.canvasWidth) or (self.weapon1[x].launchPos.y + self.weapon1[x].radius < 0 or self.weapon1[x].launchPos.y - self.weapon1[x].radius > self.canvasHeight):
                        self.weapon1.remove(self.weapon1[x]) #removing all lyras that are out of bounds or hit the player
            elif(self.currentPhase%3 == 2) and (len(self.weapon3) > 0):  #drawing all the webs and maintaining the list, so long as the weapon is not empty
                for x in range(len(self.weapon3)-1):
                    self.weapon3[x].launch()
                    self.weapon3[x].draw(canvas)
                    if(self.player.getPlayerHitBox(self.weapon3[x].launchPos, self.weapon3[x].radius)):
                        self.player.takeDamage()
                        self.weapon3.remove(self.weapon3[x])
                    elif(self.weapon3[x].launchPos.y + self.weapon3[x].radius > self.canvasHeight):
                        self.weapon3.remove(self.weapon3[x]) #removing all webs that are out of bounds or hit the player
            elif(self.currentPhase%3 == 1) and (self.weapon2 != None):
                self.weapon2.launch() #moving the silk across the canavs
                self.weapon2.draw(canvas) #drawing the silk to the canvas
                if(self.weapon2.reachedEnd()== True): #a delay before creating the next silk
                    self.newSilkDelay.start()
                if (self.weapon2.getWithinSilk(self.player.playerPosition, self.player.radius*0.6) == True) and (self.delayBool == False): #cause damage to the player if they are hit with a silk
                    self.delayBool = True
                    self.player.takeDamage()

class Lyra:
    def __init__(self, launchPos,  lyraSprite):
        self.launchPos = launchPos #the bullet current position
        self.radius = 40
        self.border = 1
        self.speed = Vector(self.randNum(),1) #each lyra has a random speed

        self.lyraSprite = lyraSprite #the lyra's sprite image

    def launch(self):
        self.launchPos.add(self.speed) #changing the position of the bullet based on the direction it was shoot in

    def randNum(self): #random number generator
        return random.randint(-5,-1)

    def draw(self, canvas): #drawing the lyra sprite to the canvas
        canvas.draw_image(self.lyraSprite, (64,64), (128,128), (self.launchPos.x,self.launchPos.y), (128,128))


class Silk:
    def __init__(self, launchPos, silkImage, canvasWidth = 1000, canvasHeight = 616):
        self.launchPos = launchPos #the bullet current position
        self.radius = 20
        self.speed = Vector(self.randNum(), 1)

        self.silkSprite = silkImage

        self.canvasWidth = canvasWidth
        self.canvasHeight = canvasHeight

    def launch(self):
        if(self.reachedEnd() == False):
            self.launchPos.add(self.speed) #changing the position of the bullet based on the direction it was shoot in#changing the position of the bullet based on the direction it was shoot in
    
    def getWithinSilk(self, playerPos, radius): #checking if something is within range of the silk
        if(playerPos.x + radius > self.launchPos.x and playerPos.x -radius < self.canvasWidth) and (playerPos.y + radius > self.launchPos.y - self.radius and playerPos.y - radius < self.launchPos.y - self.radius):
            return True
        return False

    def reachedEnd(self): #checking if the silk has reached the end of the screen
        if(self.launchPos.x <= 0):
            return True
        return False

    def randNum(self): #generating a random speed for the silk
        return random.randint(-15,-10)

    def draw(self, canvas): #drawing the silk image to the screen
        canvas.draw_image(self.silkSprite, (525,32), (1050,64), (self.launchPos.x,self.launchPos.y), (2500,64))

class Web:
    def __init__(self, launchPos, webSprite):
        self.launchPos = launchPos #the bullet current position
        self.radius = 40
        self.speed = Vector(0,self.randNum(1,5))
        self.gravity = 1.05 #the acceleration factor

        self.webSprite = webSprite

    def launch(self):
        self.speed.multiply(self.gravity)# making the web accelerate towards the ground
        self.launchPos.add(self.speed) #changing the position of the bullet based on the direction it was shoot in

    def randNum(self, num1, num2): #generating a random number wiht a certain boundary
        return random.randint(num1,num2)
    
    def draw(self, canvas): #drawing the web sprite to the canvas
        canvas.draw_image(self.webSprite, (32,32), (64,64), (self.launchPos.x,self.launchPos.y), (128,128))
