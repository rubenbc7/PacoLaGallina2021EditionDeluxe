from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *
import sys
import playsound
import time
from Carrito import *
from Obstaculo import *
from Piso import *
from Nube import *

#llamado a clases
carrito = Carrito()
obstaculo = Obstaculo(0.0 , -0.6)
piso = Piso(0.0 , 0.0)
nube = Nube(0.8)

xPaja = 0.0
yPaja = -0.4
DirPaja = 1
yrPaja = 0.0

xPaja2 = 0.7
yPaja2 = -0.4
DirPaja2 = 1
yrPaja2 = 0.0

xAve = -0.6
yAve = 0.1
DirAve = 1
yrAve = 0.0

xAve2 = 0.8
yAve2 = -0.2
DirAve2 = 1
yrAve2 = 0.0

tiempo_anterior = 0
saltando = 0
vidas=1001



playsound.playsound('music.mp3', False)
print("Porfavor seleccione un numero del 1 al 5 para la dificultad y presione ENTER antes de continuar:")
vmx = (float(input()) / 200)
colisionando = False

angMolino = 0

def checar_colisiones():
    global colisionando
    global xPaja
    global yPaja
    
    global carrito 
    global xAve
    global yAve
    global xAve2
    global yAve2
    global xPaja2
    global yPaja2

    #Si extremaDerechaCarrito > extremaIzquiedaObstaculo
    # Y extremaIzquierdaCarrito < extremaDerechaObstaculo
    # Y extremoSuperirorCarrito > extremoInferirorObstaculo
    # Y extremoSuperirorCarrito < extremoInferirorObstaculo
    if xPaja + 0.05 > carrito.Xpos - 0.05 and xPaja - 0.05 < carrito.Xpos + 0.05 and yPaja + 0.05 > carrito.Ypos - 0.05 and yPaja - 0.05 < carrito.Ypos + 0.05:
        colisionando = True
    elif xAve + 0.05 > carrito.Xpos - 0.05 and xAve - 0.05 < carrito.Xpos + 0.05 and yAve + 0.05 > carrito.Ypos - 0.05 and yAve - 0.05 < carrito.Ypos + 0.05:
        colisionando = True
    elif xAve2 + 0.05 > carrito.Xpos - 0.05 and xAve2 - 0.05 < carrito.Xpos + 0.05 and yAve2 + 0.05 > carrito.Ypos - 0.05 and yAve2 - 0.05 < carrito.Ypos + 0.05:
        colisionando = True
    elif xPaja2 + 0.05 > carrito.Xpos - 0.05 and xPaja2 - 0.05 < carrito.Xpos + 0.05 and yPaja2 + 0.05 > carrito.Ypos - 0.05 and yPaja2 - 0.05 < carrito.Ypos + 0.05:
        colisionando = True

    else:
        colisionando = False


def chocando(x1,y1,w1,h1,x2,y2,w2,h2):
    #si extremaDerechaCarrito > extremaIquierdaCarrito
    if x1 + w1 > x2 - w2 and x1 - w1 < x2 + w2 and y1 + h1 > y2 - h2 and y1 - h1 < y2 + h2:
        return True
    return False

