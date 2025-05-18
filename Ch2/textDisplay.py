import pygame
from pygame.locals import * # mouse interactions

pygame.init() # enabling pygame

screen_width = 800
screen_height = 200
screen = pygame.display.set_mode((screen_width, screen_height)) # create a screen

done = False # bool that will be changed to True when we want to quit the game
white = pygame.Color(255, 255, 255)

pygame.font.init() # font initialize
print(pygame.font.get_fonts()) # list all system fonts
font = pygame.font.SysFont('Arial', 100)

text = font.render('Gienio Galaretka', True, white)

while not done:
    for event in pygame.event.get(): # for every event that happens pygame.event.get() return list of events
        if event.type == pygame.QUIT: # if the user clicks the close button
            done = True # we want to quit the game
        screen.blit(text, (28, 28)) # text placing on screen
        pygame.display.update() # update the screen
pygame.quit()