from graphics import *
import time
import random as rand


def line(x, y, x1, y1, window):

    lne = Line(Point(x, y), Point(x1, y1))
    lne.setFill(color_rgb(rand.randint(50,255),rand.randint(1,255),rand.randint(1,255)))
    lne.draw(window)


def main():
    # create window
    win = GraphWin("Straight Curved Lines", 1600, 900)
    win.setCoords(-1.0,-1.0,100,100)
    win.setBackground("black")
    #  Point 1
    x = 10.0
    y = 10.0
    # Point 2
    x1 = 90.0
    y1 = 10.0

    # Point 3
    x2 = 90.0
    y2 = 10.0

    # Point 4

    x3 = 90.0
    y3 = 90.0

    start = time.clock()


    while x1 >= 10:
        line(x, y, x1, y1,  win)
        line(x2, y2, x3 ,y3 , win)

        # time.sleep(.000000000002)

        x1 -= .20
        y += .20
        y2 += .20
        x3 -= .20

    stop = time.clock()

    print(stop - start)

        # if x1 < 10:
        #     break



    win.getMouse()


main()