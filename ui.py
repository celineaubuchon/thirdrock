import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from shapes import * # script I made that contains drawing functions for shapes
from AsteroidField import AsteroidField # class representing an asteroid field
from utilities import *

def main():

    pygame.init() # initializes pygame
    display = (800, 600) # width and height of display box
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL) # sets up the display window

    # sets up perspective projection: 
    # viewing angle, aspect ratio, near clipping plane, far clipping plane
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5.0) # zoom out 
    glRotatef(0.0, 0.0, 0.0, 0.0) # not doing anything right now

    #initialize asteroid field 
    asteroid_field = AsteroidField(15) # takes in number of asteroids

    #infinite loop
    while True:
        ############################ MANAGE EVENTS ##############################
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if user closes the window
                pygame.quit()
                quit()
        #########################################################################
        ############################ DRAW GL SCENE ##############################
        
        # clear color and depth buffers at the beginning of current frame
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        # translates scene (moves the ship through space)
        #glTranslatef(0.0, 0.0, 0.01) # speed is set by z, x and y could be used for steering?
        
        # draws each asteroid
        # for asteroid in asteroid_field.asteroids:
        #     (r_x, r_y, r_z) = asteroid.rotation_data
        #     (t_x, t_y, t_z) = asteroid.translation_data

        #     # permanently rotates each vertex about the origin
        #     asteroid.rotate((r_x, r_y, r_z))

        #     # draws the current asteroid
        #     glPushMatrix()
        #     glTranslatef(t_x, t_y, t_z) # translates it to its location in space
        #     asteroid.draw() # draws it
        #     modelview = glGetFloatv(GL_MODELVIEW_MATRIX)
        #     glPopMatrix()
        glRotatef(1, 0, 3, 1)
        sphere(1)
        pygame.display.flip() # draw the buffers
        pygame.time.wait(20) # wait 20 millisecs
        #########################################################################


############################################################################################
main() # calls main function to start the game