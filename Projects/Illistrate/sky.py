import pygame

class Sky:

    def __init__(self, width, height):
        self.mWidth = width
        self.mHeight = height
        self.mColor = (66, 215, 245)

    def draw(self, surface):
        sky = pygame.Rect(0, 0, self.mWidth, self.mHeight) #pls explain specifications
        pygame.draw.rect(surface, self.mColor, sky, 0)
        