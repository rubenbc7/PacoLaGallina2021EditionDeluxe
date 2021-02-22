from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *

xObstaculo = 0.0
yObstaculo = -0.6

xPaja = 0.0
yPaja = -0.3

xCarrito = -0.6
yCarrito = -0.35
yrCarrito = 0.0


xPiso = 0.0
yPiso = 0.0

xNube = 0.8

tiempo_anterior = 0

colisionando = False

def checar_colisiones():
    global colisionando
    global xPaja
    global yPaja
    global xCarrito
    global yCarrito 

    #Si extremaDerechaCarrito > extremaIzquiedaObstaculo
    # Y extremaIzquierdaCarrito < extremaDerechaObstaculo
    # Y extremoSuperirorCarrito > extremoInferirorObstaculo
    # Y extremoSuperirorCarrito < extremoInferirorObstaculo
    if xPaja + 0.05 > xCarrito - 0.15 and xPaja - 0.05 < xCarrito + 0.15 and yPaja + 0.05 > yCarrito - 0.15 and yPaja - 0.05 < yCarrito + 0.15:
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
    global xCarrito
    global yCarrito
    global xNube
    global yrCarrito

    tiempo_actual = glfw.get_time()
    tiempo_delta = tiempo_actual - tiempo_anterior


    estadoIzquierda = glfw.get_key(window, glfw.KEY_LEFT)
    estadoDerecha = glfw.get_key(window, glfw.KEY_RIGHT)
    estadoAbajo = glfw.get_key(window, glfw.KEY_DOWN)
    estadoArriba = glfw.get_key(window, glfw.KEY_SPACE)

    if not chocando(xCarrito, yCarrito - 0.01, 0.05, 0.05, xObstaculo, yObstaculo, 1, 0.15):
            yCarrito = yCarrito - 0.01
    
   
    if estadoIzquierda == glfw.PRESS and xCarrito - 0.05 > -1:
        xCarrito = (xCarrito - 0.003)
        if yrCarrito == 0:
            yrCarrito = (yrCarrito - 180)
    if estadoDerecha == glfw.PRESS and xCarrito + 0.05 < 1:
        xCarrito = (xCarrito + 0.003)
        if yrCarrito == -180:
            yrCarrito = 0

    if estadoAbajo == glfw.PRESS and yCarrito - 0.05 > -1:
        if not chocando(xCarrito, yCarrito - 0.01, 0.05, 0.05, xObstaculo, yObstaculo, 1, 0.15):
            yCarrito = yCarrito - 0.03
    if estadoArriba == glfw.PRESS and yCarrito + 0.05 + 0.01 < 1:
        if chocando(xCarrito, yCarrito - 0.01, 0.05, 0.05, xObstaculo, yObstaculo, 1, 0.15):
            yCarrito = (yCarrito + 0.3)
    
    if (xNube > -2):
        xNube = xNube - 0.0001
    else:
        xNube = 0.8

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

def dibujarObstaculo():
    global xObstaculo
    global yObstaculo

    glPushMatrix()
    glTranslate(xObstaculo, yObstaculo,0.0)
    glBegin(GL_QUADS)
    glColor3f(0,0.6,0.1)
    glVertex3f(-1,0.15,0.0)
    glVertex3f(1,0.15,0.0)
    glVertex3f(1,-0.15,0.0)
    glVertex3f(-1,-0.15,0.0)
    glEnd()
    glPopMatrix()

def dibujarPaja():
    global xPaja
    global yPaja
    global colisionando
    
    glPushMatrix()
    glTranslate(xPaja,yPaja,0.0)
    glBegin(GL_QUADS)
    if colisionando == True:
        glColor3f(1.0, 1.0, 1.0)
    else:
        glColor3f(0.0,0.0,1.0)
    glVertex3f(-0.15, 0.15, 0.0)
    glVertex3f(0.15, 0.15, 0.0)
    glVertex3f(0.15, -0.15, 0.0)
    glVertex3f(-0.15, -0.15, 0.0)
    glEnd()
    glPopMatrix()    

#paco
def dibujarCarrito():
    global xCarrito
    global yCarrito
    global yrCarrito

    glPushMatrix()
    glTranslate(xCarrito, yCarrito, 0.0)
    glRotate(yrCarrito,0.0,1.0,0.0)
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

def dibujarNubes():
    global xNube
    glPushMatrix()
    glTranslate(xNube,0,0)
    glBegin(GL_POLYGON)
    glColor3f(1,1,1)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.3 + 0.6 , sin(angulo) * 0.06 + 0.4 ,0.0)
    glColor3f(0,0,0)

    glEnd()
    glPopMatrix()


def dibujarPiso():
    global xPiso
    global yPiso

    glPushMatrix()
    glTranslate(xPiso, yPiso, 0.0)
    glBegin(GL_QUADS)
    glColor3f(1,0.7,0.0)
    glVertex3f(-1,-0.6,0.0)
    glVertex3f(1,-0.6,0.0)
    glVertex3f(1,-1,0.0)
    glVertex3f(-1,-1,0.0)
    glEnd()
    glPopMatrix()

def dibujar():
    #rutinas de dibujo
    dibujarGranero()
    dibujarObstaculo()
    dibujarPiso()
    dibujarSilo()
    dibujarSol()
    dibujarNubes()
    dibujarPaja()
    dibujarCarrito()
    
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