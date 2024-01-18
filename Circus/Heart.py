import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Spritesheet import Spritesheet

class Heart:
    def __init__(self, pos):
        #setting up parameters to draw the hearts to the canvas
        self.image = simplegui.load_image("https://www.cs.rhul.ac.uk/home/zlac239/heartSprite.png")
        self.pos = pos
        self.radius = 20

        #setting the variables for the heart image to be drawn to the canvas
        self.currentFrame = (pos[0], pos[1])
        self.sourceDim = (32,32)
        self.spritePosition = (pos[0], pos[1])
        self.spriteSize = (50,50)

    def draw(self,canvas): #drawing hte heart image to the screen
        canvas.draw_image(self.image, (16,16), self.sourceDim, self.pos, self.spriteSize)