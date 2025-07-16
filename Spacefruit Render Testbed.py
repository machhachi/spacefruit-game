from cmu_graphics import *
import math

# From (filename) import * 'runs the entire thing' as though it replaced that one line
# from (filename) import Name, name eing hte name of a class or function
# Should be able to drop these in another file and have "app" aliasing be okay

# Rendering Pipeline Mathematical Support
def setRenderOrigin(app, posX = 0.5, posY = 0.5):
    app.renderOrigin = (app.width * posX, app.height * posY)

def renderTranslate(x, y, cx, cy):
    return x - cx, y - cy

def renderRotate(x, y, theta):
    theta = math.radians(theta)
    rotatedX = math.cos(theta) * x - math.sin(theta) * y
    rotatedY = math.sin(theta) * x + math.cos(theta) * y
    return rotatedX, rotatedY

def distance(x1, y1, x2, y2):
    return( (y2 - y1) ** 2 + (x2 - x1) ** 2 ) ** 0.5
 
def renderMaster(app, posTuple): # The master renderer
    xReal, yReal = posTuple[0], posTuple[1]
    thetaReal = posTuple[2]
    
    xCam, yCam = app.playerPos[0], app.playerPos[1]
    thetaCam = app.playerPos[2]
    
    # Shift the coordinates in realspace to put the camera at origin
    tx, ty = renderTranslate(xReal, yReal, xCam, yCam)
    print("Translated, ",tx, ty, "about to rotate with", thetaCam)
    rx, ry = renderRotate(tx, ty, thetaCam)
    print("Now rotated to:", rx, ry)
    finalx, finaly = rx, ry
    
    # Shift to render scheme
    xRender, yRender = app.renderOrigin[0] + finalx, app.renderOrigin[1] - finaly
    return xRender, yRender





def onStep(app):
    for i in range(3):
        app.playerPos[i] += app.playerThrust[i]

def onKeyHold(app, key):
    kx, ky, kT = 0, 0, 0
    velocity = 15
    twist = 2
    for thisKey in key:
        kx += int(thisKey == 'd') * velocity
        kx -= int(thisKey == 'a') * velocity
        ky += int(thisKey == 'w') * velocity
        ky -= int(thisKey == 's') * velocity
        kT += int(thisKey == 'e') * twist
        kT -= int(thisKey == 'q') * twist
    app.playerThrust = [kx, ky, kT]

def onKeyRelease(app, key):
    app.playerThrust = [0, 0, 0]


def onAppStart(app):
    app.stepsPerSecond = 5
    setRenderOrigin(app, 0.5, 0.5)

    app.isKeyPressed = False

    app.playerPos = [0, 0, 0]
    app.playerThrust = [0, 0, 0]

    app.objectOnePos = [40, 0, 0]

def redrawAll(app):
    drawCircle(*renderMaster(app, app.playerPos), 10, fill = 'blue')
    drawCircle(*renderMaster(app, app.objectOnePos), 20, fill = 'green')
    drawCircle(*app.renderOrigin, 3, fill = 'black')
    
def main():
    scale = 600
    runApp(width = scale, height = scale)

main()