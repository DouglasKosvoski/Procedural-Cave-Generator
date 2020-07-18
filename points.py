import pygame, random

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = random.randint(0,1)
        self.width = 0
        self.radius = 8

    def draw(self, display):
        __c1 = (0,0,0)
        __c2 = (120,120,120)
        
        if self.value == 0:
            pygame.draw.circle(display, __c2, [self.x, self.y], self.radius, self.width)
            pass
        else:
            pygame.draw.circle(display, __c1, [self.x, self.y], self.radius, self.width)
