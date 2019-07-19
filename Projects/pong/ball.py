import pygame

class Ball:
    def __init__(self, size, min_x, max_x, min_y, max_y, left_paddle_x, right_paddle_x):
        self.mX = min_x                     # x cordinate to top left of ball
        self.mY = min_y                     # y cordinate to top left of ball
        self.mSize = Size                   # length of the sides of the ball/ ball is square
        self.mDX = 0                        # DX = Delta-x // speed of the ball on x axis
        self.mDY = 0                        # DY = Delta-y // speed of the ball on y axis
        self.mMinX = min_x                  # represents the wall on the left 
        self.mMaxX = max_x                  # represents the wall on the right
        self.mMinY = min_y                  # represents the wall on the top
        self.mMaxY = max_y                  # represents the wall on the bottom
        self.mLeftPaddleX = left_paddle_x
        self.mLeftPaddleMinY = 
        self.mLeftPaddleMaxY = 
        self.mRightPaddleX = 
        self.mRightPaddleMinY = 
        self.mRightPaddleMaxY = 

    def 