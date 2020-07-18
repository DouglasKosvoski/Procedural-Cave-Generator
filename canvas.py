import pygame

class Canvas:
    def __init__(self):
        self.height = 802
        self.width = 1201
        self.resolution = [self.width, self.height]
        self.canvas = pygame.display.set_mode(self.resolution)
        self.clock = pygame.time.Clock()
        self.bg_color = (30, 30, 30)
        self.grid_color = (0, 250, 0)
        self.gap = 48 #subdivisoes
        self.step = int(self.resolution[0]/self.gap)
        
    def background(self):
        pygame.draw.rect(self.canvas, self.bg_color, (0, 0, self.width, self.height))
    
    def update(self):
        pygame.display.update()
        
    def draw_grid(self):
        for i in range(0, self.width, self.step):
            pygame.draw.line(self.canvas, self.grid_color, [0,i], [self.width, i])
            
        for j in range(0, self.height, self.step):
            pygame.draw.line(self.canvas, self.grid_color, [j, 0], [j, self.height])
