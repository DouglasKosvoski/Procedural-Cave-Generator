"""
Douglas Kosvoski
Procedural cave generator using python3 and pygame
https://en.wikipedia.org/wiki/Marching_squares
"""

import pygame, random
from event_manager import Event_handler
from marching_squares import MarchingSquares
from canvas import Canvas

pygame.init()
event = Event_handler()
display = Canvas()
ms = MarchingSquares(display)


display.background()
lista = ms.generate_points()
ms.draw_points(lista)
ms.draw_cave(lista)

while True:
    event.manage()
    display.clock.tick(30)
    display.update()
