import math
from math import cos, sin
import random
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from shapes import *
from utilities import *


                   ########################################
####################            CLASS: ASTEROID           #####################
                   ########################################
    
    #   A class to contain all of the information needed to maintain one asteroid

class Asteroid:
    def __init__(self, verts, edges):
        self.vertices = verts
        self.edges = edges
        self.translation_data = gen_randXYZ(-6.0, 6.0)
        self.rotation_data = gen_randXYZ(-0.5, 0.5)
        self.scale_data = gen_randXYZ(0.25, 0.45)
        self.center = self.translation_data
        self.col = (0, 1, 0)
        
    def rotate(self):
    # rotates asteroid by ang, and xyz rotation vector
        ang = self.rotation_data
        rot_mat = gen_rotation_mat(ang)
        apply_transformation(self.vertices, rot_mat)

    def detect_collision(self, vec, rad):
    # checks if the point defined by vec is within radius rad of the 
    # asteroid
        dist = distance3D(vec, self.center)
        
        return (dist < rad)

    def update_center(self, x, y, z):
    # updates the center of the asteroid to reflect the new location
        c = self.center
        self.center = (c[0] + x, c[1] + y, c[2] + z)
        (t_x, t_y, t_z) = self.translation_data
        self.translation_data = (t_x + x, t_y + y, t_z + z)

    def draw(self):
        (s_x, s_y, s_z) = self.scale_data
        (t_x, t_y, t_z) = self.translation_data
        glPushMatrix()
        glScalef(s_x, s_y, s_z)
        glTranslatef(t_x, t_y, t_z) # translates it to its location in space
        drawShapeLines(self.vertices, self.edges, self.col)
        glPopMatrix()