def actualizar(window):
    global tiempo_anterior
    
    global carrito
    global nube
    
    global saltando
    global angMolino

    tiempo_actual = glfw.get_time()
    tiempo_delta = tiempo_actual - tiempo_anterior

    global vmx
    global xPaja
    global xAve
    global DirPaja
    global DirAve
    global yrPaja
    global yrAve
    global xAve2
    global DirAve2
    global yrAve2
    global xPaja2
    global yPaja2
    global yrPaja2
    global DirPaja2

    #PerroAliasElPajas
    if xPaja > 1.6:
        DirPaja =-1
        yrPaja = (yrPaja - 180)
     
    if xPaja < -1.1:
        DirPaja =1
        yrPaja = (yrPaja + 180)
        
    xPaja = (xPaja + vmx * DirPaja) 

    if xPaja2 > 1.5:
        DirPaja2 =-1
        yrPaja2 = (yrPaja2 - 180)
     
    if xPaja2 < -1.3:
        DirPaja2 =1
        yrPaja2 = (yrPaja2 + 180)
        
    xPaja2 = (xPaja2 + vmx * DirPaja2) 

    #Aves
    if xAve > 1.4:
        DirAve =-1
        yrAve = (yrAve - 180)
     
    if xAve < -1.8:
        DirAve =1
        yrAve = (yrAve + 180)
        
    xAve = (xAve + vmx * DirAve)

    if xAve2 > 1.05:
        DirAve2 =-1
        yrAve2 = (yrAve2 - 180)
     
    if xAve2 < -1.3:
        DirAve2 =1
        yrAve2 = (yrAve2 + 180)
        
    xAve2 = (xAve2 + vmx * DirAve2)

    #Paco
    estadoIzquierda = glfw.get_key(window, glfw.KEY_LEFT)
    estadoDerecha = glfw.get_key(window, glfw.KEY_RIGHT)
    estadoAbajo = glfw.get_key(window, glfw.KEY_DOWN)
    estadoArriba = glfw.get_key(window, glfw.KEY_SPACE)

    checar_colisiones()

    if not chocando(carrito.Xpos, carrito.Ypos - 0.01, 0.05, 0.05, obstaculo.Xpos, obstaculo.Ypos, 1, 0.15):
            carrito.Ypos = carrito.Ypos - 0.01

    if estadoIzquierda == glfw.PRESS and carrito.Xpos - 0.05 > -1:
        carrito.Xpos = (carrito.Xpos - vmx)
        if carrito.Yrpos == 0:
            carrito.Yrpos = (carrito.Yrpos - 180)
    if estadoDerecha == glfw.PRESS and carrito.Xpos + 0.05 < 1:
        carrito.Xpos = carrito.Xpos + vmx
        if carrito.Yrpos == -180:
            carrito.Yrpos = 0

    if estadoAbajo == glfw.PRESS and carrito.Ypos - 0.05 > -1 and saltando == 0:
        if not chocando(carrito.Xpos, carrito.Ypos - 0.01, 0.05, 0.05, obstaculo.Xpos, obstaculo.Ypos, 1, 0.15):
            carrito.Ypos = carrito.Ypos - 0.03
    if estadoArriba == glfw.PRESS and carrito.Ypos + 0.05 + 0.01 < 1:
        if chocando(carrito.Xpos, carrito.Ypos - 0.01, 0.05, 0.05, obstaculo.Xpos, obstaculo.Ypos, 1, 0.15):
            saltando = 1

    if saltando == 1:
        carrito.Ypos = carrito.Ypos + 0.06
    if carrito.Ypos >= 0.2:
        saltando = 0
                
    #Nube
    if (nube.xPos > -2):
        nube.xPos = nube.xPos - 0.0001
    else:
        nube.xPos = 0.8
    
    angMolino = angMolino + 0.1

    vmx = vmx + (glfw.get_time() / 100000000000000000000000000000000000000000000000000000) 



def dibujarSilo():
    glPushMatrix()
    glTranslate(0,0,0)
    glBegin(GL_QUADS)
    glColor3f(0.5,0.5,0.5)
    glVertex2f(0.8,-0.45)
    glVertex2f(0.6,-0.45)
    glVertex2f(0.6,0.0)
    glVertex2f(0.8,0.0)
    glEnd()
    glPopMatrix()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.1 + 0.7 , sin(angulo) * 0.1 - 0.0 ,0.0)
    glEnd()


def dibujarSol():
    glColor3f(1,1,0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.2 + 0.5 , sin(angulo) * 0.2 + 0.6 ,0.0)
    glEnd()

