import math
import random
from OpenGL.GL import *
from OpenGL.GLU import *
from shapes import *
from Asteroid import Asteroid # the Asteroid class
from StarParticle import StarParticle # the StarParticle class


                   ########################################
####################         CLASS: ASTEROID FIELD        #####################
                   ########################################
    
    #   A class to contain all of the information of objects in an asteroid. An
    #   AsteroidField object contains the vertices, edges, and locations  of 
    #   every asteroid in the field, and can be updated to reflect when the locations 
    #   of the asteroids change.

    #   Functions are not commented because been written with names that make their 
    #   purpose clear.


class AsteroidField:
    def __init__(self, density):
        self.density = density
        self.asteroids = self.gen_asteroids()
        self.star_particles = []

    def gen_asteroids(self):
        asteroids = []
        for d in range(self.density):
            [verts, edges] = gen_asteroid()
            asteroids.append(Asteroid(verts, edges))
        return asteroids

    def add_asteroid(self):
        [verts, edges] = gen_asteroid()
        asteroid_obj = Asteroid(verts, edges)
        trans_data = asteroid_obj.translation_data
        asteroid_obj.translation_data = (trans_data[0], trans_data[1], abs(trans_data[2]) + -15)
        asteroid_obj.center = asteroid_obj.translation_data
        self.asteroids.append(asteroid_obj)
        # add star particle by chance
        self.add_star_particle()

    def add_star_particle(self):
        chance = random.uniform(0, 1)
        if chance > 0.5:
            (verts, edges) = load_mesh("objs/star_particles.obj")
            star = StarParticle(verts, edges)
            trans_data = star.translation_data
            star.translation_data = (trans_data[0], trans_data[1], abs(trans_data[2]) + -15)
            star.center = star.translation_data
            self.star_particles.append(star)

    def del_asteroid(self, asteroid):
        self.asteroids.remove(asteroid)
    
    def del_star(self, star):
        self.star_particles.remove(star)
    
    def check_asteroid_status(self, asteroid, camera_displacement):
        if(asteroid.center[2] + camera_displacement > abs(camera_displacement) + 1):
            self.del_asteroid(asteroid)
            self.add_asteroid()

    def check_star_status(self, star, camera_displacement):
        if(star.center[2] + camera_displacement > abs(camera_displacement) + 1):
            self.del_star(star)
