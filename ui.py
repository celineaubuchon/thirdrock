import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from shapes import * # script I made that contains drawing functions for shapes
from AsteroidField import AsteroidField # class representing an asteroid field
from utilities import *
def handle_keypress(event):
    valid = True
    speed = 0.1
    key = event.key
    if event.type == pygame.KEYDOWN:
        # handle key down
        if key == K_a:
            x = speed; y = 0.0
        elif key == K_d:
            x = -speed; y = 0.0
        elif key == K_w:
            x = 0.0; y = -speed
        elif key == K_s:
            x = 0.0; y = speed
        else:
            valid = False; x = 0.0; y = 0.0
    if event.type == pygame.KEYUP:
        x = 0.0; y = 0.0
    return (x, y, valid)
            
        
    
    return (x, y)
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

    #initialize ship object
    [ship_verts, ship_edges] = load_mesh('objs/ship.obj')
    #initialize asteroid field 
    asteroid_field = AsteroidField(10) # takes in number of asteroids

    # translates scene (moves the ship through space)
    x = 0.0
    y = 0.0
    z = 0.2
    #infinite loop
    while True:
    
        ############################ MANAGE EVENTS ##############################
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if user closes the window
                pygame.quit()
                quit()
            if (event.type == pygame.KEYDOWN) or (event.type == pygame.KEYUP):
                [new_x, new_y, valid] = handle_keypress(event)
                if valid:
                    x = new_x; y = new_y
        #########################################################################
        ############################ DRAW GL SCENE ##############################
        
        # clear color and depth buffers at the beginning of current frame
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        # draws each asteroid
        for asteroid in asteroid_field.asteroids:
            (r_x, r_y, r_z) = asteroid.rotation_data
            (s_x, s_y, s_z) = asteroid.scale_data
            (t_x, t_y, t_z) = asteroid.translation_data

            # permanently rotates each vertex about the origin
            asteroid.rotate((r_x, r_y, r_z))

            # check is asteroid left field of view, delete and add a new one if so
            if(asteroid.center[2] + camera_displacement > abs(camera_displacement) + 1):
                asteroid_field.del_asteroid(asteroid)
                asteroid_field.add_asteroid()

            # draws the current asteroid
            glPushMatrix()
            glScalef(s_x, s_y, s_z)
            glTranslatef(t_x, t_y, t_z) # translates it to its location in space
            asteroid.draw() # draws it
            glPopMatrix()

            # updates the location of the asteroid center
            c = asteroid.center
            asteroid.center = (c[0] + x, c[1] + y, c[2] + z)
            asteroid.translation_data = (t_x + x, t_y + y, t_z + z)

            # checks for collision between ship and current asteroid
            collision = asteroid.detect_collision((0.0, -1.5, 11), 1.0)
            if collision:
                asteroid.col = (1, 0, 0)
                x = 0; y = 0; z = 0

        
        # draw the ship
        glPushMatrix()
        glScale(0.75, 0.75, 0.75)
        glTranslate(0, -1.5, 0.5)
        drawShapeLines(ship_verts, ship_edges, (0.75, 0.4, 0.6))
        glPopMatrix()

        pygame.display.flip() # draw the buffers
        pygame.time.wait(20) 
        #########################################################################


############################################################################################
main() # calls main function to start the game