def dibujarPaja():
    global xPaja
    global yPaja
    global colisionando
    global yrPaja
    global vidas
    global carrito
    
    if colisionando == True:
        playsound.playsound('uff.mp3', False)
        if vidas > 0:
            vidas = vidas - 1
            carrito.Ypos = carrito.Ypos + 0.3
            if vidas == 11:
                print("Te quedan 2 vidas extra.")
            elif vidas == 7:
             print("Te quedan 1 vidas extra.")
            elif vidas == 3:
             print("No te quedan vidas extra.")
        elif vidas <= 0:
            print("GAME OVER")
            print("Sobreviviste:")
            print(glfw.get_time())
            print("Segundos")
            sys.exit()   
    glPushMatrix()
    glTranslate(xPaja,yPaja,0.0)
    glRotate(yrPaja,0.0,1.0,0.0)

    #perritow
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.5, 0.2)
    glVertex3f(-0.06, 0.02, 0.0)
    glVertex3f(0.03, 0.02, 0.0)
    glVertex3f(0.03, -0.03, 0.0)
    glVertex3f(-0.06, -0.03, 0.0)
    glEnd()

    #pataz
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.5, 0.2)
    glVertex3f(-0.05, -0.04, 0.0)
    glVertex3f(-0.03, -0.04, 0.0)
    glVertex3f(-0.03, -0.05, 0.0)
    glVertex3f(-0.05, -0.05, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.8, 0.5, 0.2)
    glVertex3f(-0.06, -0.03, 0.0)
    glVertex3f(-0.04, -0.03, 0.0)
    glVertex3f(-0.04, -0.05, 0.0)
    glVertex3f(-0.06, -0.05, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.8, 0.5, 0.2)
    glVertex3f(0.02, -0.03, 0.0)
    glVertex3f(0.03, -0.03, 0.0)
    glVertex3f(0.03, -0.05, 0.0)
    glVertex3f(0.02, -0.05, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.8, 0.5, 0.2)
    glVertex3f(0.01, -0.03, 0.0)
    glVertex3f(0.02, -0.03, 0.0)
    glVertex3f(0.02, -0.05, 0.0)
    glVertex3f(0.01, -0.05, 0.0)
    glEnd()

    #collar
    glBegin(GL_QUADS)
    glColor3f(0.6, 0, 0)
    glVertex3f(0.01, 0.03, 0.0)
    glVertex3f(0.03, 0.03, 0.0)
    glVertex3f(0.03, 0.02, 0.0)
    glVertex3f(0.01, 0.02, 0.0)
    glEnd()

    #collaramarillo
    glBegin(GL_QUADS)
    glColor3f(1, 1, 0.2)
    glVertex3f(0.02, 0.02, 0.0)
    glVertex3f(0.03, 0.02, 0.0)
    glVertex3f(0.03, 0.01, 0.0)
    glVertex3f(0.02, 0.01, 0.0)
    glEnd()

    #Cabeza
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.5, 0.2)
    glVertex3f(0.01, 0.05, 0.0)
    glVertex3f(0.06, 0.05, 0.0)
    glVertex3f(0.06, 0.03, 0.0)
    glVertex3f(0.01, 0.03, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.4, 0.2, 0.1)
    glVertex3f(0.05, 0.05, 0.0)
    glVertex3f(0.06, 0.05, 0.0)
    glVertex3f(0.06, 0.04, 0.0)
    glVertex3f(0.05, 0.04, 0.0)
    glEnd()



    glBegin(GL_QUADS)
    glColor3f(0.8, 0.5, 0.2)
    glVertex3f(0.01, 0.07, 0.0)
    glVertex3f(0.05, 0.07, 0.0)
    glVertex3f(0.05, 0.05, 0.0)
    glVertex3f(0.01, 0.05, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.4, 0.2, 0.1)
    glVertex3f(-0.01, 0.07, 0.0)
    glVertex3f(0.02, 0.07, 0.0)
    glVertex3f(0.02, 0.03, 0.0)
    glVertex3f(-0.01, 0.03, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0, 0, 0)
    glVertex3f(0.04, 0.06, 0.0)
    glVertex3f(0.05, 0.06, 0.0)
    glVertex3f(0.05, 0.05, 0.0)
    glVertex3f(0.04, 0.05, 0.0)
    glEnd()
    #cola
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.2, 0.1)
    glVertex3f(-0.07, 0.03, 0.0)
    glVertex3f(-0.05, 0.03, 0.0)
    glVertex3f(-0.05, 0.02, 0.0)
    glVertex3f(-0.07, 0.02, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.4, 0.2, 0.1)
    glVertex3f(-0.08, 0.04, 0.0)
    glVertex3f(-0.06, 0.04, 0.0)
    glVertex3f(-0.06, 0.03, 0.0)
    glVertex3f(-0.08, 0.03, 0.0)
    glEnd()

    glPopMatrix() 

