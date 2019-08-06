import rock, ship, pygame, random

class Asteroids:

    def __init__(self, world_width, world_height):
        self.mWorldWidth = world_width
        self.mWorldHeight = world_height
        shipX = self.mWorldWidth / 2
        shipY = self.mWorldHeight / 2
        self.mShip = ship.Ship(shipX, shipY, self.mWorldWidth, self.mWorldHeight)
        self.mRocks = []
        self.mObjects = [self.mShip]

        # drawing the rocks
        for x in range(10):
            rockX = random.randrange(0, self.mWorldWidth)
            rockY = random.randrange(0 , self.mWorldHeight)
            rock1 = rock.Rock(rockX, rockY, world_width, world_height)
            self.mRocks.append(rock1)
            self.mObjects.append(rock1)


    def getWorldWidth(self):
        return self.mWorldWidth
    

    def getWorldHeight(self):
        return self.mWorldHeight
    

    def getShip(self):
        return self.mShip
    
    
    def getRocks(self):
        return self.mRocks
    

    def getObjects(self):
        return self.mObjects
    

    def turnShipLeft(self, delta_rotation):
        self.mShip.rotate(-delta_rotation)
    

    def turnShipRight(self, delta_rotation):
        self.mShip.rotate(delta_rotation)
    

    def accelerateShip(self, delta_velocity):
        self.mShip.accelerate(delta_velocity)
    
    def evolve(self, dt):
        for obj in self.mObjects:
            obj.evolve(dt)
    
    
    def draw(self, surface):
        surface.fill((0,0,0))
        for obj in self.mObjects:
            obj.draw(surface)