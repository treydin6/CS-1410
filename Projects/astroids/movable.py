

class Movable:

    def __init__(self, x, y, dx, dy, world_width, world_height):
        self.mX = x
        self.mY = y
        self.mDX = dx
        self.mDY = dy
        self.mWorldWidth = world_width
        self.mWorldHeight = world_height
    
    def getX(self):
        return self.mX
    def getY(self):
        return self.mY

    def getDX(self):
        return self.mDX
    
    def getDY(self):
        return self.mDY
    
    def getWorldWidth(self):
        return self.mWorldWidth
    
    def getWorldHeight(self):
        return self.mWorldHeight
    
    def move(self, dt):
        new_x = self.mX + self.mDX * dt
        new_y = self.mY + self.mDY * dt

        if new_x >= self.mWorldWidth:
            new_x -= self.mWorldWidth
        if new_x < 0:
            new_x += self.mWorldWidth

        if new_y >= self.mWorldHeight:
            new_y -= self.mWorldHeight
        if new_y < 0:
            new_y += self.mWorldHeight

        self.mX = new_x
        self.mY = new_y
    
    def accelerate(self, delta_velocity):
        raise NotImplementedError
        
    def evolve(self, dt):
        raise NotImplementedError
    
    def draw(self, surface):
        raise NotImplementedError