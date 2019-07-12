# 1 
# Initializes the data member for capacity from the parameter, 
# and the data member for charge from the capacity.
class Battery:
    def __init__(self, capacity):
        self.capacity = capacity
        self.charge = capacity

# 2
# The current value of the capacity data member.
def getCapacity(self):
        return self.capacity

# 3
# The current value of the charge data member.
def getCharge(self):
        return self.charge

# 4
# Removes milliamps from the charge of the object. If the new charge is less than 0, 
# then set the charge to 0.
# Only do this action of milliamps is positive, and the Battery isn't already at 0 charge.
def drain(self, milliamps):
        if milliamps > 0 and self.charge > 0:
            if self.charge - milliamps < 0:
                self.charge = 0
                return True
            else:
                self.charge -= milliamps
                return True
        else:
            return False

# 5
# Adds milliamps to the charge of the object. If the new charge is exceeds the capacity, 
# then set the charge to the maximum allowed charge.
# Only do this action of milliamps is positive, and the Battery isn't already at maximum charge.
def recharge(self, milliamps):
        if milliamps > 0 and self.getCharge() < self.getCapacity():
            if self.getCharge() + milliamps > self.getCapacity():
                self.charge = self.getCapacity()
                return True
            else:
                self.charge += milliamps
                return True
        else:
            return False

# 6
# Initializes the data members using x, y, width, and height
class Rectangle:
    def __init__(self, x, y, width, height):
        self.mX = x
        self.mY = y
        self.mWidth = width
        self.mHeight = height

# 7
# A number, the current value of the appropriate data member.
def getX(self):
        return self.mX

    def getY(self):
        return self.mY

    def getWidth(self):
        return self.mWidth

    def getHeight(self):
        return self.mHeight

# 8
# Sets the data member to value, if it is in legal range. The legal range is 0 or higher.
def setX(self, value):
        if value > 0:
            self.mX = value
            return True
        else:
            return False

    def setY(self, value):
        if value > 0:
            self.mY = value
            return True
        else:
            return False

    def setWidth(self, value):
        if value > 0:
            self.mWidth = value
            return True
        else:
            return False

    def setHeight(self, value):
        if value > 0:
            self.mHeight = value
            return True
        else:
            return False

# 9
# Calculates the area of the rectangle and returns it.
def getArea(self):
        return self.mWidth * self.mHeight

# 10
# Calculates the perimeter distance of the rectangle and returns it.
def getPerimeter(self):
        return (self.mWidth * 2) + (self.mHeight * 2)