def dibujarPaja2():
    global xPaja2
    global yPaja2
    global colisionando
    global yrPaja2
    global vidas
    global carrito
    
    if colisionando == True:
        if vidas > 0:
            vidas = vidas - 1
            carrito.Ypos = carrito.Ypos + 0.3
            if vidas == 11:
                print("Te quedan 2 vidas extra.")
            elif vidas == 7:
             print("Te quedan 1 vidas extra.")
            elif vidas == 3:
             print("No te quedan vidas extra.")
        elif vidas <= 0:
            print("GAME OVER")
            print("Sobreviviste:")
            print(glfw.get_time())
            print("Segundos")
            sys.exit()  
    glPushMatrix()
    glTranslate(xPaja2,yPaja2,0.0)
    glRotate(yrPaja2,0.0,1.0,0.0)

    #perritow
    glBegin(GL_QUADS)
    glColor3f(0, 0, 0)
    glVertex3f(-0.06, 0.02, 0.0)
    glVertex3f(0.03, 0.02, 0.0)
    glVertex3f(0.03, -0.03, 0.0)
    glVertex3f(-0.06, -0.03, 0.0)
    glEnd()

    #pataz
    glBegin(GL_QUADS)
    glColor3f(1, 1, 1)
    glVertex3f(-0.05, -0.04, 0.0)
    glVertex3f(-0.03, -0.04, 0.0)
    glVertex3f(-0.03, -0.05, 0.0)
    glVertex3f(-0.05, -0.05, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0, 0, 0)
    glVertex3f(-0.06, -0.03, 0.0)
    glVertex3f(-0.04, -0.03, 0.0)
    glVertex3f(-0.04, -0.05, 0.0)
    glVertex3f(-0.06, -0.05, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0, 0, 0)
    glVertex3f(0.02, -0.03, 0.0)
    glVertex3f(0.03, -0.03, 0.0)
    glVertex3f(0.03, -0.05, 0.0)
    glVertex3f(0.02, -0.05, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0, 0, 0)
    glVertex3f(0.01, -0.03, 0.0)
    glVertex3f(0.02, -0.03, 0.0)
    glVertex3f(0.02, -0.05, 0.0)
    glVertex3f(0.01, -0.05, 0.0)
    glEnd()

    #collar
    glBegin(GL_QUADS)
    glColor3f(0.1, 0, 0.8)
    glVertex3f(0.01, 0.03, 0.0)
    glVertex3f(0.03, 0.03, 0.0)
    glVertex3f(0.03, 0.02, 0.0)
    glVertex3f(0.01, 0.02, 0.0)
    glEnd()

    #collaramarillo
    glBegin(GL_QUADS)
    glColor3f(1, 1, 0.2)
    glVertex3f(0.02, 0.02, 0.0)
    glVertex3f(0.03, 0.02, 0.0)
    glVertex3f(0.03, 0.01, 0.0)
    glVertex3f(0.02, 0.01, 0.0)
    glEnd()

    #Cabeza
    glBegin(GL_QUADS)
    glColor3f(0, 0, 0)
    glVertex3f(0.01, 0.05, 0.0)
    glVertex3f(0.06, 0.05, 0.0)
    glVertex3f(0.06, 0.03, 0.0)
    glVertex3f(0.01, 0.03, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.4, 0.2, 0.1)
    glVertex3f(0.05, 0.05, 0.0)
    glVertex3f(0.06, 0.05, 0.0)
    glVertex3f(0.06, 0.04, 0.0)
    glVertex3f(0.05, 0.04, 0.0)
    glEnd()



    glBegin(GL_QUADS)
    glColor3f(0, 0, 0.)
    glVertex3f(0.01, 0.07, 0.0)
    glVertex3f(0.05, 0.07, 0.0)
    glVertex3f(0.05, 0.05, 0.0)
    glVertex3f(0.01, 0.05, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1, 1, 1)
    glVertex3f(-0.01, 0.07, 0.0)
    glVertex3f(0.02, 0.07, 0.0)
    glVertex3f(0.02, 0.03, 0.0)
    glVertex3f(-0.01, 0.03, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1, 1, 0.2)
    glVertex3f(0.04, 0.06, 0.0)
    glVertex3f(0.05, 0.06, 0.0)
    glVertex3f(0.05, 0.05, 0.0)
    glVertex3f(0.04, 0.05, 0.0)
    glEnd()
    #cola
    glBegin(GL_QUADS)
    glColor3f(1, 1, 1)
    glVertex3f(-0.07, 0.03, 0.0)
    glVertex3f(-0.05, 0.03, 0.0)
    glVertex3f(-0.05, 0.02, 0.0)
    glVertex3f(-0.07, 0.02, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1, 1, 1)
    glVertex3f(-0.08, 0.04, 0.0)
    glVertex3f(-0.06, 0.04, 0.0)
    glVertex3f(-0.06, 0.03, 0.0)
    glVertex3f(-0.08, 0.03, 0.0)
    glEnd()

    glPopMatrix() 

