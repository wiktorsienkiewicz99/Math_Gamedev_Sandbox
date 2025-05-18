import pygame

pygame.init() # enabling pygame
screen_width = 800
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height)) # create a screen
done = False # bool that will be changed to True when we want to quit the game
while not done:
    for event in pygame.event.get(): # for every event that happens pygame.event.get() return list of events
        if event.type == pygame.QUIT: # if the user clicks the close button
            done = True # we want to quit the game
        for y in range(screen_height):
            for x in range(screen_width):
                screen.set_at((x, y), pygame.Color (int(x/screen_width*255), 0, int(y/screen_height*255)))
        pygame.display.update() # update the screen
pygame.quit()