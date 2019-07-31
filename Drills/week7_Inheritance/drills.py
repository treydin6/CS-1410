# drill1
# Initializes the data members to their values from the x and y parameters.
class Shape:
    def __init__(self, x, y):
        self.mX = x
        self.mY = y

# drill 2
# The current value of the x or y data member, depending on the method
def getX(self):
        return self.mX

def getY(self):
    return self.mY

# drill 3
# True if a change occurred, False otherwise
def setX(self, value):
        if self.mX != value:
            self.mX = value
            return True
        else:
            return False

def setY(self, value):
    if self.mY != value:
        self.mY = value
        return True
    else:
        return False

# drill 4
# init method
import shape
class Circle(shape.Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        shape.Shape.setX(self, x)
        shape.Shape.setY(self, y)
        self.mRadius = r

# drill 5
# True if a change occurred, False otherwise.
def getRadius(self):
        return self.mRadius

def setRadius(self, r):
    if r < 0 or self.mRadius == r:
        return False
    else:
        self.mRadius = r
        return True

# drill 6
# init method
import shape
class Rectangle(shape.Shape):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        shape.Shape.setX(self, x)
        shape.Shape.setY(self, y)
        self.mWidth = w
        self.mHeight = h

# drill 7
# The current value of the correct data member. / True if a change occurred, False otherwise.
def getWidth(self):
        return self.mWidth

def getHeight(self):
    return self.mHeight

def setWidth(self, value):
        if value < 0 or value == self.mWidth:
            return False
        else:
            self.mWidth = value
            return True
def setHeight(self, value):
    if value < 0 or value == self.mHeight:
        return False
    else:
        self.mHeight = value
        return True

# drill 8
# init method
import rectangle
class Square(rectangle.Rectangle):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        self.mSize = size

# drill 9
# The current value of the correct data member. / True if a change occurred, False otherwise.
def getSize(self):
        return rectangle.Rectangle.getWidth(self)

def setSize(self, value):
    if rectangle.Rectangle.setWidth(self, value) and rectangle.Rectangle.setHeight(self, value):
        return True
    else:
        return False

# drill 10
# True if a change occurred, False otherwise
def move(self, delta_x, delta_y):
        if delta_x == 0 and delta_y == 0:
            return False
        else:
            self.mX += delta_x
            self.mY += delta_y
            return True
