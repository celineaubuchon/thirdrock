import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from shapes import * # script I made that contains drawing functions for shapes


def main():
    pygame.init() # initializes pygame
    display = (800, 600) # width and height of display box
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL) # sets up the display window

    # sets up perspective projection: 
    # viewing angle, aspect ratio, near clipping plane, far clipping plane
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -3.0) # zoom out 
    glRotatef(0.0, 0.0, 0.0, 0.0)

    #infinit loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if user closes the window
                pygame.quit()
                quit()

        # clear color and depth buffers at the beginning of current frame
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glRotatef(1.0, 3.0, 1.0, 0.0)
        sphere(1.0)
        pygame.display.flip() # draw the buffers
        pygame.time.wait(10) # wait 10 millisecs



############################################################################################
main() # calls main function to start the game