import pygame
from points import Point

class MarchingSquares:
    def __init__(self, canvas):
        self.canvas = canvas
        pass

    def generate_points(self):
        __pontos = []
        for i in range(0, self.canvas.width, self.canvas.step):
            sub_list = []
            for j in range(0, self.canvas.width, self.canvas.step):
                sub_list.append(Point(i,j))
            __pontos.append(sub_list)
        return __pontos

    def draw_points(self, points_list):
        for i in range(len(points_list)):
            for j in range(len(points_list[0])):
                points_list[i][j].draw(self.canvas.canvas)

    def draw_line(self, p1, p2):
        line_color = (55, 255, 87)
        line_width = 2
        pygame.draw.line(self.canvas.canvas, line_color, [p1[0], p1[1]], [p2[0], p2[1]], line_width)

    def get_state(self, a, b, c, d):
        return ((a.value*8) + (b.value*4) + (c.value*2) + (d.value*1))

    def draw_cave(self, lista):
        for i in range(len(lista)-1):
            for j in range(len(lista[0])-1):
                x = i * self.canvas.step
                y = j * self.canvas.step

                a = x + self.canvas.step / 2, y
                b = x + self.canvas.step, y + self.canvas.step * 0.5
                c = x + self.canvas.step * 0.5, y + self.canvas.step
                d = x, y + self.canvas.step * 0.5

                p1 = lista[i][j]
                p2 = lista[i+1][j]
                p3 = lista[i+1][j+1]
                p4 = lista[i][j+1]
                state = self.get_state(p1, p2, p3, p4)

                if state == 0:
                    pass
                elif state == 1:
                    self.draw_line(c, d)
                elif state == 2:
                    self.draw_line(c, b)
                elif state == 3:
                    self.draw_line(b,d)
                elif state == 4:
                    self.draw_line(a,b)
                elif state == 5:
                    self.draw_line(d,a)
                    self.draw_line(c,b)
                elif state == 6:
                    self.draw_line(a,c)
                elif state == 7:
                    self.draw_line(d,a)
                elif state == 8:
                    self.draw_line(d,a)
                elif state == 9:
                    self.draw_line(a,c)
                elif state == 10:
                    self.draw_line(a,b)
                    self.draw_line(d,c)
                elif state == 11:
                    self.draw_line(a,b)
                elif state == 12:
                    self.draw_line(d,b)
                elif state == 13:
                    self.draw_line(b,c)
                elif state == 14:
                    self.draw_line(d,c)
                else:
                    pass