def dibujarAve():
    global xAve
    global yAve
    global colisionando
    global yrAve
    global vidas
    global carrito
    
    if colisionando == True:
        if vidas > 0:
            vidas = vidas - 1
            carrito.Ypos = carrito.Ypos + 0.3
            if vidas == 11:
                print("Te quedan 2 vidas extra.")
            elif vidas == 7:
             print("Te quedan 1 vidas extra.")
            elif vidas == 3:
             print("No te quedan vidas extra.")
        elif vidas <= 0:
            print("GAME OVER")
            print("Sobreviviste:")
            print(glfw.get_time())
            print("Segundos")
            sys.exit()   
    
    
    glPushMatrix()
    glTranslate(xAve,yAve,0.0)
    glRotate(yrAve,0.0,1.0,0.0)
    glBegin(GL_POLYGON)
    glColor3f(0.6,0.6,0.5)

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

    glBegin(GL_POLYGON)
    glColor3f(1,1,1)
    glVertex2f(0.01,0.01)
    glVertex2f(0.03,0.01)
    glVertex2f(0.03,0.03)
    glVertex2f(0.01,0.03)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1,0.9,0.25)
    glVertex2f(0.03,0.01)
    glVertex2f(0.05,0.01)
    glVertex2f(0.05,0.02)
    glVertex2f(0.03,0.02)
    glEnd()


    glPopMatrix()  


