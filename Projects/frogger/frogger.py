import pygame
from froggerlib import frog, road, water, stage, car, log

class Frogger:

    def __init__(self, cell_size, columns, rows):
        self.cell_size = cell_size
        self.columns = columns
        self.rows = rows
        self.width = columns * cell_size
        self.height = rows * cell_size

        self.frog_dead = False


        gap_size = .2

        w = self.cell_size - (2 * gap_size * self.cell_size)
        h = self.cell_size - (2 * gap_size * self.cell_size)
        x = ((self.columns // 2) * self.cell_size) + (gap_size * self.cell_size)
        y = ((self.rows - 1) * self.cell_size) + (gap_size * self.cell_size)
        dx = x
        dy = y
        s = 25
        hg = self.cell_size
        vg = self.cell_size
        self.frog = frog.Frog(x, y, w, h, dx, dy, s, hg, vg)

        self.roads = []
        gap_size = .025
        num_roads = (self.rows - 3) //2
        for i in range(2, 2 + num_roads):
            x = 0
            y = ((self.rows - i) * self.cell_size) + (gap_size * self.cell_size)
            w = self.width
            h = self.cell_size - (2 * gap_size * self.cell_size)
            self.roads.append(road.Road(x,y,w,h))

        self.waters = []
        water_start = 2 + num_roads +1
        num_waters = (self.rows - 3) -num_roads
        for i in range(water_start, water_start+num_waters):
            x = 0
            y = (self.rows - i) * self.cell_size
            w = self.width
            h = self.cell_size 
            self.waters.append(water.Water(x,y,w,h))

        self.end_stage = stage.Stage(0, 0, self.width, self.cell_size)
        self.middle_stage = stage.Stage(0, 6 * self.cell_size, self.width, self.cell_size)
        self.start_stage = stage.Stage(0, 11 * self.cell_size, self.width, self.cell_size)


        # car
        gap_size = .2
        x = 0
        y = ((self.rows -2 ) * self.cell_size) + (gap_size * self.cell_size)
        w = self.cell_size + (2* gap_size * self.cell_size)
        h = self.cell_size - (2 * gap_size * self.cell_size)
        dx = self.width + gap_size
        dy = y
        s = 15                  # set speed of the car
        self.car = car.Car(x,y,w,h,dx,dy,s)

        # car 2
        x2 = self.width
        y2 = ((self.rows -3 ) * self.cell_size) + (gap_size * self.cell_size)
        w2 = self.cell_size + (2* gap_size * self.cell_size)
        h2 = self.cell_size - (2 * gap_size * self.cell_size)
        dx2 = 0 - gap_size
        dy2 = y2
        s = 15
        self.car2 = car.Car(x2, y2, w2, h2, dx2, dy2, s)

        # car 3
        x3 = 0
        y3 = ((self.rows -4 ) * self.cell_size) + (gap_size * self.cell_size)
        w3 = self.cell_size + (2* gap_size * self.cell_size)
        h3 = self.cell_size - (2 * gap_size * self.cell_size)
        dx3 = self.width + gap_size
        dy3 = y3
        s3 = 20                  # set speed of the car
        self.car3 = car.Car(x3,y3,w3,h3,dx3,dy3,s3)
        # car 3 #2
        x3 = 0
        y3 = ((self.rows -4 ) * self.cell_size) + (gap_size * self.cell_size)
        w3 = self.cell_size + (2* gap_size * self.cell_size)
        h3 = self.cell_size - (2 * gap_size * self.cell_size)
        dx3 = self.width + gap_size
        dy3 = y3
        s3 = 10                  # set speed of the car
        self.car32 = car.Car(x3,y3,w3,h3,dx3,dy3,s3)

        # car 4
        x4 = self.width
        y4 = ((self.rows -5 ) * self.cell_size) + (gap_size * self.cell_size)
        w4 = self.cell_size + (2* gap_size * self.cell_size)
        h4 = self.cell_size - (2 * gap_size * self.cell_size)
        dx4 = 0 - gap_size
        dy4 = y4
        s = 25
        self.car4 = car.Car(x4, y4, w4, h4, dx4, dy4, s)

        # log lane 1
        logx = 0
        logxR = self.width
        logy1 = ((self.rows -7) * self.cell_size) + (gap_size * self.cell_size)
        logy2 = ((self.rows -8) * self.cell_size) + (gap_size * self.cell_size)
        logy3 = ((self.rows -9) * self.cell_size) + (gap_size * self.cell_size)
        logy4 = ((self.rows -10) * self.cell_size) + (gap_size * self.cell_size)
        logy5 = ((self.rows -11) * self.cell_size) + (gap_size * self.cell_size)
        logw = self.cell_size + (3* gap_size * self.cell_size)
        logh = self.cell_size - (2 * gap_size * self.cell_size)
        logdx =  self.width + gap_size
        logdxR = 0 - logw
        logdy1 = logy1
        logdy2 = logy2
        logdy3 = logy3
        logdy4 = logy4
        logdy5 = logy5

        logs = 15

        self.log1 = log.Log(logx, logy1, logw, logh, logdx, logdy1, logs) #left to right
        self.log2 = log.Log(logxR, logy2, logw, logh, logdxR, logdy2, 5) # right to left
        self.log3 = log.Log(logx, logy3, logw, logh, logdx, logdy3, 20) # left to right
        self.log4 = log.Log(logxR, logy4, logw, logh, logdxR, logdy4, 15) # right to left
        self.log5 = log.Log(logx, logy5, logw, logh, logdx, logdy5, logs) # left to right


    def UP(self):
        self.frog.up()

    def DOWN(self):
        self.frog.down()

    def LEFT(self):
        self.frog.left()

    def RIGHT(self):
        self.frog.right()


    def evolve(self, dt):
        if self.frog_dead:
            return
        self.frog.move()
        self.car.move()
        self.car2.move()
        self.car3.move()
        self.car32.move()
        self.car4.move()
        self.log1.move()
        self.log2.move()
        self.log3.move()
        self.log4.move()
        self.log5.move()
        if self.car.atDesiredLocation():
            self.car.setX(-self.car.getWidth() - 10)
        if self.car2.atDesiredLocation():
            self.car2.setX(self.width)
        if self.car3.atDesiredLocation():
            self.car3.setX(-self.car.getWidth() - 90)
        if self.car32.atDesiredLocation():
            self.car32.setX(-self.car.getWidth() - 90)
        if self.car4.atDesiredLocation():
            self.car4.setX(self.width)
        # logs desired loction
        if self.log1.atDesiredLocation():
            self.log1.setX(-self.log1.getWidth() - 10)
        if self.log2.atDesiredLocation():
            self.log2.setX(self.width)
        if self.log3.atDesiredLocation():
            self.log3.setX(-self.log1.getWidth() - 10)
        if self.log4.atDesiredLocation():
            self.log4.setX(self.width)
        if self.log5.atDesiredLocation():
            self.log5.setX(-self.log1.getWidth() - 10)




        if self.car.hits(self.frog):
            self.frog_dead = True
        if self.car2.hits(self.frog):
          self.frog_dead = True
        if self.car3.hits(self.frog):
            self.frog_dead = True
        if self.car32.hits(self.frog):
            self.frog_dead = True
        if self.car4.hits(self.frog):
            self.frog_dead = True

        
        if self.frog.hits(self.waters):
            self.frog_dead = True
        

        if self.frog.outOfBounds(self.width, self.height):
            self.frog_dead = True
        


    def draw(self, surface):
        bg = pygame.Rect(0,0,self.width, self.height)
        pygame.draw.rect(surface,(255,255,255), bg)

        #draw_obj(surface, self.road, (0,0,0))
        for road in self.roads:
            draw_obj(surface, road, (0,0,0))
        for water in self.waters:
            draw_obj(surface, water,(0, 0, 255))
        ## Put stuff after road and water

        #car
        draw_obj(surface, self.car, (255,0,0))
        draw_obj(surface, self.car2, (100, 0, 176))
        draw_obj(surface, self.car3, (50,130,70))
        draw_obj(surface, self.car32,(255,0,0))     # car lane 3 2nd car
        draw_obj(surface, self.car4, (255,255,0))

        # stage
        draw_obj(surface, self.end_stage, (248, 7, 244))
        draw_obj(surface, self.middle_stage, (248, 7, 244))
        draw_obj(surface, self.start_stage, (248, 7, 244))

        # logs
        draw_obj(surface, self.log1, (150, 75, 0))
        draw_obj(surface, self.log2, (150, 75, 0))
        draw_obj(surface, self.log3, (150, 75, 0))
        draw_obj(surface, self.log4, (150, 75, 0))
        draw_obj(surface, self.log5, (150, 75, 0))



        



        ## Dont put anything after this.
        # this is the frog and the frog needs to be the last item
        draw_obj(surface, self.frog, (0, 250, 0))
        
       


def draw_obj(surface, obj, color):
    r = pygame.Rect(obj.getX(), obj.getY(), obj.getWidth(), obj.getHeight())
    pygame.draw.rect(surface, color, r)



