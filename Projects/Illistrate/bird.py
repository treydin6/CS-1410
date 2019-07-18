import pygame

class Bird:

    def __init__(self, x, y, width, height):
        p1 = (x,y+height)
        p2= (int(x=width/4),y)
        p3 = (int(x+width/2), y+ height)
        p4 = (int(x+3*width/4),y)
        p5 = (x+width, y+width)
        self.mpoints = [p1, p2, p3, p4, p5]
        self.mThickness = 2
        self.mColor = (0, 0, 0)

    def draw(self, surface):
        pygame.draw.lines(surface, self.mColor, False, self.mpoints, self.mThickness)