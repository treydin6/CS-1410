import pygame

class Square:

    def __init__(self, x, y, w, h, color):
        self.mX = x
        self.mY = y
        self.mWidth = w
        self.mHeight = h
        self.mColor = color

    def draw(self, surface):
        #                        x     ycordinates   width    height     
        square = pygame.Rect(self.mX, self.mY, self.mWidth, self.mHeight) 

        pygame.draw.rect(surface, self.mColor, square, 0)