import pygame
from pygame import gfxdraw
import math


pygame.init() # enabling pygame
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height)) # create a screen
pygame.display.set_caption('Circle')
done = False # bool that will be changed to True when we want to quit the game

white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)
red = pygame.Color(255, 0, 0)

def circle_points(x, y, center):
    screen.set_at((x + center[0], y + center[1]), white)
    screen.set_at((y + center[0], x + center[1]), white)
    screen.set_at((-x + center[0], y + center[1]), white)
    screen.set_at((-y + center[0], x + center[1]), white)
    screen.set_at((-x + center[0], -y + center[1]), white)
    screen.set_at((-y + center[0], -x + center[1]), white)
    screen.set_at((x + center[0], -y + center[1]), white)
    screen.set_at((y + center[0], -x + center[1]), white)

def draw_circle(center, radius):
    x = 0
    y = radius
    d = 5/4.0 - radius
    circle_points(x,y,center)
    while y > x:
        if d < 0:
            d = d + 2 * x + 3
            x += 1
        else:
            d = d + 2 * (x - y) + 5
            x = x + 1
            y = y - 1
        circle_points(x,y,center)
while not done:
    for event in pygame.event.get(): # for every event that happens pygame.event.get() return list of events
        if event.type == pygame.QUIT: # if the user clicks the close button
            done = True # we want to quit the game
        draw_circle(radius=50, center=(200, 200))
        pygame.draw.circle(screen, green, (200, 100), 50)
        pygame.gfxdraw.circle(screen, 300, 100, 50, red)
        pygame.display.update() # update the screen
pygame.quit()