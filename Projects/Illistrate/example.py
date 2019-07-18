import pygame
import grass, sky, cloud, sun, square, roof, bird

# this example game draws 3 concentric circles on top of a single color background
# the circles move down every time frame
# the user can control the circles by:
# - clicking the left mouse button to relocate them
# - holding the UP key to move them up
# - pressing the A key to move them to the left of the window
# - holding the A key to gradually move them to the right
class Example:

    def __init__( self, width, height ):
        self.mWidth = width
        self.mHeight = height

        # DSU's colors
        self.mDSUTan = ( 229, 217, 189 )
        self.mDSUBlack = ( 2, 2, 2 )
        self.mDSULightRed = ( 186, 28, 33 )
        self.mDSUDarkRed = ( 136, 21, 24 )

        # Sizes to draw circles
        self.mRadius1 = int( min( self.mWidth, self.mHeight ) / 10 )
        self.mRadius2 = int( self.mRadius1 * 0.7 )
        self.mRadius3 = int( self.mRadius1 * 0.4 )

        # Position to draw circles
        self.mDrawX = self.mWidth / 2
        self.mDrawY = 2 * self.mRadius1
        
        return

    # move the circles to the left side of the window every time the a button is pressed
    def actOnPressA( self ):
        self.mDrawX = self.mRadius1
        return

    # move the circles right every frame the a button is held down
    # don't let the circles go off the window
    def actOnHoldA( self ):
        self.mDrawX += self.mWidth / 20
        if self.mDrawX + self.mRadius1 > self.mWidth:
            self.mDrawX = self.mWidth - self.mRadius1
        return

    # raise the circles every frame the UP button is held down
    # don't let the circles go off the window
    def actOnHoldUP( self ):
        self.mDrawY -= self.mHeight / 20
        if self.mDrawY < self.mRadius1:
            self.mDrawY = self.mRadius1
        return

    # relocate the circles based on the mouse click
    # don't let the circles go off the window
    def actOnLeftClick( self, x, y ):
        self.mDrawX = x
        if self.mDrawX < self.mRadius1:
            self.mDrawX = self.mRadius1
        if self.mDrawX + self.mRadius1 > self.mWidth:
            self.mDrawX = self.mWidth - self.mRadius1
            
        self.mDrawY = y
        if self.mDrawY < self.mRadius1:
            self.mDrawY = self.mRadius1
        if self.mDrawY + self.mRadius1 > self.mHeight:
            self.mDrawY = self.mHeight - self.mRadius1
        return

    # move the circles down every frame according to how much time has passed
    # don't let the circles go off the window
    def evolve( self, dt ):
        dy = dt * ( self.mHeight / 5 )
        self.mDrawY += dy
        if self.mDrawY + self.mRadius1 > self.mHeight:
            self.mDrawY = self.mHeight - self.mRadius1
        return

    # draws the current state of the system
    def draw( self, surface ):
        
        # rectangle to fill the background
        # sky = pygame.Rect(0, 0, self.mWidth, self.mHeight)
        # pygame.draw.rect( surface, (66, 215, 245), sky, 0 )

        # grass = pygame.Rect( 0, self.mWidth//2, self.mWidth, self.mHeight//2)
        # pygame.draw.rect( surface, (164, 254, 66), grass, 0 )



        # must have 5/6 0f these
        # i have ract, circle, ellipse
        # rect(), polygon(), circle(), ellipse(), arc(), line()
        # Drawing the Sky 1/6 Classes complete
        theSky = sky.Sky(700, 600)
        theSky.draw(surface)

        # Drawing the Grass 2/6 Classed complete
        theGrass = grass.Grass(700, 600)
        theGrass.draw(surface)

        # Drawing the Cloud 3/6 Classed complete
        theCloud = cloud.Cloud(50, 50, 125, 75)
        theCloud.draw(surface)

        # right cloud
        theCloud2 = cloud.Cloud(500, 100, 125, 75)
        theCloud2.draw(surface)

        theSun = sun.Sun(350, 100, 70)
        theSun.draw(surface)

        house = square.Square(200, 300, 300, 190, (50, 100, 200))
        house.draw(surface)

        # surface, self.mColor, self.mPoint, 0)
        HouseRoof = roof.Roof( ( (170, 300), (350, 200), (530, 300) ), (115, 47, 0) )
        HouseRoof.draw(surface)

        # door
        door = square.Square(325, 410, 50, 80, (255, 255, 255))
        door.draw(surface)

        # left window
        # self.mX, self.mY, self.mWidth, self.mHeight
        leftWindow = square.Square(242, 330, 40, 40, (255, 191, 0))
        leftWindow.draw(surface)

        # right window
        rightWindow = square.Square(420, 330, 40, 40, (255,191,0 ))
        rightWindow.draw(surface)

        # walk way
        stone1 = square.Square(333, 500, 35, 35, (90, 90, 90))
        stone1.draw(surface)

        stone2 = square.Square(333, 545, 35, 35, (90, 90, 90))
        stone2.draw(surface)

        stone2 = square.Square(333, 590, 35, 35, (90, 90, 90))
        stone2.draw(surface)

        bird1 = bird.Bird(75, 200, 50, 50)
        bird1.draw(surface)

        

        return
