#ID : 18301279
#SECTION : 04

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    #call the draw methods here
    drawPixel()

    glutSwapBuffers()

# put your drawing codes inside this 'draw' function
def draw_Hline( x1, y1, x2, y2 ):
    glBegin( GL_POINTS )
    glPointSize(2.0)
    if x2 < x1:
        x2, x1 = x1, x2
    for x in range( x1, x2 ):
        glVertex2f( x, y1 )
    glEnd()

def drawPixel():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 1.0)
    import random
    glPointSize(2.0)
    glBegin(GL_POINTS)
    for i in range( 50 ):
        x = random.randint(250,375)
        y = random.randint(250, 375)
        glVertex2f(x, y)
    glEnd()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow("OpenGL Template")
glutDisplayFunc(showScreen)

init()

glutMainLoop()