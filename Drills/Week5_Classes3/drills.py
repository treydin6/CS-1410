# 1
# Initializes the data members to their values from the red, green, and blue parameters.
class Color:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

# 2
# The current value of the red, green or blue data member, depending on the method.
def getRed(self):
        return self.red

    def getGreen(self):
        return self.green

    def getBlue(self):
        return self.blue

# 3
# Sets the correct data member to value, if it is in legal range. The legal range is 0 to 255, inclusive.
def setRed(self, value):
        if value >= 0 and value <= 255:
            self.red = value
            return True
        else:
            return False

    def setGreen(self, value):
        if value >= 0 and value <= 255:
            self.green = value
            return True
        else:
            return False
    def setBlue(self, value):
        if value >= 0 and value <= 255:
            self.blue = value
            return True
        else:
            return False

# 4
# Changes the red, green, and blue values for the color into their complementary values. Use 255 as the maximum value.
def complement(self):
        self.red = 255 - self.red
        self.green = 255 - self.green
        self.blue = 255 - self.blue
        return True

# 5
# Changes the red, green, and blue values for the color into those of the next triad color.
def triad(self):
        red = self.red
        green = self.green
        blue = self.blue

        self.red = green
        self.green = blue
        self.blue = red
        return True

# 6
# The longest string in strings.
import math

def longest_string(strings):
    longest = strings[0]
    for string in strings:
        if len(string) > len(longest):
            longest = string
    return longest

# 7
# The key from dictionary that is considered less than all other keys.
def least_key(dictionary):
    small = 'zzzzzzzzzz'
    for key in dictionary:
        if key < small:
            small = key
    return small


# 8
# The value from dictionary that is considered less than or equal to all other values.
def least_value(dictionary):
    small = 100000
    for key in dictionary:
        if dictionary[key] < small:
            small = dictionary[key]
    return small

#9
# The planet from planets that is farthest from the center of the star they orbit.
def farthest_planet(planets):
    largest = 0
    plan = ''
    for planet in planets:
        x = planet['x']**2
        y = planet['y']**2
        z = planet['z']**2
        l = x + y + z
        if l > largest:
            largest = l
            plan = planet
    return plan

# 10
# The factorial of n, according to the description above.
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact
