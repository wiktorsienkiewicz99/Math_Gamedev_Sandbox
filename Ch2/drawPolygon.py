import pygame
from pygame.locals import *

pygame.init() # enabling pygame

screen_width = 800
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height)) # create a screen

done = False # bool that will be changed to True when we want to quit the game
white = pygame.Color(255, 255, 255)
timesClicked = 0

while not done:
    for event in pygame.event.get(): # for every event that happens pygame.event.get() return list of events
        if event.type == pygame.QUIT: # if the user clicks the close button
            done = True # we want to quit the game
        elif event.type == MOUSEBUTTONDOWN:
            if timesClicked == 0:
                point1 = pygame.mouse.get_pos()
            elif timesClicked == 1:
                point2 = pygame.mouse.get_pos()
            else:
                point3 = pygame.mouse.get_pos()
            timesClicked += 1
            if timesClicked > 2:
                pygame.draw.polygon(screen, white, (point1, point2, point3))
                timesClicked = 0
        #pygame.draw.polygon(screen, white, ((150, 200), (600, 400), (400, 600)))
        pygame.display.update() # update the screen
pygame.quit()