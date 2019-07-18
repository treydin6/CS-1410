import pygame

class Sun:
    def __init__(self, x, y, radius):
        self.mX = x
        self.mY = y
        self.mRadius = radius
        self.mColor = (255, 191, 0)

    def draw(self, surface):
        pygame.draw.circle(surface, self.mColor,(self.mX, self.mY), self.mRadius, 0)