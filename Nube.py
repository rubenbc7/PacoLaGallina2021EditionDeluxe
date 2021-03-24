from glew_wish import *
import glfw
from math import *

class Nube():
    xPos = 0.0
    
    def __init__(self, x):
        self.xPos = x

    def dibujar(self):
        global xPos

        glPushMatrix()
        glTranslate(self.xPos,0,0)
        glBegin(GL_POLYGON)
        glColor3f(1,1,1)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo) * 0.3 + 0.6 , sin(angulo) * 0.06 + 0.4 ,0.0)
        glColor3f(0,0,0)

        glEnd()
        glPopMatrix()
