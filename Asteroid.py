import math
from math import cos, sin
import random
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from shapes import *


                   ########################################
####################            CLASS: ASTEROID           #####################
                   ########################################
    
    #   A class to contain all of the information needed to maintain one asteroid

class Asteroid:
    def __init__(self, verts, edges):
        self.vertices = verts
        self.edges = edges
        self.translation_data = self.gen_randXYZ(-2.0, 2.0)
        self.rotation_data = self.gen_randXYZ(-0.5, 0.5)

    def gen_randXYZ(self, min, max):
        x = random.uniform(min, max)
        y = random.uniform(min, max)
        z = random.uniform(min, max)
        return (x, y, z)

    def rotate(self, ang):
        to_deg = math.pi/180.0
        x = to_deg * ang[0]; y = to_deg * ang[1]; z = to_deg * ang[2]
        rot_mat = [# source: https://en.wikipedia.org/wiki/Rotation_matrix 
            [cos(z)*cos(y), cos(z)*sin(y)*sin(x) - sin(z)*cos(x), cos(z)*sin(y)*cos(x) + sin(z)*sin(x)],
            [sin(z)*cos(y), sin(z)*sin(y)*sin(x) + cos(z)*cos(x), sin(z)*sin(y)*cos(x) - cos(z)*sin(x)],
            [-sin(y), cos(y)*sin(x), cos(y)*cos(x)]]
        
        for i in range(len(self.vertices)):
            v = self.vertices[i]
            v = np.array([v[0], v[1], v[2]])
            v = np.dot(rot_mat, v)
            v = (v[0], v[1], v[2])
            self.vertices[i] = v

    def draw(self):
        drawShapeLines(self.vertices, self.edges)