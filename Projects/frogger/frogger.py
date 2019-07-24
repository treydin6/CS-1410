import pygame
from froggerlib import frog, road

class Frogger:

    def __init__(self, cell_size, columns, rows):
        self.cell_size = cell_size
        self.columns = columns
        self. rows = rows
        self.width = columns * cell_size
        self.height = rows * cell_size

        self.frog_dead = False

        w = self.cell_size
        h = self.cell_size
        x = self.width//2  - w //2
        y = (self.rows - 1) * self.cell_size
        dx = x
        dy = y
        s = 25
        hg = w
        vg = h
        self.frog = frog.Frog(x, y, w, h, dx, dy, s, hg, vg)

        x = 0
        y = (self.rows - 2) * self.cell_size
        w = self.width
        h = self.cell_size
        self.road = road.Road(x,y,w,h)

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
        if self.frog.outOfBounds(self.width, self.height):
            self.frog_dead = True

    def draw(self, surface):
        bg = pygame.Rect(0,0,self.width, self.height)
        pygame.draw.rect(surface,(255,255,255), bg)

        draw_obj(surface, self.road, (0,0,0))
        # road = pygame.Rect(self.road.getX(), self.road.getY(), self.road.getWidth(), self.road.getHeight())
        # pygame.draw.rect(surface,(0, 0, 0), road)

        draw_obj(surface, self.frog, (0, 250, 0))
        # frog = pygame.Rect(self.frog.getX(), self.frog.getY(), self.frog.getWidth(), self.frog.getHeight())
        # pygame.draw.rect(surface,(0, 200, 0), frog)


def draw_obj(surface, obj, color):
    r = pygame.Rect(obj.getX(), obj.getY(), obj.getWidth(), obj.getHeight())
    pygame.draw.rect(surface, color, r)