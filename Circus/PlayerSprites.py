import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Spritesheet import Spritesheet


class PlayerSprites:
    def __init__(self, player, clock):
        self.player = player
        self.clock = clock
        self.currentSprite = 0 #keeping track of the current player object that needs to be drawn to the screen
        self.idle = Spritesheet("https://www.cs.rhul.ac.uk/home/zlac239/clownIdleSprite.png", 448, 64, 7, 1, self.player.playerPosition.x, self.player.playerPosition.y, 10, self.player.radius,  self.player.radius, True, clock) #case 0, idle facing left
        self.runningLeft = Spritesheet("https://www.cs.rhul.ac.uk/home/zlac239/clownRunLeftSprite.png", 384, 64, 6, 1, self.player.playerPosition.x, self.player.playerPosition.y, 4, self.player.radius,  self.player.radius, True, clock) #case 1, running left
        self.runningRight = Spritesheet("https://www.cs.rhul.ac.uk/home/zlac239/clownRunRightSprite.png", 384, 64, 6, 1, self.player.playerPosition.x, self.player.playerPosition.y, 4, self.player.radius,  self.player.radius, True, clock) #case 2, running right
        self.jumpingLeft = Spritesheet("https://www.cs.rhul.ac.uk/home/zlac239/clownJumpLeftSprite.png", 512, 64, 8, 1, self.player.playerPosition.x, self.player.playerPosition.y, 3, self.player.radius,  self.player.radius, False, clock) #case 3, jumping
        self.jumpingRight = Spritesheet("https://www.cs.rhul.ac.uk/home/zlac239/clownJumpRightSprite.png", 512, 64, 8, 1, self.player.playerPosition.x, self.player.playerPosition.y, 3, self.player.radius,  self.player.radius, False, clock) #case 4, jumping
        self.attackLeft = Spritesheet("https://www.cs.rhul.ac.uk/home/zlac239/clownAttackSprite.png", 320, 64, 5, 1, self.player.playerPosition.x, self.player.playerPosition.y, 5, self.player.radius,  self.player.radius, True, clock) #case 5, attack left
        self.attackRight = Spritesheet("https://www.cs.rhul.ac.uk/home/zlac239/clownAttackRightSprite.png", 320, 64, 5, 1, self.player.playerPosition.x, self.player.playerPosition.y, 5, self.player.radius,  self.player.radius, True, clock) #case 6, attack right
        self.playerSpriteList = [self.idle, self.runningLeft, self.runningRight, self.jumpingLeft,self.jumpingRight,  self.attackLeft, self.attackRight]

    def draw(self, canvas):
        if(self.clock.transition(5)): #creating a slight delay before switching to the next sprite
            self.playerSpriteList[self.currentSprite].next_frame()
        self.playerSpriteList[self.currentSprite].draw(canvas, self.player.playerPosition.x, self.player.playerPosition.y) #during the player sprite to the canvas