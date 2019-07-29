from random import uniform
import pygame


class Ball:
    def __init__(self, size, min_x, max_x, min_y, max_y, left_paddle_x, right_paddle_x):
        self.mX = min_x                         # x cordinate to top left of ball
        self.mY = min_y                         # y cordinate to top left of ball
        self.mSize = size                       # length of the sides of the ball/ ball is square
        self.mDX = 0                            # DX = Delta-x // speed of the ball on x axis
        self.mDY = 0                            # DY = Delta-y // speed of the ball on y axis
        self.mMinX = min_x                      # represents the wall on the left 
        self.mMaxX = max_x                      # represents the wall on the right
        self.mMinY = min_y                      # represents the wall on the top
        self.mMaxY = max_y                      # represents the wall on the bottom
        self.mLeftPaddleX = left_paddle_x       # 
        self.mLeftPaddleMinY = min_y            # 
        self.mLeftPaddleMaxY = max_y            # 
        self.mRightPaddleX = right_paddle_x     # 
        self.mRightPaddleMinY = min_y           # 
        self.mRightPaddleMaxY = max_y           # 

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

    ####################
    ### Setters Test ###
    ####################

    
    
    def setPosition(self, x, y):
        if x >= self.mMinX and (x + self.mSize) <= self.mMaxX:
            if y >= self.mMinY and (y + self.mSize) <= self.mMaxY:
                self.mX = x
                self.mY = y

    def setSpeed(self, dx,dy):
        self.mDX = dx
        self.mDY = dy

    def setLeftPaddleY(self, paddle_min_y,paddle_max_y):
        if paddle_min_y >= self.getLeftPaddleMinY() and paddle_max_y <= self.getLeftPaddleMaxY():
            if paddle_min_y <= paddle_max_y:
                self.mLeftPaddleMinY = paddle_min_y
                self.mLeftPaddleMaxY = paddle_max_y

    def setRightPaddleY(self, paddle_min_y, paddle_max_y):
        if paddle_min_y >= self.getRightPaddleMinY() and paddle_max_y <= self.getRightPaddleMaxY():
            if paddle_min_y <= paddle_max_y:
                self.mRightPaddleMinY = paddle_min_y
                self.mRightPaddleMaxY = paddle_max_y


    def checkTop(self, new_y):
        if new_y >= self.mMinY:
            return new_y
        else:
            new = self.mMinY - new_y
            new_y = self.mMinY + new
            self.mDY = -self.mDY
            return new_y

    def checkBottom(self, new_y):
        if (new_y + self.mSize) <= self.mMaxY:
            return new_y
        else:
            self.mDY = -self.mDY
            new = new_y - self.mMaxY
            new_y = (self.mMaxY - new) - self.mSize
            return new_y -self.mSize

    def checkLeft(self, new_x):
        if new_x >= self.mMinX:
            return new_x
        else:
            self.setSpeed(0,0)
            new_x = self.mMinX
            return new_x
 
    def checkRight(self, new_x):
        if (new_x + self.mSize) <= self.mMaxX:
            return new_x
        else:
            self.setSpeed(0, 0)
            new_x = (self.mMaxX - self.mSize)
            return new_x

    def checkLeftPaddle(self, new_x, new_y):
        mid_y = (self.mY + new_y) / 2
        if mid_y > self.mLeftPaddleMinY and mid_y < self.mLeftPaddleMaxY:
            if new_x <= self.mLeftPaddleX and self.mX > self.mLeftPaddleX:
                dif = self.mLeftPaddleX - new_x
                new = self.mLeftPaddleX + dif
                self.mDX = -self.mDX
                return new
            else:
                return new_x
        else:
            return new_x
        

    
    def checkRightPaddle(self, new_x, new_y):
        mid_y = (new_y + self.mY) / 2
        if mid_y >= self.mRightPaddleMinY and mid_y <= self.mRightPaddleMaxY and (new_x + self.mSize) >= self.mRightPaddleX and (self.mX + self.mSize) <= self.mRightPaddleX:
            dif = new_x - self.mRightPaddleX + self.mSize
            new = (self.mRightPaddleX -self.mSize) - dif
            self.mDX = -self.mDX
            return new
        else:
            return new_x


    def move(self, dt):  # amount of seconds since last frame
        # Uses mX, mDX and dt to calculate new_x
        new_x = self.mX + self.mDX * dt
        new_y = self.mY + self.mDY * dt

        new_x = self.checkLeft(new_x)
        new_x = self.checkRight(new_x)

        new_y = self.checkTop(new_y)
        new_y = self.checkBottom(new_y)

        new_x = self.checkLeftPaddle(new_x, new_y)
        new_x = self.checkRightPaddle(new_x, new_y)

        self.mX = new_x
        self.mY = new_y        


    def serveLeft(self, x ,min_y,max_y,min_dx,max_dx,min_dy,max_dy):
        self.mX = x
        self.mY = uniform(min_y, max_y)         # random.uniform
        self.mDX = uniform(min_dx, max_dx)
        self.mDY = uniform(min_dy, max_dy)


    def serveRight(self, x,min_y,max_y,min_dx,max_dx,min_dy,max_dy):
        self.mX = x
        self.mY = uniform(min_y, max_y)         # random.uniform
        self.mDX = uniform(-min_dx, -max_dx)
        self.mDY = uniform(min_dy, max_dy)


    def draw(self, surface):
        ball = (self.mX, self.mY, self.mSize, self.mSize)
        draw.rect(surface, (0, 200, 0), ball)


    














