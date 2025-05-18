import pygame
from pygame.locals import * # mouse interactions

pygame.init() # enabling pygame

screen_width = 1300
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height)) # create a screen

done = False # bool that will be changed to True when we want to quit the game
yellow = pygame.Color(255, 255, 0)
white = pygame.Color(255, 255, 255)

pygame.font.init() # font initialize
print(pygame.font.get_fonts()) # list all system fonts
font = pygame.font.SysFont('Arial', 100)
custom_font = pygame.font.Font('../Resources/Fonts/5x5dots.ttf', 100)


text = font.render('Gienio Galaretka', True, white)
custom_text = custom_font.render('Gienio Galarretka', True, yellow)

while not done:
    for event in pygame.event.get(): # for every event that happens pygame.event.get() return list of events
        if event.type == pygame.QUIT: # if the user clicks the close button
            done = True # we want to quit the game
        screen.blit(text, (28, 28)) # text placing on screen
        screen.blit(custom_text, (28, 28 + font.get_height()))
        pygame.display.update() # update the screen
pygame.quit()