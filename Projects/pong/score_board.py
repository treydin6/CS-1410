import pygame
from text import Text


class ScoreBoard:
    def __init__(self, x, y, width, height):
        self.mX = x
        self.mY = y
        self.mWidth = width
        self.mHeight = height
        self.mLeftScore = 0
        self.mLeftText = Text(str(self.mLeftScore), self.mX + 20, self.mY + 22)
        self.mRightScore = 0
        self.mRightText = Text(str(self.mRightScore), self.mX + 60, self.mY + 22)
        self.mServeStatus = 1
       

    def getX(self):
        return self.mX
    def getY(self):
        return self.mY
    def getWidth(self):
        return self.mWidth
    def getHeight(self):
        return self.mHeight
    def getLeftScore(self):
        return self.mLeftScore
    def getRightScore(self):
        return self.mRightScore
    def getServeStatus(self):
        return self.mServeStatus
    def isGameOver(self):
        if self.mServeStatus > 2:
            return True
        else:
            return False

    def scoreLeft(self):
        if not self.isGameOver():
            self.mLeftScore += 1
            self.mLeftText.setText(str(self.mLeftScore))
            if self.mLeftScore == 9:
                self.mServeStatus = 3

    def scoreRight(self):
        if not self.isGameOver():
            self.mRightScore += 1
            self.mRightText.setText(str(self.mRightScore))
            if self.mRightScore == 9:
                self.mServeStatus = 4

    def swapServe(self):
        if not self.isGameOver():
            if self.mServeStatus == 1:
                self.mServeStatus = 2
            else:
                self.mServeStatus = 1

    def draw(self, surface):
        color = (250, 250, 250)
        rect = (self.mX, self.mY, self.mWidth, self.mHeight)
        pygame.draw.rect(surface, color, rect)
        self.mLeftText.draw(surface)
        self.mRightText.draw(surface)

