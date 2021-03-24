from glew_wish import *
import glfw
from math import *

class Obstaculo():
    Xpos = 0.0
    Ypos = 0.0

    def __init__(self, x, y):
        self.Xpos = x
        self.Ypos = y

    def dibujar(self):
        global Xpos
        global Ypos

        glPushMatrix()
        glTranslate(self.Xpos, self.Ypos, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0,0.6,0.1)
        glVertex3f(-1,0.15,0.0)
        glVertex3f(1,0.15,0.0)
        glVertex3f(1,-0.15,0.0)
        glVertex3f(-1,-0.15,0.0)
        glEnd()
        glPopMatrix()
