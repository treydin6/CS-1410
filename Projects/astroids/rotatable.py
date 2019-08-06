import movable
import math

class Rotatable(movable.Movable):

    def __init__(self, x, y, dx, dy, rotation, world_width, world_height):
        super().__init__(x, y, dx, dy, world_width, world_height)
        self.mRotation = rotation

    def getRotation(self):
        return self.mRotation
    
    
    def rotate(self, delta_rotation):
        self.mRotation += delta_rotation
        self.mRotation %= 360
        # if self.mRotation < 0:
        #     self.mRotation += 360
        # if self.mRotation >= 360:
        #     self.mRotation -= 360

            
    
    
    def splitDeltaVIntoXAndY(self, rotation,delta_velocity):
        dir_x = math.cos(math.radians(rotation)) * delta_velocity
        dir_y = math.sin(math.radians(rotation)) * delta_velocity

        return(dir_x, dir_y)
    
    def accelerate(self, delta_velocity):
        (dif_x, dif_y) = self.splitDeltaVIntoXAndY(self.mRotation, delta_velocity)
        self.mDX += dif_x
        self.mDY += dif_y
    
    
    def rotatePoint(self, x, y):
        d = math.sqrt(x**2 + y**2)
        angle = math.atan2(y, x)
        angle_rotation = angle + math.radians(self.mRotation)
        rotated_x = math.cos(angle_rotation) * d
        rotated_y = math.sin(angle_rotation) * d
        return (rotated_x, rotated_y)

    
    
    def translatePoint(self, x,y):
        return (x + self.mX, y + self.mY)
    
    
    def rotateAndTranslatePoint(self, x,y):
        new_x, new_y = self.rotatePoint(x,y)
        new_x, new_y = self.translatePoint(new_x, new_y)
        return(new_x, new_y)

    
    def rotateAndTranslatePointList(self, point_list):
        points = []
        for p in point_list:
            points.append(self.rotateAndTranslatePoint(p[0],p[1]))
        return points

        