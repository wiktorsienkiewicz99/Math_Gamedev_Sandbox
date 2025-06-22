import pygame
from pygame.locals import *


pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
done = False
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 255)
red = pygame.Color(255, 0, 0)

mouse_dawn = False
last_mouse_pos = (0,0)

while not done:
    pygame.draw.rect(screen, green, (screen_width/2, screen_height/2, 100, 30))
    mx = pygame.mouse.get_pos()[0]
    my = pygame.mouse.get_pos()[1]
    for event in pygame.event.get():
        #print('mx ', mx)
        #print('my ', my)
        #print(event.type)
        if event.type == QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            mouse_dawn = True
            last_mouse_pos = pygame.mouse.get_pos()
        elif event.type == MOUSEBUTTONUP and event.button == 1:
            mouse_dawn = False
        elif event.type == MOUSEMOTION and mouse_dawn:
            pygame.draw.line(screen, white, last_mouse_pos, pygame.mouse.get_pos(), 5)
            last_mouse_pos = pygame.mouse.get_pos()
        if event.type == MOUSEMOTION and screen_width / 2 < mx < screen_width / 2 + 100 and screen_height / 2 < my < screen_height / 2 + 30:
            print('HOVER')
            '''
            if event.button == 1: # use only LMB for drawing
                print("LMB")
                pygame.draw.rect(screen, white, (pygame.mouse.get_pos(), (5,5)))
            if event.button == 2:
                print ("RMB")
                pygame.draw.rect(screen, green, (pygame.mouse.get_pos(), (5,5)))
            if event.button == 4:
                print ("Scroll")
                pygame.draw.rect(screen, red, (pygame.mouse.get_pos(), (5,5)))
            '''

    pygame.display.update()
pygame.quit()