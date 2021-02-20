from OpenGL.GL import *
from glew_wish import *
import glfw
import time
import datetime

xObstaculo = 0.0
yObstaculo = -0.6

xCarrito = 0.0
yCarrito = 0.0

xPiso = 0.0
yPiso = 0.0

colisionando = False

def chocando(x1,y1,w1,h1,x2,y2,w2,h2):
    #si extremaDerechaCarrito > extremaIquierdaCarrito
    if x1 + w1 > x2 - w2 and x1 - w1 < x2 + w2 and y1 + h1 > y2 - h2 and y1 - h1 < y2 + h2:
        return True
    return False

def actualizar(window):
    global xCarrito
    global yCarrito
    
    estadoIzquierda = glfw.get_key(window, glfw.KEY_LEFT)
    estadoDerecha = glfw.get_key(window, glfw.KEY_RIGHT)
    estadoAbajo = glfw.get_key(window, glfw.KEY_DOWN)
    estadoArriba = glfw.get_key(window, glfw.KEY_SPACE)

    if not chocando(xCarrito, yCarrito - 0.01, 0.05, 0.05, xObstaculo, yObstaculo, 1, 0.15):
            yCarrito = yCarrito - 0.01
    
   
    if estadoIzquierda == glfw.PRESS and xCarrito - 0.05 > -1:
        xCarrito = xCarrito - 0.03
    if estadoDerecha == glfw.PRESS and xCarrito + 0.05 < 1:
        xCarrito = xCarrito + 0.03
    if estadoAbajo == glfw.PRESS and yCarrito - 0.05 > -1:
        if not chocando(xCarrito, yCarrito - 0.01, 0.05, 0.05, xObstaculo, yObstaculo, 1, 0.15):
            yCarrito = yCarrito - 0.03
    if estadoArriba == glfw.PRESS and yCarrito + 0.05 + 0.01 < 1:
        if chocando(xCarrito, yCarrito - 0.01, 0.05, 0.05, xObstaculo, yObstaculo, 1, 0.15):
            yCarrito = (yCarrito + 0.4) 
    

def dibujarObstaculo():
    global xObstaculo
    global yObstaculo
    glPushMatrix()

    glTranslate(xObstaculo, yObstaculo,0.0)
    glBegin(GL_QUADS)
    glColor3f(1.0,0.5,0.6)
    glVertex3f(-1,0.15,0.0)
    glVertex3f(1,0.15,0.0)
    glVertex3f(1,-0.15,0.0)
    glVertex3f(-1,-0.15,0.0)
    glEnd()
    glPopMatrix()

def dibujarCarrito():
    global xCarrito
    global yCarrito

    glPushMatrix()
    glTranslate(xCarrito, yCarrito, 0.0)
    glBegin(GL_TRIANGLES)
  
    glColor3f(0.8,0.8,0.1)
    glVertex3f(0.0,0.05,0.0)
    glVertex3f(-0.05,-0.05,0.0)
    glVertex3f(0.05,-0.05,0.0)
    glEnd()
    glPopMatrix()

def dibujarPiso():
    global xPiso
    global yPiso

    glPushMatrix()
    glTranslate(xPiso, yPiso, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0,0.5,0.6)
    glVertex3f(-1,-0.6,0.0)
    glVertex3f(1,-0.6,0.0)
    glVertex3f(1,-1,0.0)
    glVertex3f(-1,-1,0.0)
    glEnd()
    glPopMatrix()


def dibujar():
    #rutinas de dibujo
    dibujarObstaculo()
    dibujarPiso()
    dibujarCarrito()

def main():
    #inicia glfw
    if not glfw.init():
        return
    
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(800,800,"Mi ventana", None, None)

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
        glClearColor(0.2,0.2,0.7,1)
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