import pygame, random

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = random.randint(0,1)
        # width = 0 means the circle will be filled
        # otherwise is the thickness
        self.width = 0
        # circle radius
        self.radius = 8

    def draw(self, display):
        # colors
        __c1 = (0,0,0)
        __c2 = (85, 80, 210)

        if self.value == 0:
            pygame.draw.circle(display, __c2, [self.x, self.y], self.radius, self.width)
        else:
            pygame.draw.circle(display, __c1, [self.x, self.y], self.radius, self.width)
