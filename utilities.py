import math
from math import cos, sin
import random
import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import OpenGL.GLUT

                   ########################################
####################              UTILITIES               #####################
                   ########################################

    # Holds useful functions that my other files will import

def gen_randXYZ(min, max):
# generates an xyz vector with random values ranging from min to max
    x = random.uniform(min, max)
    y = random.uniform(min, max)
    z = random.uniform(min, max)
    return (x, y, z)

def gen_rotation_mat(rot_vec):
# generates a 3D rotation matrix that rotates by rot_vec, an xyz rotation vectorS
    to_deg = math.pi/180.0
    x = to_deg*rot_vec[0]; y = to_deg*rot_vec[1]; z =  to_deg*rot_vec[2]
    rot_mat = [# source: https://en.wikipedia.org/wiki/Rotation_matrix 
            [cos(z)*cos(y), cos(z)*sin(y)*sin(x) - sin(z)*cos(x), cos(z)*sin(y)*cos(x) + sin(z)*sin(x)],
            [sin(z)*cos(y), sin(z)*sin(y)*sin(x) + cos(z)*cos(x), sin(z)*sin(y)*cos(x) - cos(z)*sin(x)],
            [-sin(y), cos(y)*sin(x), cos(y)*cos(x)]]
    return rot_mat
def gen_translation_mat(vec):
# generates a 3D rotation matrix that rotates by rot_vec, an xyz rotation vectorS
    x = vec[0]; y = vec[1]; z = vec[2]
    trans_mat = [[1, 0, x],
                 [0, 1, y],
                 [0, 0, z]]
    return trans_mat

def apply_transformation(verts, mat):
# applies a tranfomation represented by 'mat' to a list of vertices 'verts'
    for i in range(len(verts)):
        v = verts[i]
        v = np.array([v[0], v[1], v[2]])
        v = np.dot(mat, v)
        v = (v[0], v[1], v[2])
        verts[i] = v
    return verts
def distance3D(vec1, vec2):
# calculates the distance between vec1, and vec2, which are both xyz coord
    x1 = vec1[0]; y1 = vec1[1]; z1 = vec1[2]
    x2 = vec2[0]; y2 = vec2[1]; z2 = vec2[2]

    return ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)**0.5

def drawText(position, textString, color, size):   
# draws text starting at 3D position, thank you https://www.pygame.org/wiki/CrossPlatformTextOpengl 
#  expects 4 channel color out of 255  
    font = pygame.font.Font (None, size)
    textSurface = font.render(textString, True, color, (0,0,0,255))     
    textData = pygame.image.tostring(textSurface, "RGBA", True)     
    glRasterPos3d(*position)     
    glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)

 