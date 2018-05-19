from Model.Figure import *

class Enemy(Figure):
    def __init__(self, scale, x, y):
        super().__init__(scale,x,y)

    def move(self, laberinto):
        pos = self.getPosition()
        x = pos[0]
        y = pos[1]
        xstep= random.choice([-1, 0, 1])
        if xstep!= 0:
            ystep= 0
        else:
            ystep = random.choice([-1, 0, 1])
        if (x + xstep * self.step, y + ystep * self.step) in laberinto.ocupados:
            return
        else:
            self.x0 += xstep * self.step
            self.y0 += ystep * self.step