def dibujarAve2():
    global xAve2
    global yAve2
    global colisionando
    global yrAve2
    global vidas
    global carrito
    
    if colisionando == True:
        if vidas > 0:
            vidas = vidas - 1
            carrito.Ypos = carrito.Ypos + 0.3
            if vidas == 11:
                print("Te quedan 2 vidas extra.")
            elif vidas == 7:
             print("Te quedan 1 vidas extra.")
            elif vidas == 3:
             print("No te quedan vidas extra.")
        elif vidas <= 0:
            print("GAME OVER")
            print("Sobreviviste:")
            print(glfw.get_time())
            print("Segundos")
            sys.exit()  
    
    
    glPushMatrix()
    glTranslate(xAve2,yAve2,0.0)
    glRotate(yrAve2,0.0,1.0,0.0)
    glBegin(GL_POLYGON)
    glColor3f(0.2,0.6,0.8)

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

    glBegin(GL_POLYGON)
    glColor3f(1,1,1)
    glVertex2f(0.01,0.01)
    glVertex2f(0.03,0.01)
    glVertex2f(0.03,0.03)
    glVertex2f(0.01,0.03)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1,0.9,0.25)
    glVertex2f(0.03,0.01)
    glVertex2f(0.05,0.01)
    glVertex2f(0.05,0.02)
    glVertex2f(0.03,0.02)
    glEnd()


    glPopMatrix()  


#paco
def dibujarGranero():
    glPushMatrix()
    glTranslate(0,-0.45,0)
    glBegin(GL_QUADS)
    glColor3f(1,0,0)
    glVertex2f(-0.8,0.0)
    glVertex2f(-0.4,0.0)
    glVertex2f(-0.4,0.3)
    glVertex2f(-0.8,0.3)
    glEnd()
    glPopMatrix()

    #bordeTecho
    glPushMatrix()
    glTranslate(0,-0.45,0)
    glBegin(GL_POLYGON)
    glColor3f(1,1,1)
    glVertex2f(-0.86,0.25)
    glVertex2f(-0.71,0.45)
    glVertex2f(-0.60,0.51)
    glVertex2f(-0.49,0.45)
    glVertex2f(-0.34,0.25)
    glEnd()
    glPopMatrix()

    #techo
    glPushMatrix()
    glTranslate(0,-0.45,0)
    glBegin(GL_POLYGON)
    glColor3f(1,0,0)
    glVertex2f(-0.85,0.25)
    glVertex2f(-0.70,0.45)
    glVertex2f(-0.6,0.50)
    glVertex2f(-0.50,0.45)
    glVertex2f(-0.35,0.25)
    glEnd()
    glPopMatrix()

    #bordeVentana
    glPushMatrix()
    glTranslate(0,-0.45,0)
    glBegin(GL_QUADS)
    glColor3f(1,1,1)
    glVertex2f(-0.66,0.29)
    glVertex2f(-0.54,0.29)
    glVertex2f(-0.54,0.41)
    glVertex2f(-0.66,0.41)
    glEnd()
    glPopMatrix()

    #ventana
    glPushMatrix()
    glTranslate(0,-0.45,0)
    glBegin(GL_QUADS)
    glColor3f(0,0,0)
    glVertex2f(-0.65,0.30)
    glVertex2f(-0.55,0.30)
    glVertex2f(-0.55,0.40)
    glVertex2f(-0.65,0.40)
    glEnd()
    glPopMatrix()

    #marcoPuerta
    glPushMatrix()
    glTranslate(0,-0.45,0)
    glBegin(GL_QUADS)
    glColor3f(1,1,1)
    glVertex2f(-0.71,0.0)
    glVertex2f(-0.49,0.0)
    glVertex2f(-0.49,0.21)
    glVertex2f(-0.71,0.21)
    glEnd()
    glPopMatrix()

    #interiorPuerta
    glPushMatrix()
    glTranslate(0,-0.45,0)
    glBegin(GL_QUADS)
    glColor3f(0,0,0)
    glVertex2f(-0.7,0.0)
    glVertex2f(-0.5,0.0)
    glVertex2f(-0.5,0.2)
    glVertex2f(-0.7,0.2)
    glEnd()
    glPopMatrix()

