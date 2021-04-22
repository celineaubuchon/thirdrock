import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import OpenGL.GLUT
from shapes import * # script I made that contains drawing functions for shapes
from AsteroidField import AsteroidField # class representing an asteroid field
from utilities import * # utility functions I wrote to handle general calculations
def draw_title():
    drawText((-1, 0, 0), "thirdrock", (0, 255, 0, 255), 80)

def draw_options(diff):

    if diff == 'easy':
        easy = "X"
        hard = " "
    else:
        easy = " "
        hard = "X"

    drawText((-0.70, -0.75, 0), "[space]", (0, 255,0,255), 64)
    drawText((-1.3, -1.25, 0), "(q) easy[" +easy+"]", (0, 255, 0, 100), 32)
    drawText((0.25, -1.25, 0), "(e) hard[" +hard+"]", (0, 255, 0, 100), 32)

def set_difficulty(easy):
    if easy:
        speed = 0.2
    else:
        speed = 0.5
    return speed

def draw_score(score):
    drawText((-2.5, -2, 0), "score: "+str(score), (0, 255, 0, 255), 32)

def draw_game_over():
    drawText((-1, 0, 0), "game over", (0, 255, 0, 255), 80)

def handle_keypress(event):
    valid = True
    speed = 0.1
    key = event.key
    if event.type == pygame.KEYDOWN:
        # handle key down

        # ship control keys
        if key == K_a:
            x = speed; y = 0.0; valid = True
        elif key == K_d:
            x = -speed; y = 0.0; valid = True
        elif key == K_w:
            x = 0.0; y = -speed; valid = True
        elif key == K_s:
            x = 0.0; y = speed; valid = True
        # menu control keys
        elif key == K_SPACE:
            # press space to start the game
            return(-1, -1, True) 
        elif key == K_q:
            valid = False; x = 0.1; y =-0.1
            # I know this doesnt make much sense, but it is for consistency with this function
        elif key == K_e:
            valid = False; x = -0.1; y = -0.1
        else:
            valid = False; x = 0.0; y = 0.0
    if event.type == pygame.KEYUP:
        x = 0.0; y = 0.0; valid = True
    return (x, y, valid)

def main():
    pygame.init() # initializes pygame
    display = (800, 600) # width and height of display box
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL) # sets up the display window

    # sets up perspective projection: 
    # viewing angle, aspect ratio, near clipping plane, far clipping plane
    gluPerspective(45, (display[0]/display[1]), 0.1, 15.0)

    # set up camera view
    camera_displacement = -5
    glTranslatef(0.0, 0.0, camera_displacement) # zoom out 
    glRotatef(0.0, 0.0, 0.0, 0.0) # not doing anything right now

    #######################################################################################
    #########################         START SCREEN          ###############################
    #######################################################################################
    menu = True
    diff = "easy"
    speed = 0.2
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if user closes the window
                pygame.quit()
                quit()
            if (event.type == pygame.KEYDOWN) or (event.type == pygame.KEYUP):
                [a, b, space] = handle_keypress(event) # a and b are not used
                if space and b < 0:
                    menu = False
                if not space:
                    print("got here", a, b)
                    if a > 0 and b < 0:
                        print("got to easy")
                        diff = "easy"
                        speed = set_difficulty(True)
                    elif a < 0 and b < 0: 
                        print("got to hard")
                        diff = "hard"
                        speed = set_difficulty(False)

        # clear color and depth buffers at the beginning of current frame
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw_title()
        draw_options(diff)
        pygame.display.flip() # draw the buffers
        pygame.time.wait(20) 


    #initialize ship object
    [ship_verts, ship_edges] = load_mesh('objs/ship.obj')
    #initialize asteroid field 
    asteroid_field = AsteroidField(10) # takes in number of asteroids
    #initialize score
    score = 0

    # translates scene (moves the ship through space)
    x = 0.0
    y = 0.0
    z = speed # z represents the speed
    
    # name sounds to be called
    game_music = pygame.mixer.music.load("sounds/game_music.wav")
    collision_sound = pygame.mixer.Sound("sounds/collision.wav")
    collect_sound = pygame.mixer.Sound("sounds/collect.wav")
    game_over_sound = pygame.mixer.Sound("sounds/game_over.wav")

    # start game music
    pygame.mixer.music.play(-1)

    game_over = False
    #######################################################################################
    #########################           GAME PLAY           ###############################
    #######################################################################################
    while not game_over:
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
        # draw score
        draw_score(score)

        # draws and maintains each asteroid
        for asteroid in asteroid_field.asteroids:
            # permanently rotates each vertex about the origin
            asteroid.rotate()

            # check if asteroid left field of view, delete and add a new one if so
            asteroid_field.check_asteroid_status(asteroid, camera_displacement)

            # draws the current asteroid
            asteroid.draw()

            # updates the location of the asteroid center
            asteroid.update_center(x, y, z)

            # checks for collision between ship and current asteroid
            collision = asteroid.detect_collision((0.0, -1.5, 11), 1.0)
            if collision:
                collision_sound.play()
                asteroid.col = (1, 0, 0)
                x = 0; y = 0; z = 0
                game_over = True
                #game_over_sound.play()

        # draw the ship

        for star in asteroid_field.star_particles:
            asteroid_field.check_star_status(star, camera_displacement)
            star.draw()
            star.update_center(x, y, z)

            # checks for collision between ship and current asteroid
            collision = star.detect_collision((0.0, -1.5, 11), 1.0)
            if collision:
                collect_sound.play()
                asteroid_field.del_star(star)
                score += 1
            
        drawShip(ship_verts, ship_edges)

        pygame.display.flip() # draw the buffers
        pygame.time.wait(20) 

        #########################################################################
    #######################################################################################
    #########################           GAME OVER           ###############################
    #######################################################################################
    ticks = pygame.time.get_ticks()
    play_sound = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if user closes the window
                pygame.quit()
                quit()
        if (pygame.time.get_ticks() > 1000 + ticks) and play_sound:
            game_over_sound.play()
            play_sound = False

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        # draw score
        draw_score(score)

        # draws and maintains each asteroid
        for asteroid in asteroid_field.asteroids:
            # permanently rotates each vertex about the origin
            asteroid.rotate()
            asteroid.draw()

        for star in asteroid_field.asteroids:
            star.draw()

        drawShip(ship_verts, ship_edges)

        draw_game_over()

        pygame.display.flip() # draw the buffers
        pygame.time.wait(20) 



############################################################################################
main() # calls main function to start the game