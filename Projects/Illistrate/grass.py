import pygame

class Grass:

    def __init__(self, width, height):
        self.mWidth = width
        self.mHeight = height
        self.mColor = (10, 112, 34)

    def draw(self, surface):
        grass = pygame.Rect(0, (self.mHeight//2) + 150, self.mWidth, self.mHeight//2) 
        pygame.draw.rect(surface, self.mColor, grass, 0)