def dibujarMolino():
    global angMolino

    glPushMatrix()
    glTranslate(0,-0.45,0)

    glBegin(GL_QUADS)
    glColor3f(0.5,0.5,0.5)
    glVertex2f(0.1,0.0)
    glVertex2f(0.07,0.0)
    glVertex2f(0.05,0.5)
    glVertex2f(0.02,0.5)

    glVertex2f(-0.1,0.0)
    glVertex2f(-0.07,0.0)
    glVertex2f(-0.05,0.5)
    glVertex2f(-0.02,0.5)
    
    glVertex2f(0.05,0.5)
    glVertex2f(-0.05,0.5)
    glVertex2f(-0.05,0.45)
    glVertex2f(0.05,0.45)    
    
    glVertex2f(0.05,0.35)
    glVertex2f(-0.05,0.35)
    glVertex2f(-0.05,0.3)
    glVertex2f(0.05,0.3)    

    glVertex2f(0.05,0.25)
    glVertex2f(-0.05,0.25)
    glVertex2f(-0.05,0.2)
    glVertex2f(0.05,0.2)    

    glVertex2f(0.07,0.15)
    glVertex2f(-0.07,0.15)
    glVertex2f(-0.07,0.1)
    glVertex2f(0.07,0.1)  


    glEnd()

    glPopMatrix()

    glPushMatrix()
    glTranslate(0.0,0.05,0.0)
    glRotate(angMolino,0.0,0.0,1.0)
    
    glBegin(GL_QUADS)
    glColor3f(1,0,0)
    glVertex2f(0.01,0.1)
    glVertex2f(-0.01,0.1)
    glVertex2f(-0.01,-0.1)
    glVertex2f(0.01,-0.1)

    glVertex2f(0.1,0.01)
    glVertex2f(-0.1,0.01)
    glVertex2f(-0.1,-0.01)
    glVertex2f(0.1,-0.01)

    glVertex2f(0.075,0.085)
    glVertex2f(0.065,0.1)
    glVertex2f(-0.075,-0.085)
    glVertex2f(-0.065,-0.1)

    glVertex2f(0.075,-0.085)
    glVertex2f(0.065,-0.1)
    glVertex2f(-0.075,0.085)
    glVertex2f(-0.065,0.1)

    glEnd()
    glPopMatrix()



    glPushMatrix()
    glTranslate(0,-0.45,0)
    glBegin(GL_POLYGON)
    glColor3f(0.8,0.8,0.8)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.02 + 0.0 , sin(angulo) * 0.02 + 0.5 ,0.0)
    glEnd()
    glPopMatrix()

def dibujar():

    global carrito
    global obstaculo
    global piso
    global nube
    #rutinas de dibujo
    dibujarMolino()
    dibujarGranero()
    obstaculo.dibujar()
    piso.dibujar()
    dibujarSilo()
    dibujarSol()
    nube.dibujar()
    dibujarPaja()
    dibujarPaja2()
    dibujarAve()
    dibujarAve2()
    carrito.dibujar()
    


    
def main():

    #inicia glfw
    if not glfw.init():
        return
    
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(800,800,"PACO LA GALLINA", None, None)
    
    #Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    #Establecemos el contexto
    glfw.make_context_current(window)

    #Activamos la validación de 
    # funciones modernas de OpenGL
    glewExperimental = True

    #Inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    while not glfw.window_should_close(window):
        #Establece regiond e dibujo
        glViewport(0,0,800,800)
        #Establece color de borrado
        glClearColor(0.0,0.7,1,1)
        #Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Dibujar
        actualizar(window)
        dibujar()

        #Preguntar si hubo entradas de perifericos
        #(Teclado, mouse, game pad, etc.)
        glfw.poll_events()
        #Intercambia los buffers
        glfw.swap_buffers(window)

    #Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #Termina los procesos que inició glfw.init
    glfw.terminate()



if __name__ == "__main__":
    main()
    