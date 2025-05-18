import pygame
from pygame.locals import * # mouse interactions

pygame.init() # enabling pygame

screen_width = 800
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height)) # create a screen

done = False # bool that will be changed to True when we want to quit the game
white = pygame.Color(255, 255, 255)
times_clicked = 0

while not done:
    for event in pygame.event.get(): # for every event that happens pygame.event.get() return list of events
        if event.type == pygame.QUIT: # if the user clicks the close button
            done = True # we want to quit the game
        elif event.type == MOUSEBUTTONDOWN:
            if times_clicked == 0:
                point1 = pygame.mouse.get_pos()
            else:
                point2 = pygame.mouse.get_pos()
            times_clicked += 1
            if times_clicked > 1:
                pygame.draw.line(screen, white, point1, point2, 1)
                times_clicked = 0
        pygame.display.update() # update the screen
pygame.quit()