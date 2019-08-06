# drill 1
# The current value of the appropriate data member.
import math
KIND_PLAYER = 1
KIND_FOOD = 2
KIND_AI = 3
class Blob:
    def __init__(self, mass, x, y, world_width, world_height, kind):
        self.mMass = float(mass)  # mass
        self.mX = float(x)        # x position
        self.mY = float(y)        # y position
        self.mDx = 0.             # portion of speed that comes from x
        self.mDy = 0.             # portion of speed that comes from y
        self.mKind = kind         # kind of blob
        self.mAlive = True        # blob's life status
        # size of the world, used for bounding motion
        self.mWorldWidth = world_width
        self.mWorldHeight = world_height
        # used to scale the speed to tune game play
        self.mSpeedMultiplier = 10.0
        # used to scale the display size of blobs
        self.mRadiusMultiplier = 5.0
        # used to make sure 1 frame's motion doesn't overshoot the destination
        self.mDestinationSpeed = 0.0
        return

    def getMass(self):
        return self.mMass
    def getX(self):
        return self.mX
    def getY(self):
        return self.mY
    def getAlive(self):
        return self.mAlive
    def getKind(self):
        return self.mKind


# drill 2
# The smallest value of the two possible speed choices.
def getSpeed(self):
    return min(self.mDestinationSpeed, self.mSpeedMultiplier/math.log(self.mMass))

# drill 3
# The radius calculated as described above.
def getRadius(self):
    return self.mRadiusMultiplier * math.sqrt(self.mMass / math.pi)

# drill 4
# True if self and other are not equal, otherwise, False.
def __ne__(self, other):
    if self.mX != other.mX or self.mY != other.mY:
        return True
    else:
        return False

# drill 5
# True if self is larger by the required amount, otherwise False.
def __gt__(self, other):
        if self.mMass /other.mMass > 1.25:
            return True
        else:
            return False

# drill 6
# Return self. There is a reason for this, but it is not explained here.
def __iadd__(self, other):
        self.mMass += other.mMass
        other.mMass = 0
        other.mAlive = False
        return self

