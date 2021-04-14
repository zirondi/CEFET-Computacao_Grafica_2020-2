import OpenGL.GLUT as GLUT
import OpenGL.GLU as GLU
import OpenGL.GL as GL
from sys import argv
from math import sin, cos, pi

# Window Name
window_name = "Prismas e Piramides"

# Rotation vars
left_button = False
alpha = 0
beta = 0
delta_alpha = 0.5

# Translation vars
right_button = False
delta_x, delta_y, delta_z = 0, 0, 0

down_x, down_y = 0, 0

# Colors
sides_colors = (
    (0.909, 0.254, 0.094),
    (0.298, 0.819, 0.215),
    (0, 0.658, 1)
)

top_bottom_colors = (0.862, 0.866, 0.882)

# Background Color RGBA
background_color = (0.184, 0.211, 0.250, 1)

# Figure Vars

vertices = 3
radius = 2
prism_height = 3
piramid_modifier = 1

def figure():

    polygon_points = []
    faces_angle = (2*pi)/vertices
    
    GL.glPushMatrix()
    
    GL.glTranslatef(0.0, 1.5, -10)
    GL.glRotatef(90,1.0,0.0,0.0)

    # Translation and Zoom
    GL.glTranslatef(delta_x, delta_y, delta_z)

    # Rotation
    # X axis
    GL.glRotatef(alpha, 0.0, 0.0, 1.0)
    # Y axis
    GL.glRotatef(beta, 0.0, 1.0, 0.0)

    # Figure

    # Bottom
    GL.glColor3fv(top_bottom_colors)
    GL.glBegin(GL.GL_POLYGON)
    for i in range(vertices):
        x = radius * cos(i*faces_angle)
        y = radius * sin(i*faces_angle)
        polygon_points += [ (x,y) ]
        GL.glVertex3f(x,y,0.0)
    GL.glEnd()

    # Top
    GL.glBegin(GL.GL_POLYGON)
    for x,y in polygon_points:
        GL.glVertex3f(piramid_modifier*x,piramid_modifier*y, prism_height)
    GL.glEnd()

    # Sides
    GL.glBegin(GL.GL_QUADS)
    for i in range(vertices):
        GL.glColor3fv(sides_colors[i%3])
        
        GL.glVertex3f(polygon_points[i][0],polygon_points[i][1],0)
        GL.glVertex3f(piramid_modifier*polygon_points[i][0],piramid_modifier*polygon_points[i][1],prism_height)

        GL.glVertex3f(piramid_modifier*polygon_points[(i+1)%vertices][0],piramid_modifier*polygon_points[(i+1)%vertices][1],prism_height)
        GL.glVertex3f(polygon_points[(i+1)%vertices][0],polygon_points[(i+1)%vertices][1],0)
    GL.glEnd()

    GL.glPopMatrix()


def draw():
    global alpha, left_button, right_button

    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

    figure()

    # Auto-Rotation
    alpha = alpha + delta_alpha

    GLUT.glutSwapBuffers()


def timer(i):
    GLUT.glutPostRedisplay()
    GLUT.glutTimerFunc(10, timer, 1)


def special_key_pressed(key, x, y):
    global vertices, piramid_modifier

    if (key == GLUT.GLUT_KEY_UP and vertices < 12):
        vertices += 1

    elif (key == GLUT.GLUT_KEY_DOWN and vertices > 3):
        vertices -= 1
    

    GLUT.glutPostRedisplay()


def key_pressed(key, x, y):
    global delta_alpha, piramid_modifier

    if key == b"\033":
        GLUT.glutLeaveMainLoop()

    # Toggles Piramid
    elif key == b"p":
        if piramid_modifier == 1:
            piramid_modifier = 0.5
        else:
            piramid_modifier = 1

    # Toggles Rotation
    elif key == b" ":
        if delta_alpha == 0:
            delta_alpha = 0.5
        else:
            delta_alpha = 0

    GLUT.glutPostRedisplay()


def mouse_click(button, state, x, y):
    global down_x, down_y, left_button, right_button, delta_y, piramid_modifier

    down_x, down_y = x, y

    left_button = button == GLUT.GLUT_LEFT_BUTTON and state == GLUT.GLUT_DOWN
    right_button = button == GLUT.GLUT_RIGHT_BUTTON and state == GLUT.GLUT_DOWN

    # Zoom
    if button == 3 and state == GLUT.GLUT_DOWN:
        delta_y += 1
    elif button == 4 and state == GLUT.GLUT_DOWN:
        delta_y -= 1

    # Toggles Piramid
    elif button == GLUT.GLUT_MIDDLE_BUTTON and state == GLUT.GLUT_DOWN:
        if piramid_modifier == 1:
            piramid_modifier = 0.5
        else:
            piramid_modifier = 1

    GLUT.glutPostRedisplay()


def mouse_move(x, y):
    global alpha, beta, down_x, down_y, delta_x, delta_y, delta_alpha

    # Rotate
    if left_button:
        delta_alpha = 0
        # Alpha calculations and bounds
        alpha -= ((x - down_x) / 4.0) * -1

        if alpha >= 360:
            alpha -= 360

        if alpha <= 0:
            alpha += 360

        # Beta calculations and bounds
        if alpha >= 180:
            beta += (y - down_y) / 4.0 * -1
        else:
            beta -= (y - down_y) / 4.0 * -1

        if beta >= 360:
            beta -= 360

        if beta <= 0:
            beta += 360

    # Translate
    if right_button:
        delta_x += -1 * (x - down_x) / 100.0
        delta_y += (y - down_y) / 100.0

    down_x, down_y = x, y

    GLUT.glutPostRedisplay()


def main():    
    GLUT.glutInit(argv)
    GLUT.glutInitDisplayMode(
        GLUT.GLUT_DOUBLE | GLUT.GLUT_RGBA | GLUT.GLUT_DEPTH | GLUT.GLUT_MULTISAMPLE
    )

    # Creating a screen with good resolution proportions
    screen_width = GLUT.glutGet(GLUT.GLUT_SCREEN_WIDTH)
    screen_height = GLUT.glutGet(GLUT.GLUT_SCREEN_HEIGHT)

    window_width = round(2 * screen_width / 3)
    window_height = round(2 * screen_height / 3)

    GLUT.glutInitWindowSize(window_width, window_height)
    GLUT.glutInitWindowPosition(
        round((screen_width - window_width) / 2), round((screen_height - window_height) / 2)
    )
    GLUT.glutCreateWindow(window_name)

    # Drawing Function
    GLUT.glutDisplayFunc(draw)

    # Input Functions
    GLUT.glutSpecialFunc(special_key_pressed)
    GLUT.glutKeyboardFunc(key_pressed)
    GLUT.glutMouseFunc(mouse_click)
    GLUT.glutMotionFunc(mouse_move)

    GL.glEnable(GL.GL_MULTISAMPLE)
    GL.glEnable(GL.GL_DEPTH_TEST)

    GL.glClearColor(*background_color)

    # Pre-render camera positioning
    GLU.gluPerspective(-45, window_width / window_height, 0.1, 100.0)


    GLUT.glutTimerFunc(10, timer, 1)
    GLUT.glutMainLoop()


if(__name__ == '__main__'):
    main()