import pygame
from pygame.locals import *

pygame.init() # enabling pygame
screen_width = 800
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height)) # create a screen
done = False # bool that will be changed to True when we want to quit the game

white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)
point1 = (0, 0)
point2 = (0, 0)
timesClicked = 0

def plot_line(point1, point2):
    if point2[0] < point1[0]:
        point1, point2 = point2, point1
    x0, y0 = point1
    x1, y1 = point2
    if x1 - x0 != 0:
        m = (y1 - y0) / (x1 - x0) # slope calculated from definition
    else: return
    c = y0 - m * x0 # calculation of intersection point with y axis
    for x in range(screen_width):
        y = int(m * x + c) # defined linear equation
        screen.set_at((x, y), white)

while not done:
    for event in pygame.event.get(): # for every event that happens pygame.event.get() return list of events
        if event.type == pygame.QUIT: # if the user clicks the close button
            done = True # we want to quit the game
        elif event.type == MOUSEBUTTONDOWN:
            if timesClicked == 0:
                point1 = pygame.mouse.get_pos()
            else:
                point2 = pygame.mouse.get_pos()
            timesClicked += 1
            if timesClicked > 1:
                plot_line(point1, point2)
                timesClicked = 0
        pygame.display.update() # update the screen
pygame.quit()