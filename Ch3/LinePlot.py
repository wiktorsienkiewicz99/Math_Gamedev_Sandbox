import pygame

pygame.init() # enabling pygame
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height)) # create a screen
done = False # bool that will be changed to True when we want to quit the game

white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)
xOriginOffset = int(screen.get_width()/2)
yOriginOffset = int(screen.get_height()/2)

while not done:
    for event in pygame.event.get(): # for every event that happens pygame.event.get() return list of events
        if event.type == pygame.QUIT: # if the user clicks the close button
            done = True # we want to quit the game
        # X axis
        for x in range(int(-screen.get_width()/2), int(screen.get_width()/2)):
            screen.set_at((x + xOriginOffset,yOriginOffset), green)
        # Y axis
        for y in range(int(-screen.get_height()/2), int(screen.get_height()/2)):
            screen.set_at((xOriginOffset, y + yOriginOffset), green)
        # Linear equasion
        for x in range(int(-screen.get_width()/2), int(screen.get_width()/2)):
            #y = -1 * (2 * x + 4) # standard linear equation (multiplied by -1 because of top left axis' zero)
            #y = int(0.05 * x) - 100 # stairs like shape (a slope is low)
            y = (10 * x) - 100 # gaps are not interpolated
            screen.set_at((x + xOriginOffset, y + yOriginOffset), white)
        pygame.display.update() # update the screen
pygame.quit()