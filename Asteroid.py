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
        self.translation_data = gen_randXYZ(-2.0, 2.0)
        self.rotation_data = gen_randXYZ(-0.5, 0.5)
        # set random location in space
        #apply_transformation(self.vertices, \
            #gen_translation_mat(gen_randXYZ(-2.0, 2.0)))

    def rotate(self, ang):
    # rotates asteroid by ang, and xyz rotation vector
        rot_mat = gen_rotation_mat(ang)
        apply_transformation(self.vertices, rot_mat)

    def draw(self):
        drawShapeLines(self.vertices, self.edges)