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
                         (-0.5, 0.5, -0.5)]

        self.triangles = [0, 2, 3, 0, 3, 1]
        self.draw_type = GL_LINE_LOOP
        self.texture = pygame.image.load()
        self.texID = 0

    def draw(self):
        glEnable(GL_TEXTURE_2D)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
        glBindTexture(GL_TEXTURE_2D, self.texID)
        for t in range(0, len(self.triangles), 3):
            glBegin(self.draw_type)
            glTexCoord2fv(self.uvs[self.triangles[t]])
            glVertex3fv(self.vertices[self.triangles[t]])
            glTexCoord2fv(self.uvs[self.triangles[t + 1]])
            glVertex3fv(self.vertices[self.triangles[t + 1]])
            glTexCoord2fv(self.uvs[self.triangles[t + 2]])
            glVertex3fv(self.vertices[self.triangles[t + 2]])
            glEnd()

    def int_texture(self):
        self.texID = glGenTextures(1)
        textureData = pygame.image.tostring(self.texture, "RGB", 1)
        width = self.texture.get_width()
        height = self.texture.get_height()
        glBindTexture(GL_TEXTURE_2D, self.texID)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, textureData)

class Cube(Mesh3D):
    def __init__(self, draw_type, filename):
        self.vertices = [(0.5, -0.5, 0.5),
                        (-0.5, -0.5, 0.5),
                        (0.5, 0.5, 0.5),
                        (-0.5, 0.5, 0.5),
                        (0.5, 0.5, -0.5),
                        (-0.5, 0.5, -0.5),
                        (0.5, -0.5, -0.5),
                        (-0.5, -0.5, -0.5),
                        (0.5, 0.5, 0.5),
                        (-0.5, 0.5, 0.5),
                        (0.5, 0.5, -0.5),
                        (-0.5, 0.5, -0.5),
                        (0.5, -0.5, -0.5),
                        (0.5, -0.5, 0.5),
                        (-0.5, -0.5, 0.5),
                        (-0.5, -0.5, -0.5),
                        (-0.5, -0.5, 0.5),
                        (-0.5, 0.5, 0.5),
                        (-0.5, 0.5, -0.5),
                        (-0.5, -0.5, -0.5),
                        (0.5, -0.5, -0.5),
                        (0.5, 0.5, -0.5),
                        (0.5, 0.5, 0.5),
                        (0.5, -0.5, 0.5)]

        self.triangles = [0, 2, 3, 0, 3, 1, 8, 4, 5,
                          8, 5, 9, 10, 6, 7, 10, 7, 11,
                          12, 13, 14, 12, 14, 15, 16, 17, 18,
                          16, 18, 19, 20, 21, 22, 20, 22, 23]

        self.uvs = [(0.0, 0.0),
                   (1.0, 0.0),
                   (0.0, 1.0),
                   (1.0, 1.0),
                   (0.0, 1.0),
                   (1.0, 1.0),
                   (0.0, 1.0),
                   (1.0, 1.0),
                   (0.0, 0.0),
                   (1.0, 0.0),
                   (0.0, 0.0),
                   (1.0, 0.0),
                   (0.0, 0.0),
                   (0.0, 1.0),
                   (1.0, 1.0),
                   (1.0, 0.0),
                   (0.0, 0.0),
                   (0.0, 1.0),
                   (1.0, 1.0),
                   (1.0, 0.0),
                   (0.0, 0.0),
                   (0.0, 1.0),
                   (1.0, 1.0),
                   (1.0, 0.0)]

        Mesh3D.draw_type = draw_type
        Mesh3D.texture = pygame.image.load(filename)

pygame.init()
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL) # use OpenGL for rendering, use double buffer for drawing animated objects
pygame.display.set_caption("OpenGL window")
mesh = Cube(GL_POLYGON, "../Resources/Textures/TCom_Pavement_PaintedConcrete3_512_albedo.tif")
mesh.int_texture()
done = False
white = pygame.Color(255, 255, 255)
glMatrixMode(GL_PROJECTION) # set projection matrix
gluPerspective(30, (screen_width // screen_height), 0.1, 100.0) # set camera FOV, ratio, near and far plane
glMatrixMode(GL_MODELVIEW) # set modelview matrix
#glOrtho(-10, 10, 10, -10, 0.1, 100.0)
glTranslatef(-0.5, -0.5, -10.0) # place camera
glEnable(GL_DEPTH_TEST) # render only what is in front of the camera
glEnable(GL_LIGHTING) # enable enviroment lighting

glLight(GL_LIGHT0, GL_POSITION, (5, 5, 5, 1)) # Creating light source
glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 0, 0, 1.0))
glEnable(GL_LIGHT0) # enable light source

glMaterialfv(GL_FRONT, GL_DIFFUSE, (0, 1, 0, 1.0))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen using bit mask (depth | color)
    glRotatef(0.01, 1, 1, 1)
    mesh.draw()
    pygame.display.flip() # flip = update, switches the rendering buffer
pygame.quit()