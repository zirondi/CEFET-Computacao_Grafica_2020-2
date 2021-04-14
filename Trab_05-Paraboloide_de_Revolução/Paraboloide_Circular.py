import OpenGL.GLUT as GLUT
import OpenGL.GLU as GLU
import OpenGL.GL as GL
from sys import argv
from math import sin, cos, pi

ROTATION_ANGLE = 0
ANGLE_MODIFIER = 0.5
VERTICES = 3
DX, DY, DZ = 0, 0, 0

BG_COLOR = (0.184, 0.211, 0.250, 1)

SIDES_COLORS = (
    (0.909, 0.254, 0.094),
    (0.298, 0.819, 0.215),
    (0, 0.658, 1)
)

TOP_AND_BOTTOM_COLORS = (0.862, 0.866, 0.882)

def f(i,j):
    
    theta = ( (pi * i) / (n1 -1) ) - (pi / 2)
    phi = 2*pi*j/(n2-1)
    
    x = r * cos(theta) * cos(phi)
    y = r * sin(theta)
    z = r * cos(theta) * sin(phi)

    return x,y**2,z

a = 0
n1 = 50
n2 = 50
r = 2

def prism():
    
    GL.glPushMatrix()
    GL.glTranslatef(0,-1.5,DZ)
    GL.glRotatef(ROTATION_ANGLE,0.0,1.0,0.0)
    GL.glRotatef(-105,1.0,0.0,0.0)
    GL.glRotatef(DX, 1.0, 0.0, 0.0)
    GL.glRotatef(DY, 0.0, 1.0, 0.0)
    

    for i in range(n1):
        #GL.glBegin(GL.GL_QUAD_STRIP)
        GL.glBegin(GL.GL_POINTS)
        for j in range(n2):
            #circulo de baixo 
            # GL.glColor3fv(
            #     ((1.0*i/(n1-1)),
            #     0,
            #     1 - (1.0*i/(n1-1))))

            x, y, z = f(i,j)
            GL.glVertex3f(x,y,z)
            #circulo de cima
            # GL.glColor3fv(
            #     ((1.0*(i+1)/(n1-1)),
            #     0,
            #     1 - (1.0*(i+1)/(n1-1))))
            x, y, z = f(i+1, j)
            GL.glVertex3f(x,y,z)
        GL.glEnd()


    GL.glPopMatrix()


def draw():
    global ROTATION_ANGLE
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
    prism()
    ROTATION_ANGLE = ROTATION_ANGLE + ANGLE_MODIFIER
    GLUT.glutSwapBuffers()
  
def timer(i):
    GLUT.glutPostRedisplay()
    GLUT.glutTimerFunc(10,timer,1)

def special_key_pressed(key, x, y):
    global DX, DY

    if (key == GLUT.GLUT_KEY_LEFT):
        DX -= 1

    elif (key == GLUT.GLUT_KEY_RIGHT):
        DX += 1

    elif (key == GLUT.GLUT_KEY_UP):
        DY += 1

    elif (key == GLUT.GLUT_KEY_DOWN):
        DY -= 1

def key_pressed(key, x, y):
    global ANGLE_MODIFIER, DX, DY

    if key == b'\033':
        GLUT.glutLeaveMainLoop()

    elif key == b' ':
        if(ANGLE_MODIFIER==0):
            ANGLE_MODIFIER = 0.5
        else :
            ANGLE_MODIFIER = 0
    
    elif (key == b'a'):
        DX -= 1

    elif (key == b'd'):
        DX += 1

    elif (key == b'w'):
        DY += 1

    elif (key == b's'):
        DY -= 1

def mouse_click(button, state, x, y):
    global VERTICES, DZ

    if (button == GLUT.GLUT_LEFT_BUTTON and state == GLUT.GLUT_DOWN and VERTICES < 12):
        VERTICES += 1

    elif (button == GLUT.GLUT_RIGHT_BUTTON and state == GLUT.GLUT_DOWN and VERTICES > 3):
        VERTICES -= 1

    elif (button == 3 and state == GLUT.GLUT_DOWN and DZ < 10):
        DZ += 1

    elif (button == 4 and state == GLUT.GLUT_DOWN and DZ > -15):
        DZ -= 1


GLUT.glutInit(argv)
GLUT.glutInitDisplayMode(
                GLUT.GLUT_DOUBLE | 
                GLUT.GLUT_RGBA   | 
                GLUT.GLUT_DEPTH  | 
                GLUT.GLUT_MULTISAMPLE
)

screenWidth = GLUT.glutGet(GLUT.GLUT_SCREEN_WIDTH)
screenHeight = GLUT.glutGet(GLUT.GLUT_SCREEN_HEIGHT)

windowWidth = round(2*screenWidth/3)
windowHeight = round(2*screenHeight/3)


GLUT.glutInitWindowSize(windowWidth,windowHeight)
GLUT.glutInitWindowPosition(
    round((screenWidth - windowWidth)/2),
    round((screenHeight - windowHeight)/2)
)
GLUT.glutCreateWindow("Paraboloide Circular")


GLUT.glutDisplayFunc(draw)
GLUT.glutSpecialFunc(special_key_pressed)
GLUT.glutKeyboardFunc(key_pressed)
GLUT.glutMouseFunc(mouse_click)

GL.glEnable(GL.GL_MULTISAMPLE)
GL.glEnable(GL.GL_DEPTH_TEST)

GL.glClearColor(*BG_COLOR)

GLU.gluPerspective(45,windowWidth/windowHeight,0.1,100.0)
GL.glTranslatef(0.0,0.0,-10)

GLUT.glutTimerFunc(10,timer,1)
GLUT.glutMainLoop()