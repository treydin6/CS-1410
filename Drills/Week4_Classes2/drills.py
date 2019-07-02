# drill 1
# In this exercise, you will create a class to represent a Car and its speed. You are only responsible for creating the data member to store speed and for the constructor.
class Car:
    def __init__(self):
        self.mSpeed = 0.0

# drill 2
# In this exercise, you will add to your Car class a method to return the value of the speed data member from an instance of the class.
def getSpeed(self):
        return self.mSpeed

# drill 3
# In this exercise, you will add to your Car class a method to change the value of the speed data member in an instance of the class.
def setSpeed(self, speed):
        if speed >= 0 and speed <=maxSpeed:
            self.mSpeed = speed
            return True
        else:
            return False

# drill 4
# In this exercise, you will add to your Car class a method to change the value of the speed data member in an instance of the class.
def accelerate(self, delta_speed):
        if delta_speed > 0 and self.mSpeed < 80:
            if self.mSpeed + delta_speed >81:
                self.mSpeed = 80
                return True
            else:
                self.mSpeed += delta_speed
                return True
        else:
            return False

# drill 5
# In this exercise, you will add to your Car class a method to apply the brake and reduce the speed of an instance.
def brake(self, delta_speed):
        if delta_speed > 0 and self.mSpeed > 0:
            if self.mSpeed - delta_speed < 0:
                self.mSpeed = 0
                return True
            else:
                self.mSpeed -= delta_speed
                return True
        else:
            return False

# drill 6
# In this exercise, you will add to your Car class a method to apply the brake and reduce the speed of an instance.
import math

class Circle:
    def __init__(self, radius):
        self.mRadius = radius

# drill 7
# In this exercise, you will add to your Circle class a method to return the value of the radius data member from an instance of the class.
def getRadius(self):
        return self.mRadius

# drill 8
# In this exercise, you will add to your Circle class a method to change the value of the radius data member in an instance of the class.
def setRadius(self, radius):
        if radius >= 0:
            self.mRadius = radius
            return True
        else: return False

# drill 9
# In this exercise, you will add to your Circle class a method to calculate the area of a circle instance. If you don't know the formula, find it. 
#Use an approximation for pi that has at least 7 digits.
def getArea(self):
        radius = self.getRadius()
        x = math.pi*radius **2
        return x

# drill 10
#In this exercise, you will add to your Circle class a method to calculate the circumference of a circle instance. If you don't know the formula, find it. 
#Use an approximation for pi that has at least 7 digits.
def getCircumference(self):
        pi = math.pi
        radius = self.getRadius()
        return 2*pi*radius


