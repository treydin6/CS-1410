import movable

class Rotatable(movable.Movable):

    def __init__(self, x, y, dx, dy, rotation, world_width, world_height):
        super().__init__(x, y, dx, dy, world_width, world_height)
        self.mRotation = rotation

    def getRotation(self):
        return self.mRotation
    
    
    def rotate(self, delta_rotation):
        if self.mRotation >= 0 and self.mRotation < 360:
            
    
    
    def splitDeltaVIntoXAndY(rotation,delta_velocity)
    
    
    def accelerate(delta_velocity)
    
    
    def rotatePoint(x,y)
    
    
    def translatePoint(x,y)
    
    
    def rotateAndTranslatePoint(x,y)
    
    
    def rotateAndTranslatePointList(point_list)