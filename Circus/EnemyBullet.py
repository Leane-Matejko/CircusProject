import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Spritesheet import Spritesheet
from Vector import Vector

class EnemyBullet:
    def __init__(self, launchPos, bulletSpeed, image):
        self.launchPos = launchPos #the bullet current position
        self.radius = 20 #the radius of the bullet size
        self.border = 1 #the border size of the bullet
        self.colour = 'Black' #the colour of the bullet
        self.speed = bulletSpeed #the speed of the bullet is the same as the parameter that is passed to it
        self.image = image

    def launch(self):
        self.launchPos.add(self.speed) #changing the position of the bullet based on the direction it was shoot in

    def draw(self, canvas): #drawing the web sprite to the canvas
        canvas.draw_image(self.image, (32,32), (64,64), (self.launchPos.x,self.launchPos.y), (32,32))