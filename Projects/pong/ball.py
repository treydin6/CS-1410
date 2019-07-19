import pygame

class Ball:
    def __init__(self, size, min_x, max_x, min_y, max_y, left_paddle_x, right_paddle_x):
        self.mX = min_x                     # x cordinate to top left of ball
        self.mY = min_y                     # y cordinate to top left of ball
        self.mSize = size                   # length of the sides of the ball/ ball is square
        self.mDX = 0                        # DX = Delta-x // speed of the ball on x axis
        self.mDY = 0                        # DY = Delta-y // speed of the ball on y axis
        self.mMinX = min_x                  # represents the wall on the left 
        self.mMaxX = max_x                  # represents the wall on the right
        self.mMinY = min_y                  # represents the wall on the top
        self.mMaxY = max_y                  # represents the wall on the bottom
        self.mLeftPaddleX = left_paddle_x
        self.mLeftPaddleMinY = min_y        
        self.mLeftPaddleMaxY = max_y
        self.mRightPaddleX = right_paddle_x
        self.mRightPaddleMinY = min_y
        self.mRightPaddleMaxY = max_y

    def getX(self):
        return self.mX

    def getY(self):
        return self.mY

    def getSize(self):
        return self.mSize

    def getDX(self):
        return self.mDX

    def getDY(self):
        return self.mDY

    def getMinX(self):
        return self.mMinX

    def getMaxX(self):
        return self.mMaxX

    def getMinY(self):
        return self.mMinY

    def getMaxY(self):
        return self.mMaxY

    def getLeftPaddleX(self):
        return self.mLeftPaddleX

    def getLeftPaddleMinY(self):
        return self.mLeftPaddleMinY

    def getLeftPaddleMaxY(self):
        return self.mLeftPaddleMaxY

    def getRightPaddleX(self):
        return self.mRightPaddleX

    def getRightPaddleMinY(self):
        return self.mRightPaddleMinY

    def getRightPaddleMaxY(self):
        return self.mRightPaddleMaxY
