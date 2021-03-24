from glew_wish import *
import glfw
from math import *

class Piso():
    xPos = 0.0
    yPos = 0.0
    
    def __init__(self, x, y):
        self.xPos = x
        self.yPos = y

    def dibujar(self):
        global xPos
        global yPos

        glPushMatrix()
        glTranslate(self.xPos, self.yPos, 0.0)
        glBegin(GL_QUADS)
        glColor3f(1,0.7,0.0)
        glVertex3f(-1,-0.6,0.0)
        glVertex3f(1,-0.6,0.0)
        glVertex3f(1,-1,0.0)
        glVertex3f(-1,-1,0.0)
        glEnd()
        glPopMatrix()

