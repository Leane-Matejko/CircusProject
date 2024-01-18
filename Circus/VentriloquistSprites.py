canvasWidth = 1000
canvasHeight = 616

class VentriloquistSprites:
    def __init__(self, player, clock):
        self.player = player
        self.clock = clock

        self.currentSprite = 0 #setting the current sprite

        self.ventriloSprites = [] #list of all the ventriloquist sprites

    def draw(self, canvas):
        if(self.clock.transition(5)): #creating a slight delay before switching to the next sprite
            canvas.draw_circle((canvasWidth/2, canvasHeight/2), 150, 12, 'Green')
        self.ventriloSprites[self.currentSprite].draw(canvas, self.player.playerPosition.x, self.player.playerPosition.y)