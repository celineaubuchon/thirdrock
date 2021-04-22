import math
import random
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from MeshLoader import MeshLoader
from utilities import *

# note: not all of these functions are used in the program, many were used 
# for testing while the prgram was being developed

                   ########################################
####################                CUBE                  #####################
                   ########################################
def gen_cube():
# Defines vertices and edges for a line drawing of a unit sphere
    vertices = [       # indices
        (-0.5, 0.5, -0.5), #0
        (0.5, 0.5, -0.5),  #1
        (-0.5, -0.5, -0.5),#2
        (0.5, -0.5, -0.5), #3
        (-0.5, 0.5, 0.5),  #4
        (0.5, 0.5, 0.5),   #5
        (-0.5, -0.5, 0.5), #6
        (0.5, -0.5, 0.5)   #7
    ]
    edges = [
        # front lines
        (0, 1), (1, 3), (3, 2), (2, 0),
        # back lines
        (4, 5), (5, 7), (7, 6), (6, 4),
        # top lines
        (0, 4), (1, 5),
        # bottom lines
        (2, 6), (3, 7)
    ]
    return (vertices, edges)

def cube():
    (verts, edges) = gen_cube()
    drawShapeLines(verts, edges)

                   ########################################
####################               SPHERE                 #####################
                   ########################################
def gen_ico_edges(row_length, row_count):
# generates an edge list for an icosphere based on row_length and row_count
    # However, I think I made this for nothing because the ordering of the
    # vertices is specific in this case, and I won't generate that in the 
    # same way. Still, a fun exercise.

    edges = []
    # top
    for i in range(1, row_length + 1):
        edges.append((0, i))

    # mid-rings
    for i in range(1, row_length * row_count + 1):
        if (i % row_length) == 0:
            edges.append((i, i - row_length + 1))
        else:
            edges.append((i, i + 1))
    
    # connect rings
    for i in range(row_count - 1):
        for j in range(row_length):
            first = 1 + i*j + j
            second = 1 + i*j + j + row_length
            if j == row_length - 1:
                1
                edges.append((first, second))
                edges.append((second, first - row_length + 1))
            else:
                edges.append((first, second))
                edges.append((first + 1, second))


    # bottom
    upper = row_count * row_length + 1
    lower = upper - row_length
    for i in range(lower, upper):
        edges.append((i, upper))
    
    return edges
     
def gen_icosahedron(radius):
# generates vertice and edge lists for a basic icosahedron, thank you to 
    ## http://www.songho.ca/opengl/gl_sphere.html for reference on how to do this

    ## FIRST, calculate the vertices of the icosahedron
    PI = 3.1415926
    H_ANGLE = PI / 180 * 72
    V_ANGLE = math.atan(0.5)

    # list of zeros to be populated with the 12 vertices
    vertices = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 

    h_ang1 = -PI/2 - H_ANGLE/2 # start angle for first row
    h_ang2 = -PI/2 # start angle for second row

    # top vertex
    vertices[0] = (0.0, 0.0, radius)

    # 10 vertices of the first and second rows
    for i in range(1, 5 + 1):
        i1 = i; i2 = i + 5; # indices for curr vertex in first and second row

        # x y z values of current vertex
        z = radius * math.sin(V_ANGLE) 
        xy = radius * math.cos(V_ANGLE)

        # first row current vertex
        vertices[i1] = (xy * math.cos(h_ang1), xy * math.sin(h_ang1), z)
        # second row current vertex
        vertices[i2] = (xy * math.cos(h_ang2), xy * math.sin(h_ang2), -z)

        # next horizontal angles
        h_ang1 += H_ANGLE
        h_ang2 += H_ANGLE 
    
    # bottom vertex
    vertices[-1] = (0, 0, -radius)

    ## SECOND, calculate the edges of the icosahedron
    edges = gen_ico_edges(5, 2)

    # return the vertices
    return (vertices, edges)

def sphere(radius):
    (verts, edges) = gen_icosahedron(radius)
    drawShapeLines(verts, edges)

                   ########################################
####################               OBJ MESH               #####################
                   ########################################

def load_mesh(filepath):
    mesh_loader = MeshLoader(filepath)
    [vertices, edges] = mesh_loader.load_mesh()
    return (vertices, edges)

                   ########################################
####################               Asteroid               #####################
                   ########################################

def gen_asteroid():
    [verts, edges] = load_mesh('objs/ico_s2.obj')
    nPerturbations = 4
    wavelength_range = 1
    
    for p in range(nPerturbations):
        for v in range(len(verts)):
            vert = verts[v]
            vert = np.array([vert[0], vert[1], vert[2]])
            [x, y, z] = gen_randXYZ(-0.08, 0.08)
            vert = (vert[0] + x, vert[1] + y, vert[2] + z)
            verts[v] = vert
    return (verts, edges)



                   ########################################
####################                 DRAW                 #####################
                   ########################################

def drawShapeLines(vertices, edges, col):
    glBegin(GL_LINES) # drawing mode lines
    glColor3f(col[0],col[1],col[2]) # set color to green
    for edge in edges:
        for vert in edge:
            curr_v = vertices[vert]
            glVertex3f(curr_v[0], curr_v[1], curr_v[2])
    glEnd()

def drawShip(ship_verts, ship_edges):
    glPushMatrix()
    glScale(0.75, 0.75, 0.75)
    glTranslate(0, -1.5, 0.5)
    drawShapeLines(ship_verts, ship_edges, (0.75, 0.4, 0.6))
    glPopMatrix()