class Clock:
    def __init__(self):
        self.time = 0 #a counter used by the clock, incremented every game cycle

    def tick(self):
        self.time += 1 #incrementing the clock

    def transition(self, frameDuration): #controlling a delay, the longer the frame duration, the longer the transition time
        if self.time % frameDuration == 0:
            return True
        else:
            return False