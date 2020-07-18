"""
Procedural cave generator using python3 and pygame

https://en.wikipedia.org/wiki/Marching_squares
"""

import pygame, random
from canvas import Canvas
from event_manager import Event_handler
from points import Point

pygame.init()
display = Canvas()
event = Event_handler()

def generate_points():
    __pontos = []
    for i in range(0, display.width, display.step):
        sub_list = []
        for j in range(0, display.width, display.step):
            sub_list.append(Point(i,j))
        __pontos.append(sub_list)
    return __pontos
    
def draw_points(points_list):
    for i in range(len(points_list)):
        for j in range(len(points_list[0])):
            points_list[i][j].draw(display.canvas)
        
def show_matrix(lista, br):
    for i in range(0, len(lista)):
        print("[{0} {1}]".format(lista[i].x, lista[i].y), end=' ')
        # print('[', lista[i].x, lista[i].y, end='] ')
        if i%br == 0 and i!=(br-1) and i!=0:
            print()

def draw_line(p1, p2):
    line_color = (0, 255, 0)
    line_width = 2
    pygame.draw.line(display.canvas, line_color, [p1[0], p1[1]], [p2[0], p2[1]], line_width)

def get_state(a,b,c,d):
    return ((a.value*8) + (b.value*4) + (c.value*2) + (d.value*1))

def draw_cave(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista[0])-1):
            x = i * display.step
            y = j * display.step
            
            a = x + display.step / 2,   y
            b = x + display.step,       y + display.step * 0.5
            c = x + display.step * 0.5, y + display.step
            d = x,              y + display.step * 0.5
            
            p1 = lista[i][j]
            p2 = lista[i+1][j]
            p3 = lista[i+1][j+1]
            p4 = lista[i][j+1]
            state = get_state(p1, p2, p3, p4)

            

            if state == 0:
                pass
            elif state == 1:
                draw_line(c, d)
            elif state == 2:
                draw_line(c, b)
            elif state == 3:
                draw_line(b,d)
            elif state == 4:
                draw_line(a,b)
            elif state == 5:
                draw_line(d,a)
                draw_line(c,b)
            elif state == 6:
                draw_line(a,c)
            elif state == 7:
                draw_line(d,a)
            elif state == 8:
                draw_line(d,a)
            elif state == 9:
                draw_line(a,c)
            elif state == 10:
                draw_line(a,b)
                draw_line(d,c)
            elif state == 11:
                draw_line(a,b)
            elif state == 12:
                draw_line(d,b)
            elif state == 13:
                draw_line(b,c)
            elif state == 14:
                draw_line(d,c)
            elif state == 15:
                pass
            else:
                print("deu ruim")
                
# display.background()
# display.draw_grid()
lista = generate_points()
draw_points(lista)
draw_cave(lista)


while True:    
    event.manage()
    display.clock.tick(60)
    display.update()
