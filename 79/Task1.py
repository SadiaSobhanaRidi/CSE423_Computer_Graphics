#ID : 18301279
#SECTION : 04

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def FindZone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) >= abs(dy): # zone 0,3,4,7
        if dx>=0 and dy>=0:
            zone = 0
        elif dx<=0 and dy>=0:
            zone = 3
        elif dx >= 0 and dy >= 0:
            zone = 7
        elif dx<=0 and dy<=0:
            zone = 4
    else: # zone 1,2,5,6
        if dx>=0 and dy>=0:
            zone = 1
        elif dx<=0 and dy>=0:
            zone = 2
        elif dx >= 0 and dy >= 0:
            zone = 5
        elif dx<=0 and dy<=0:
            zone = 6
    return zone

def OriginalZone(x, y, zone):
    if zone==1:
        temp = x
        x=y
        y=temp

    elif zone==2:
        temp = x
        x = - y
        y = temp

    elif zone==3:
        x = - x
        y = y

    elif zone == 4:
        x = - x
        y = - y

    elif zone==5:
        temp = x
        x = - y
        y = - temp

    elif zone==6:
        temp = x
        x = y
        y = - temp

    elif zone==7:
        x = x
        y = -y

    return x, y

def ConvertZone(x1, y1, x2, y2, zone):
    if zone == 1:
        temp = x1
        x1 = y1
        y1 = temp
        temp = x2
        x2 = y2
        y2 = temp
    elif zone == 2:
        temp = x1
        x1 = y1
        y1 = - temp
        temp = x2
        x2 = y2
        y2 = - temp
    elif zone == 3:
        x1 = - x1
        y1 = y1
        x2 = - x2
        y2 = y2
    elif zone == 4:
        x1 = - x1
        y1 = - y1
        x2 = - x2
        y2 = - y2
    elif zone == 5:
        temp = x1
        x1 = - y1
        y1 = - temp
        temp = x2
        x2 = - y2
        y2 = - temp
    elif zone == 6:
        temp = x1
        x1 = -y1
        y1 = temp
        temp = x2
        x2 = - y2
        y2 =  temp
    elif zone == 7:
        x1 = x1
        y1 = -y1
        x2 = x2
        y2 = -y2

    return x1, y1, x2, y2

def DrawLine(x1, y1, x2, y2):
    glPointSize(3)
    #glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_POINTS)
    zone = FindZone(x1, y1, x2, y2)
    x1, y1, x2, y2 = ConvertZone(x1, y1, x2, y2, zone)
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    incE = 2 * dy
    incNE = 2 * (dy-dx)
    y = y1

    for x in range(x1, x2 + 1):
        X, Y = OriginalZone(x,y,zone)
        glVertex2f(X, Y)
        if d>0 :
            d = d + incNE
            y = y+1
        else:
            d = d + incE
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
    DrawLine(200,300,250,300)
    DrawLine(250,300,250,200)
    DrawLine(260,300,310,300)
    DrawLine(310, 300, 310, 200)
    DrawLine(260, 300, 260, 250)
    DrawLine(260, 250, 310, 250)

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()