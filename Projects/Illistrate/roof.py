import pygame

class Roof:

    def __init__(self, points, color):
        self.mPoint = points
        self.mColor = color
        return

    def draw(self, surface):
        pygame.draw.polygon(surface, self.mColor, self.mPoint, 0)
        return