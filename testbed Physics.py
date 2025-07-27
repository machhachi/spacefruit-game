# Spacefruit Physics Simulation Testbed
from cmu_graphics import *
import math

# Rendering Pipeline Mathematical Support
def setRenderOrigin(app, posX = 0.5, posY = 0.5):
    app.renderOrigin = (app.width * posX, app.height * posY)

def renderTranslate(x, y, cx, cy):
    return x - cx, y - cy

def renderRotate(x, y, theta):
    # We can now assume the center is 0
    radius = distance(x, y, 0, 0)
    return radius * math.cos(math.radians(theta)), radius * math.sin(math.radians(theta))

def distance(x1, y1, x2, y2):
    return( (y2 - y1) ** 2 + (x2 - x1) ** 2 ) ** 0.5
 
def renderCoords(app, posTuple): # The master renderer
    xReal, yReal = posTuple[0], posTuple[1]
    thetaReal = posTuple[2]
    
    xCam, yCam = app.playerPos[0], app.playerPos[1]
    thetaCam = app.playerPos[2]
    
    # Shift the coordinates in realspace to put the camera at origin
    tx, ty = renderTranslate(xReal, yReal, xCam, yCam)
    rx, ry = renderRotate(tx, ty, thetaCam)
    finalx, finaly = tx, ty
    
    # Shift to render scheme
    xRender, yRender = app.renderOrigin[0] + finalx, app.renderOrigin[1] - finaly
    return xRender, yRender

# Physics Stepping

def stepPhysics(app):
    # Affirm all forces in question are still relevant

    # Crunch net force
    netX, netY = 0, 0

    # Append forces (not many in this situation)
    netX += app.playerThrustForce[0]
    netY += app.playerThrustForce[1]
    
    ddx = netX / app.playerMass
    ddy = netY / app.playerMass
    
    print("Forces", ddx, ddy)

    # Crunch angle movement (not too sophisticated)
    ddTheta = app.playerThrustForce[2]

    stepPlayerMovement(app, ddx, ddy, ddTheta)


def stepPlayerMovement(app, ddx, ddy, ddtheta):
    app.playerPos[0] += ddx
    app.playerPos[1] += ddy
    app.playerPos[2] += ddtheta
    print("Position", app.playerPos[0], app.playerPos[1], app.playerPos[2])
    #app.playerVel += ddx, ddy, ddtheta
    #app.playerPos += app.playerVel

# Player Interaction

# Event Handling
def onStep(app):
    stepPhysics(app)
    setRenderOrigin(app) # I want it to center on any screen size, for now

def onKeyPress(app, key):
    pass

def onKeyHold(app, key):
    kx, ky, kT = 0, 0, 0
    for thisKey in key:
        kx += int(thisKey == 'd') * 15
        kx -= int(thisKey == 'a') * 15
        ky += int(thisKey == 'w') * 15
        ky -= int(thisKey == 's') * 15
        kT += int(thisKey == 'e') * 2
        kT -= int(thisKey == 'q') * 2
    app.playerThrustForce = [kx, ky, kT]

def onKeyRelease(app, key):
    app.isKeyPressed = False
    app.playerThrustForce = [0, 0, 0]

# Core Functionality
def onAppStart(app):
    setRenderOrigin(app, 0.5, 0.5)

    app.isKeyPressed = False

    app.playerPos = [0, 0, 0]
    app.playerVel = [0, 0, 0]
    app.playerMass = 1

    app.playerThrustForce = [0, 0, 0]

    app.objectOnePos = [30, 0, 0]

def redrawAll(app):
    drawCircle(*renderCoords(app, app.playerPos), 10, fill = 'blue')
    drawCircle(*renderCoords(app, app.objectOnePos), 20, fill = 'green')
    drawCircle(*app.renderOrigin, 3, fill = 'black')
    
def main():
    scale = 600
    runApp(width = 600, height = 600)

main()