#ID : 18301279
#SECTION : 04

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def DDA(x1, y1, x2, y2):
    m = (y1-y2)/(x1-x2) if x1 != x2 else 1
    glBegin(GL_POINTS)
    glVertex2f(x1, y1)
    if -1 <= m < 1:
        while x1 < x2:
            x1 += 1
            y1 += m
            glVertex2f(x1, round(y1))
    else:
        while y1 < y2:
            y1 += 5
            #x1 += 1/m
            glVertex2f(round(x1), y1)
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

  def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    #call the draw methods here
    iterate()
    DDA(200,200,300,200)
    DDA(200,100,200,300)
    DDA(300, 100, 300, 300)
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()