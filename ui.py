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
    gluPerspective(45, (display[0]/display[1]), 0.1, 15.0)

    camera_displacement = -5
    glTranslatef(0.0, 0.0, camera_displacement) # zoom out 
    glRotatef(0.0, 0.0, 0.0, 0.0) # not doing anything right now

    #initialize asteroid field 
    asteroid_field = AsteroidField(10) # takes in number of asteroids

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
        z = 0.1
        #glTranslatef(0.0, 0.0, z) # speed is set by z, x and y could be used for steering?
        
        gone = 0
        # draws each asteroid
        for asteroid in asteroid_field.asteroids:
            (r_x, r_y, r_z) = asteroid.rotation_data
            (s_x, s_y, s_z) = asteroid.scale_data
            (t_x, t_y, t_z) = asteroid.translation_data

            # permanently rotates each vertex about the origin
            asteroid.rotate((r_x, r_y, r_z))

            # updates the location of the asteroid center
            c = asteroid.center
            asteroid.center = (c[0], c[1], c[2] + z)
            asteroid.translation_data = (t_x, t_y, t_z + z)
            # ugh, I just had a sign error but now its working
            if(asteroid.center[2] + camera_displacement > 5):
                asteroid_field.del_asteroid(asteroid)
                asteroid_field.add_asteroid()
            # draws the current asteroid
            glPushMatrix()
            glScalef(s_x, s_y, s_z)
            glTranslatef(t_x, t_y, t_z) # translates it to its location in space
            asteroid.draw() # draws it
            glPopMatrix()
        #print(asteroid_field.asteroids[0].center)
        pygame.display.flip() # draw the buffers
        pygame.time.wait(20) 
        #########################################################################


############################################################################################
main() # calls main function to start the game