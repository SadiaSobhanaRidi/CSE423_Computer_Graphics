#ID : 18301279
#SECTION : 04

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def drawDoor():
    glBegin(GL_LINE_LOOP)
    glVertex2f(240, 240)
    glVertex2f(260, 240)
    glVertex2f(260, 200)
    glVertex2f(240, 200)
    glEnd()

    glBegin(GL_POINTS)
    glVertex2f(255.5, 220)
    glEnd()

def drawRoof():
    glPointSize(2)
    glBegin(GL_LINE_LOOP)
    glVertex2f(200, 300)
    glVertex2f(300, 300)
    glVertex2f(250, 375)
    glEnd()

def drawWindows():
    glBegin(GL_LINE_LOOP)
    glVertex2f(220, 280)
    glVertex2f(240, 280)
    glVertex2f(240, 260)
    glVertex2f(220, 260)
    glEnd()
    glBegin(GL_LINE_LOOP)
    glVertex2f(260, 280)
    glVertex2f(280, 280)
    glVertex2f(280, 260)
    glVertex2f(260, 260)
    glEnd()

def drawWall():
    glBegin(GL_LINE_LOOP)
    glVertex2f(200, 300)
    glVertex2f(300, 300)
    glVertex2f(300, 200)
    glVertex2f(200, 200)
    glEnd()
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
    #drawPoints()
    drawRoof()
    drawWall()
    drawWindows()
    drawDoor()

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

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow("OpenGL Template")
glutDisplayFunc(showScreen)

init()

glutMainLoop()