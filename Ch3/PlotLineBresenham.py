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
    dx = abs(x1 - x0)
    if x0 < x1:
        sx = 1
    else:
        sx = -1
    dy = -abs(y1 - y0)
    if y0 < y1:
        sy = 1
    else:
        sy = -1
    err = dx + dy
    while True:
        screen.set_at((x0, y0), white)
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x0 += sx
        if e2 <= dx:
            err += dx
            y0 += sy

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