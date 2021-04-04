import math
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *


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
    edges = [
        (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), # top to mid section edges
        (1, 2), (2, 3), (3, 4), (4, 5), (5, 1), # first row connecting edges
        (6, 7), (7, 8), (8, 9), (9, 10), (10, 6), # second row connecting edges
        # connecting row edges
        (1, 6), (2, 6), (2, 7), (3, 7), (3, 8), (4, 8), (4, 9), (5, 9), (5, 10), (10, 1),
        (6, 11), (7, 11), (8, 11), (9, 11), (10, 11) # mid section to bottom edges
    ]
    edges = gen_ico_edges(5, 2)

    # return the vertices
    return (vertices, edges)
def gen_icosphere(radius, subdivs):
    # get vertices for icosehedron
    verts = gen_icosahedron(radius)[0]


def sphere(radius):
    (verts, edges) = gen_icosahedron(radius)
    drawShapeLines(verts, edges)


                   ########################################
####################                 DRAW                 #####################
                   ########################################

def drawShapeLines(vertices, edges):
    glBegin(GL_LINES) # drawing mode lines
    glColor3f(0,1,0) # set color to green
    for edge in edges:
        for vert in edge:
            curr_v = vertices[vert]
            glVertex3f(curr_v[0], curr_v[1], curr_v[2])
    glEnd()
