
import sys
import os

fanicon_img = os.path.join(sys.path[0]) + "/assets/fan.png"

import pygame as pg
from pygame.locals import *
import random
import time

randy = random

scrnw = 500
scrnh = 150

frametick = 28

framecount = 0

centerpos = scrnw/2, scrnh/2

FPS = pg.time.Clock()

twovec = pg.math.Vector2

pg.init()

LEVELNUM = 0

# Color Set
clr_blue = (0, 0, 255)
clr_blue2 = (152, 255, 255)
clr_red = (255, 0, 0)
clr_red2 = (195, 0, 0)
clr_green = (0, 255, 0)
clr_black = (0, 0, 0)
clr_white = (255, 255, 255)

# Prep Stuff

logo = pg.image.load(fanicon_img)
pg.mixer.init()
pg.display.set_icon(logo)
pg.display.set_caption("PYGAME CPU TEMPERATURE GUI")
screen = pg.display.set_mode((scrnw,scrnh))

#singer = pg.mixer.music.load(music)

#pg.mixer.music.play(2)

verdanafont = pg.font.SysFont("Verdana", 40)

from tempget import *
password = getpass.getpass("Enter your sudo password: ")
print("TEMPERATURE GETTER IS LOADING")

# Misc. Functions

import pygame

def draw_text(surface, text, pos, font_size=24, color=(255, 255, 255), font_name=None, center=False):
    font = pygame.font.Font(font_name, font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    
    if center:
        text_rect.center = pos
    else:
        text_rect.topleft = pos

    surface.blit(text_surface, text_rect)

def CtoF(temp):
        a = temp - 32
        return a * 5 / 9

def truequit():
        pg.quit()
        sys.exit()

# Objects



# Looping Code

def mrloop():
    temp_regular = get_cpu_temp(password)

    if "Error" in temp_regular: 
     print('-----------OH NO! ERROR HAS OCCURED! ' + get_cpu_temp(password))
    
    temp_float = get_cpu_temp_FLOAT(password)
    temp_farenheit = CtoF(temp_float)

    draw_text(screen, temp_regular, centerpos, font_size=48, color=(255, 200, 0), center=True)
    draw_text(screen, str(round(temp_farenheit, 2)) + " F", (scrnw/2, scrnh/2 + 50), font_size=48, color=(255, 200, 0), center=True)
    
    print("AS FLOAT:" + str(temp_float))
          
# Auxillary Event Loop

def auxevents():
    pass
                    
# Run Loop

running = True

while running:

    # Event Handling

        for event in pg.event.get():
            if event.type == pg.QUIT:
                print("BYE BYE!")
                running = False
                pg.quit()
                sys.exit()
                
    # Misc. Things

        screen.fill(clr_red2)
        
        auxevents()

        mrloop()

        pg.display.flip()
        pg.display.update()
        
        FPS.tick(frametick)

        framecount = framecount + 1
