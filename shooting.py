import pygame
import alpha as a
from PPlay.sprite import *
import math

flag = False
music_notes = []

def shooty():
    if pygame.mouse.get_pressed()[0]:

        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        distance_x = mouse_x - a.player.x
        distance_y = mouse_y - a.player.y
        
        angle = math.atan2(distance_y, distance_x)
        
        speed_x = 4 * math.cos(angle)
        speed_y = 4 * math.sin(angle)
        
        music_notes.append([a.player.x, a.player.y, speed_x, speed_y])


    for item in music_notes:
        item[0] += item[2]
        item[1] += item[3]

    for pos_x, pos_y, speed_x, speed_y in music_notes:
        pos_x = int(pos_x)
        pos_y = int(pos_y)
        pygame.draw.line(a.window, (0,255,0), (pos_x, pos_y), (pos_x, pos_y))