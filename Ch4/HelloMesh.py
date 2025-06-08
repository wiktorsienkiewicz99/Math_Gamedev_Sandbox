import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class Mesh3D:
    def __init__(self):
        self.vertices = [(0.5, -0.5, 0.5),
                         (-0.5, -0.5, 0.5),
                         (0.5, 0.5, 0.5),
                         (-0.5, 0.5, 0.5),
                         (0.5, 0.5, -0.5),
                         (-0.5, 0.5, -0.5)
                         ]
        self.triangles = [0, 2, 3, 0, 3, 1]

    def draw(self):
        for t in range(0, len(self.triangles), 3):
            glBegin(GL_LINE_LOOP)
            glVertex3fv(self.vertices[self.triangles[t]])
            glVertex3fv(self.vertices[self.triangles[t + 1]])
            glVertex3fv(self.vertices[self.triangles[t + 2]])
            glEnd()

class Cube3D(Mesh3D):
    def __init__(self):
        self.vertices = [
            (1, 1, 1),  # 0
            (0, 0, 1),  # 1
            (1, 0, 1),  # 2
            (0, 1, 1),  # 3
            (1, 1, 0),  # 4
            (0, 0, 0),  # 5
            (1, 0, 0),  # 6
            (0, 1, 0)  # 7
        ]

        self.triangles = [
            # Front face (z = 1)
            0, 2, 3,
            2, 1, 3,

            # Back face (z = 0)
            4, 7, 6,
            4, 5, 7,

            # Left face (x = 0)
            3, 1, 5,
            3, 5, 7,

            # Right face (x = 1)
            0, 4, 2,
            2, 4, 6,

            # Top face (y = 1)
            0, 3, 4,
            3, 7, 4,

            # Bottom face (y = 0)
            1, 2, 5,
            2, 6, 5
        ]

mesh = Cube3D()

pygame.init()
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL) # use OpenGL for rendering, use double buffer for drawing animated objects
pygame.display.set_caption("OpenGL window")
done = False
white = pygame.Color(255, 255, 255)
# use floating point division to keep the aspect ratio intact
gluPerspective(30, (screen_width / screen_height), 0.1, 100.0) # set camera FOV, ratio, near and far plane
glOrtho(-10, 10, 10, -10, 0.1, 100.0)
glTranslatef(-0.5, -0.5, -10.0) # place camera

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen using bit mask (depth | color)
    glRotatef(0.01, 1, 1, 1)
    mesh.draw()
    pygame.display.flip() # flip = update, switches the rendering buffer
pygame.quit()
