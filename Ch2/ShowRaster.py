import pygame

pygame.init() # enabling pygame

background = pygame.image.load('../Resources/Images/vaporwave_background.jpg')
falcon = pygame.image.load('../Resources/Images/milenium_sprite.png')

screen_width = background.get_width()
screen_height = background.get_height()
screen = pygame.display.set_mode((screen_width, screen_height)) # create a screen

pygame.display.set_caption('Raster')

done = False # bool that will be changed to True when we want to quit the game

while not done:
    for event in pygame.event.get(): # for every event that happens pygame.event.get() return list of events
        if event.type == pygame.QUIT: # if the user clicks the close button
            done = True # we want to quit the game
        screen.blit(background, (0, 0))
        screen.blit(falcon, (screen_width/2, screen_height - falcon.get_height() * 2))
        pygame.display.update() # update the screen
pygame.quit()