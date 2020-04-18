import numpy as np
import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut

# global parameters
# window specified parameters
wndWidth = 300                      # window width
wndHeight = 300                     # window height
wndInitPos = (100, 100)             # window init position relative left top corner
wndTitle = b"3D graphics app"
# colors
colAmbient = (1.0, 1.0, 1.0, 1.0)
colGreen = (0.2, 0.8, 0.2, 1.0)
colRed = (0.8, 0.2, 0.2, 1.0)
colBlue = (0.8, 0.2, 0.8, 1.0)
colClear = (0.0, 0.9, 0.9, 1.0)     # default color of the window
# geometry
rotX = 0                            # rotation around x axis in degrees
rotY = 0                            # rotation around y axis in degrees
drawRect = (-6.0, 6.0, -6.0, 6.0)   # a rectangle will be drawn
posLight = (5.0, 5.0, -1.0)

# initializing scene parameters
def Init() :
    global colClear, colAmbient, rotX, rotY, drawRect
    # initalizing drawing color
    gl.glClearColor(colClear[0], colClear[1], colClear[2], colClear[3])
    # specifying drawing depth buffer
    gl.glClearDepth(1.0)
    gl.glEnable(gl.GL_DEPTH_TEST)
    gl.glDepthFunc(gl.GL_LEQUAL)
    #glu.gluOrtho2D(drawRect[0], drawRect[1], drawRect[2], drawRect[3])
    # specifying lighting
    gl.glEnable(gl.GL_LIGHTING)
    gl.glEnable(gl.GL_LIGHT0)
    gl.glLightModelfv(gl.GL_LIGHT_MODEL_AMBIENT, colAmbient)
    gl.glLightfv(gl.GL_LIGHT0, gl.GL_POSITION, posLight)

# processing the window resizing
def WndResize(width, height) :
    global wndWidth, wndHeight
    wndWidth = width
    wndHeight = height
    gl.glViewport(0, 0, width, height)
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    glu.gluPerspective(60.0, float(width) / float(height), 0.01, 60.0)
    gl.glMatrixMode(gl.GL_MODELVIEW)
    gl.glLoadIdentity()
    glu.gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)

# special commands processing
def WndInput(key, x, y) :
    global rotX, rotY
    # processing rotation according input key
    if key == glut.GLUT_KEY_UP : rotX -= 2.0
    if key == glut.GLUT_KEY_DOWN : rotX += 2.0
    if key == glut.GLUT_KEY_LEFT : rotY -= 2.0
    if key == glut.GLUT_KEY_RIGHT : rotY += 2.0
    # normalizing rotations
    if rotX > 360 : rotX -= 360
    elif rotX < 360 : rotX += 360
    if rotY > 360 : rotY -= 360
    elif rotY < 360 : rotY += 360
    # redrawing processing
    glut.glutPostRedisplay()    

# creating specifyed cylinder
def DrawCylinder(position, radius, height, color, polyn = (30, 30)) :
    # specifying material for cylinder
    gl.glMaterialfv(gl.GL_FRONT_AND_BACK, gl.GL_DIFFUSE, color)
    gl.glTranslatef(position[0], position[1], position[2])
    # creating cylinder with specifyed raduis and height
    glut.glutSolidCylinder(radius, height, polyn[0], polyn[1])

# creating specifyed cone
def DrawCone(position, radius, height, color, polyn = (30, 30)) :
    # specifying material for cone
    gl.glMaterialfv(gl.GL_FRONT_AND_BACK, gl.GL_DIFFUSE, color)
    gl.glTranslatef(position[0], position[1], position[2])
    # creating cone with specifyed raduis and height
    glut.glutSolidCone(radius, height, polyn[0], polyn[1])

# creating specifyed sphere
def DrawSphere(position, radius, color, polyn = (50, 50)) :
    # specifying material for sphere
    gl.glMaterialfv(gl.GL_FRONT_AND_BACK, gl.GL_DIFFUSE, color)
    gl.glTranslatef(position[0], position[1], position[2])
    # creating sphere with specifyed raduis and height
    glut.glutSolidSphere(radius, polyn[0], polyn[1])
    
# draw function
def WndDraw() :
    global rotX, rotY, posLight, colGreen, colBlue, colRed
    # drawing the scene
    # cleaning color buffer and depth buffer
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    # specifying objects
    gl.glPushMatrix()
    gl.glRotatef(rotX, 1.0, 0.0, 0.0)   # rotation around x
    gl.glRotatef(rotY, 0.0, 1.0, 0.0)   # rotation around y
    #gl.glLightfv(gl.GL_LIGHT0, gl.GL_POSITION, posLight)
    DrawCylinder((-1, 0, -1), 0.3, 2, colGreen)
    DrawSphere((1, 0, 1), 0.5, colRed)
    DrawCone((1, 0, -1), 0.5, 2, colBlue)
    gl.glPopMatrix()
    # rendering
    glut.glutSwapBuffers()

# OpenGL initialization
glut.glutInit(glut.sys.argv)
# initialize an image visualization type
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGBA)
# initial window size
glut.glutInitWindowSize(wndWidth, wndHeight)
# initial window position
glut.glutInitWindowPosition(wndInitPos[0], wndInitPos[1])
# creating a window
window = glut.glutCreateWindow(wndTitle)
glut.glutDisplayFunc(WndDraw)
glut.glutSpecialFunc(WndInput)
glut.glutReshapeFunc(WndResize)
Init()
#glut.glutIdleFunc(WndDraw)
glut.glutMainLoop()

