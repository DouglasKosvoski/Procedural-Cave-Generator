import pygame

class Canvas:
    def __init__(self):
        self.width = 854
        self.height = 480
        self.resolution = [self.width, self.height]
        self.canvas = pygame.display.set_mode(self.resolution)
        self.clock = pygame.time.Clock()
        self.bg_color = (30, 30, 30)
        self.grid_color = (0, 250, 0)

        # the greater this number the more detail the map will contain
        self.gap = 48 #subdivisoes
        self.step = int(self.resolution[0]/self.gap)

    def background(self):
        pygame.draw.rect(self.canvas, self.bg_color, (0, 0, self.width, self.height))

    def update(self):
        pygame.display.update()
