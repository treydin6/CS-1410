import pygame

class Cloud:

    def __init__(self, top, left, width, height):
        self.mTop = top
        self.mLeft = left
        self.mWidth = width
        self.mHeight = height
        self.mColor = (200, 200, 200)

    def draw(self, surface):
        cloud = pygame.Rect(self.mTop, self.mLeft, self.mWidth, self.mHeight)
        pygame.draw.ellipse(surface, self.mColor, cloud, 0)