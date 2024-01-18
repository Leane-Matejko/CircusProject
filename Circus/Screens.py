import sys

class StartScene:
    def __init__(self, canvasWidth, canvasHeight, frame):
        self.canvasWidth = canvasWidth
        self.canvasHeight = canvasHeight

        self.startGameBool = False

        self.mouse = frame.set_mouseclick_handler(self.mouse_handler) #registering the mouse's coordinates within the canvas
        self.nameInput = frame.add_input('Enter your name: ', self.nameInput_handler, 150) #trying to get a name for the player

        self.position = [0,0] #coordinates for the mouse

        self.name = None #the name of the player

    def nameInput_handler(self, text_input): #setting the player's input as their name
        self.name = text_input

    def draw(self, canvas):
        self.update()
        #drawing the information to the screen
        canvas.draw_text(("CIRCUS"), (self.canvasWidth/2-110, self.canvasHeight/2), 160, "White")
        canvas.draw_polygon([(610,420),(750,420),(750,450),(610,450)], 1,'White', 'White')
        canvas.draw_text(("Play"), (660, 440), 20, "Black")
        canvas.draw_polygon([(610,490),(750,490),(750,520),(610,520)], 1,'White', 'White')
        canvas.draw_text(("Exit"), (660, 510), 20, "Black")

    def update(self):
        if self.position[0] > 610 and self.position[0] < 750 and self.position[1] > 420 and self.position[1] < 450: #checking if the play again button has been pressed
            self.startGameBool = True
        if self.position[0] > 610 and self.position[0] < 750 and self.position[1] > 490 and self.position[1] < 520: #checking if the exit button has been pressed
            sys.exit() #closing the window
    
    def mouse_handler(self, position): #setting the current position of the mouse
        self.position = position

    def startGame(self): #returning whether game will be started
        return (self.startGameBool, self.name)



class DeathScreen:
    def __init__(self, points, canvasWidth, canvasHeight, frame):
        self.canvasWidth = canvasWidth
        self.canvasHeight = canvasHeight

        self.startGameBool = False

        self.closeGameBool = False

        frame.set_mouseclick_handler(self.mouse_handler) #registering the mouse's coordinates within the canvas

        self.points = points #points that player recieved

        self.position = [0,0] #coordinates for the mouse

    def draw(self, canvas):
        self.update()
        #drawing the information to the screen
        canvas.draw_text(("YOU ARE NOW"), (self.canvasWidth/2-120, self.canvasHeight/2-50), 80, "White")
        canvas.draw_text(("THE JOKE"), (self.canvasWidth/2-50, self.canvasHeight/2), 80, "White")
        canvas.draw_polygon([(610,420),(750,420),(750,450),(610,450)], 1,'White', 'White')
        canvas.draw_text(("Play Again"), (635, 440), 20, "Black")
        canvas.draw_polygon([(610,490),(750,490),(750,520),(610,520)], 1,'White', 'White')
        canvas.draw_text(("Exit"), (660, 510), 20, "Black")
        canvas.draw_text(("They're laughing at you now"), (50, 510), 20, "White")
        canvas.draw_text(("Only " + str(self.points)+ " points"), (50, 530), 20, "White")

    def update(self):
        if self.position[0] > 610 and self.position[0] < 750 and self.position[1] > 420 and self.position[1] < 450: #checking if the play again button has been pressed
            self.startGameBool = True
        if self.position[0] > 610 and self.position[0] < 750 and self.position[1] > 490 and self.position[1] < 520: #checking if the exit button has been pressed
            self.closeGameBool = True
    
    def mouse_handler(self, position): #setting the current position of the mouse
        self.position = position
    
    def startGame(self): #returning whether game will be restarted
        return self.startGameBool

    def closeGame(self): #returning whether the game will be closed
        return self.closeGameBool



class EndingScreen:
    def __init__(self, points, canvasWidth, canvasHeight, frame):
        self.canvasWidth = canvasWidth
        self.canvasHeight = canvasHeight

        self.startGameBool = False

        self.closeGameBool = False

        self.background = "https://www.cs.rhul.ac.uk/home/zlac239/circusTitleScreen.jpg"

        frame.set_mouseclick_handler(self.mouse_handler) #registering the mouse's coordinates within the canvas

        self.points = points #points that player recieved
        
        self.position = [0,0] #coordinates for the mouse

    def draw(self, canvas):
        self.update()
        #drawing the information to the screen
        canvas.draw_text(("Thank you for playing!! You recieved " + str(self.points) + " points!!"), (self.canvasWidth/2, self.canvasHeight/2+100), 20, "White")
        canvas.draw_polygon([(680,450),(820,450),(820,480),(680,480)], 1,'White', 'White')
        canvas.draw_text(("Play Again"), (705, 470), 20, "Black")
        canvas.draw_polygon([(680,520),(820,520),(820,550),(680,550)], 1,'White', 'White')
        canvas.draw_text(("Exit"), (730, 540), 20, "Black")

    def update(self):
        if self.position[0] > 680 and self.position[0] < 820 and self.position[1] > 450 and self.position[1] < 480: #checking if the play again button has been pressed
            self.startGameBool = True
        if self.position[0] > 680 and self.position[0] < 820 and self.position[1] > 520 and self.position[1] < 550: #checking if the exit button has been pressed
            self.closeGameBool = True

    def mouse_handler(self, position): #setting the current position of the mouse
        self.position = position

    def startGame(self): #returning whether game will be restarted
        return self.startGameBool
    
    def closeGame(self): #returning whether the game will be closed
        return self.closeGameBool