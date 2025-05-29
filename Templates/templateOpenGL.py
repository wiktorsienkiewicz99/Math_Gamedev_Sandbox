import pygame
from pygame.locals import *
from OpenGL.GL import *

pygame.init()
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL) # use OpenGL for rendering, use double buffer for drawing animated objects
pygame.display.set_caption("OpenGL window")
done = False
white = pygame.Color(255, 255, 255)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen using bit mask (depth | color)
    pygame.display.flip() # flip = update, switches the rendering buffer
pygame.quit()