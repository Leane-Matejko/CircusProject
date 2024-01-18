import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Keyboard:
    def __init__(self):
        self.right = False
        self.left = False
        self.jump = False
        self.damage = False
        self.shoot = False
        self.shootUp = False
        self.next = False
        self.option1 = False
        self.option2 = False
        self.option3 = False

    # a and d to move left and right, space to jump
    def keyDown(self, key):
        if key == simplegui.KEY_MAP['d']: # d - right
            self.right = True
        if key == simplegui.KEY_MAP['a']: # a - left
            self.left = True
        if key == simplegui.KEY_MAP['w']: #w - jump
            self.jump = True
        if key == simplegui.KEY_MAP['right']: #right - weapon
            self.shoot = True
        if key == simplegui.KEY_MAP['up']: #up - vertical weapon
            self.shootUp = True
        if key == simplegui.KEY_MAP['space']: #space - nextDialogueOption
            self.next = True
        if key == simplegui.KEY_MAP['1']: #1 - Dialogue Option 1
            self.option1 = True
        if key == simplegui.KEY_MAP['2']: #2 - Dialogue Option 2
            self.option2 = True
        if key == simplegui.KEY_MAP['3']: #2 - Dialogue Option 3
            self.option3 = True

    def keyUp(self, key):
        if key == simplegui.KEY_MAP['d']:
            self.right = False
        if key == simplegui.KEY_MAP['a']:
            self.left = False
        if key == simplegui.KEY_MAP['w']:
            self.jump = False
        if key == simplegui.KEY_MAP['right']:
            self.shoot = False
        if key == simplegui.KEY_MAP['up']:
            self.shootUp = False
        if key == simplegui.KEY_MAP['space']:
            self.next = False
        if key == simplegui.KEY_MAP['1']:
            self.option1 = False
        if key == simplegui.KEY_MAP['2']:
            self.option2 = False
        if key == simplegui.KEY_MAP['3']: 
            self.option3 = False