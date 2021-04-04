import math
import random
from OpenGL.GL import *
from OpenGL.GLU import *
from shapes import *
from Asteroid import Asteroid # the Asteroid class


                   ########################################
####################         CLASS: ASTEROID FIELD        #####################
                   ########################################
    
    #   A class to contain all of the information of objects in an asteroid. An
    #   AsteroidField object contains the vertices, edges, and locations  of 
    #   every asteroid in the field, and can be updated to reflect when the locations 
    #   of the asteroids change.


class AsteroidField:
    def __init__(self, density):
        self.density = density
        self.asteroids = self.gen_asteroids()

    def gen_asteroids(self):
        asteroids = []
        for d in range(self.density):
            radius = random.uniform(0.25, 0.35)
            [verts, edges] = gen_icosahedron(radius)
            asteroids.append(Asteroid(verts, edges))
        return asteroids

    def add_asteroid(self):
        [verts, edges] = gen_icosahedron(radius)
        self.asteroids.append(Asteroid(verts, edges))

    def del_asteroid(self, asteroid):
        self.asteroids.remove(asteroid)

