import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Spritesheet:
    def __init__(self, imageURL, sheetWidth, sheetHeight, columns, rows, xPos,yPos, numFrames, spriteWidth, spriteHeight, looping, clock):
        self.image = simplegui.load_image(imageURL)

        self.sheetWidth = sheetWidth
        self.sheetHeight = sheetHeight
        self.columns = columns
        self.rows = rows

        self.spriteWidth = sheetWidth/columns
        self.spriteHeight = sheetHeight/rows
        self.spriteCentreX = self.spriteWidth/2
        self.spriteCentreY = self.spriteHeight/2
        self.frameInd = [0,0]
        self.sourceDim = (self.spriteWidth, self.spriteHeight)

        self.x = xPos
        self.y = yPos

        self.currentFrame = (self.x, self.y)

        self.scale = 2
        self.xScale = self.scale*spriteWidth
        self.yScale = self.scale*spriteHeight

        self.spriteSize = (self.xScale,self.yScale)
        self.spritePosition = (xPos, yPos)

        self.clock = clock

        self.looping = looping

        self.currentImage = 0 #tracking the current image that we're on
        self.maxFrames = numFrames #the final frame of the incomplete spritesheet

    def draw(self, canvas, x, y):
        #drawing the sprite to the canvas while the spritesheet has not been finished
        # setting up the current frame of the sprite
        self.currentFrame = (self.spriteWidth * self.frameInd[0] + self.spriteCentreX, self.spriteHeight * self.frameInd[1] + self.spriteCentreY)
        self.spritePosition = (x, y)
        # drawing the sprite to the canvas
        canvas.draw_image(self.image, self.currentFrame, self.sourceDim, self.spritePosition, self.spriteSize)

    def next_frame(self):
        if self.done() == True: #checking if the animation is finished
            if self.clock.transition(15): #adding a delay
                self.reset() #resets the values of the spritesheet
        
        # if the sprite has not reached the final frame 
        if self.done() == False:
            self.currentImage += 1 #keeping track of the current frame
            # moving along the sprite frame appropriately
            self.frameInd[0] = (self.frameInd[0] + 1) % self.columns
            if self.frameInd[0] == 0: #resetting the index frame of the animation
                self.frameInd[1] = (self.frameInd[1] + 1) % self.rows

    def done(self):
        if self.looping == True: #preventing the animation from stopping
            return False
        # checking whether the sprite has reached its final frame
        if self.currentImage == self.maxFrames+1:
            return True
        else:
            return False

    def reset(self):
        self.frameInd = [0,0]
        self.currentImage = 0


