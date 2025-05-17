import pygame

# Initialization
pygame.init() #enabling pygame

# Configuration
screen_width = 800
screen_height = 640

# Convert carthesian to pygame coordinates
def to_pygame_corrdinates(display, x, y):
    return x, display.get_height() - y # convert from carthesian to pygame by subtracting y from screen height

# Draw a star at given coordinates
def draw_star(x, y, size):
    pygame.draw.rect(screen, white, (x, y, size, size))

# Draw a constellation of stars
def draw_constellation(positions):
    for position in positions:
        draw_star(position[0], position[1], 10)

screen = pygame.display.set_mode((screen_width, screen_height)) # create a screen
done = False # bool that will be changed to True when we want to quit the game
white = pygame.Color(255, 255, 255)
while not done:
    for event in pygame.event.get(): # for every event that happens pygame.event.get() return list of events
        if event.type == pygame.QUIT: # if the user clicks the close button
            done = True # we want to quit the game
        #screen.set_at(to_pygame_corrdinates(screen, 100, 100), white) # draw a white pixel on given coordinates
        #screen.set_at(to_pygame_corrdinates(screen, 200, 200), white)
        positions = [(150, 50),(240, 150), (250, 200), (500, 330), (245, 370)] # cancer constellation coordinates
        draw_constellation(positions)
        pygame.display.update() # update the screen
pygame.quit()