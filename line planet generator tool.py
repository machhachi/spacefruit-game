# Spacefruit bonus tool: line planet generator machine
# Alex Werth
# 7 / 29 / 25

from cmu_graphics import *

def onAppStart(app):
    app.scale = 1
    #app.points = [
    #    (100, 100),
    #    (-100, 100),
    #    (-200, -200),
    #    (200, -100)
    #]
    app.pointsSomberHeart = [
        (300, 300), # top inner lip
        (400, 500), (0, 600), (-350, 500), # very top
        (-500, 300), (-600, 0), (-500, -300), # back plate
        (-350, -500), (100, -650), (500, -500), # very bottom
        (400, -300), # bottom inner lip
        (0, -400), (-300, -250), (-400, 0), (-300, 250), (0, 400) # interior
    ]

    app.points = [
        (100, 100),
        (-200, 300),
        (-200, -300)
    ]

def onKeyPress(app, key):
    if key == 'up':
        app.scale += 0.1
    if key == 'down':
        app.scale -= 0.1


# DRAW

def turnToScreenSpace(app, point):
    return( point[0] * app.scale + app.width / 2, point[1] * -app.scale + app.height / 2)


def redrawAll(app):
    drawLabel(f'Up and down arrows to change scale, currently {app.scale}', app.width / 2, 40)

    drawCircle(app.width / 2, app.height / 2, 5, fill = 'black')

    for pointIndex in range(len(app.points)):
        thisPoint = app.points[pointIndex]
        prevPoint = app.points[pointIndex - 1]

        color = 'red' if pointIndex == 0 else 'blue'

        drawLine(*turnToScreenSpace(app, prevPoint), *turnToScreenSpace(app, thisPoint), lineWidth = 2 * app.scale, fill = 'orchid', arrowEnd = True)

        drawCircle(*turnToScreenSpace(app, thisPoint), 5 * app.scale, fill = color)

    debugMainSprite = CMUImage.open("assets/TRANSPARENCY TEST SHUTTLE-01.png")
    drawImage(debugMainSprite, app.width / 2, app.height / 2)

def main():
    runApp(width = 600, height = 600)

main()