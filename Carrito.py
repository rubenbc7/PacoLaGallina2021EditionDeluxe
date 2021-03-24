from glew_wish import *
import glfw
from math import *

class Carrito():
    Xpos = -0.6
    Ypos = -0.35
    Yrpos = 0.0

    def dibujar(self):
        global Xpos
        global Ypos
        global Yrpos
        
        glPushMatrix()
        glTranslate(self.Xpos, self.Ypos, 0.0)
        glRotate(self.Yrpos,0.0,1.0,0.0)
        glBegin(GL_POLYGON)
        glColor3f(1,1,1)

        #cuerpo
        glVertex3f(-0.05,0.01,0.0)
        glVertex3f(0.03,0.01,0.0)
        glVertex3f(0.03,-0.02,0.0)
        glVertex3f(-0.04,-0.02,0.0)

        glVertex3f(-0.04,-0.02,0.0)
        glVertex3f(0.02,-0.02,0.0)
        glVertex3f(0.02,-0.03,0.0)
        glVertex3f(-0.02,-0.03,0.0)
        glEnd()

        #patas
        glBegin(GL_POLYGON)
        glColor3f(1,0.9,0.25)
        glVertex2f(0.0,-0.03)
        glVertex2f(0.01,-0.03)
        glVertex2f(0.01,-0.06)
        glVertex2f(0.00,-0.06)
        glEnd()
        
        glBegin(GL_POLYGON)
        glVertex2f(-0.02,-0.03)
        glVertex2f(-0.01,-0.03)
        glVertex2f(-0.01,-0.06)
        glVertex2f(-0.02,-0.06)
        glEnd()

        #cabeza
        glBegin(GL_POLYGON)
        glColor3f(1,1,1)
        glVertex2f(0.01,0.01)
        glVertex2f(0.03,0.01)
        glVertex2f(0.03,0.03)
        glVertex2f(0.01,0.03)
        glEnd()

        #cresta
        glBegin(GL_POLYGON)
        glColor3f(1,0,0)
        glVertex2f(0.01,0.03)
        glVertex2f(0.04,0.03)
        glVertex2f(0.04,0.04)
        glVertex2f(0.01,0.04)
        glEnd()

        #pico
        glBegin(GL_POLYGON)
        glColor3f(1,0.9,0.25)
        glVertex2f(0.03,0.01)
        glVertex2f(0.05,0.01)
        glVertex2f(0.05,0.02)
        glVertex2f(0.03,0.02)
        glEnd()

        #barbilla
        glBegin(GL_POLYGON)
        glColor3f(1,0,0)
        glVertex2f(0.03,0.01)
        glVertex2f(0.04,0.01)
        glVertex2f(0.04,0.00)
        glVertex2f(0.03,0.00)
        glEnd()

        #cola
        glBegin(GL_POLYGON)
        glColor3f(1,1,1)
        glVertex2f(-0.02,0.01)
        glVertex2f(-0.05,0.01)
        glVertex2f(-0.045,0.015)
        glVertex2f(-0.02,0.015)
        glEnd()


        glPopMatrix()

