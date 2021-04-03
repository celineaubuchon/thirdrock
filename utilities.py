import math
from math import cos, sin
import random
import numpy as np

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