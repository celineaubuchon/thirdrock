import math
from math import cos, sin
import random
import numpy as np

                   ########################################
####################           CLASS: MESH LOADER         #####################
                   ########################################
    
    #   A class to load in a mesh from an obj file.

class MeshLoader:
    def __init__(self, filepath):
        self.filepath = filepath
    
    def load_mesh(self):
        verts = []
        edges = []
        f = open(self.filepath, 'r') # opens the obj file to read it
        for line in f:
            print(line)
            line = line.strip('\n').split(' ')
            if line[0] == 'v':
                [x, y, z] = line[1:]
                verts.append((float(x),float(y),float(z)))
            if line[0] == 'f':
                [one, two, three] = line[1:]
                edges.append((int(one) -1, int(two) -1))
                edges.append((int(two) -1, int(three) -1))
                edges.append((int(three) -1, int(one) -1))
        
        return [verts, edges]