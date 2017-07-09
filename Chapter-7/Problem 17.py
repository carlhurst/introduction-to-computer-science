"""
This programme is desgined to make a simple animation of a ball bouncing around the screen
Author: Carl Hurst
"""
from graphics import *
import time
import random as r

def main():
    print("This programme is designed to make a bouncing ball")



    # Make Window
    win = GraphWin("Bouncing Ball", 600, 600)

    # Make Circle
    circ = Circle(Point(300, 300),30)
    circ.setFill("Yellow")
    circ.draw(win)

    dx = -1
    dy = -1

    for i in range(100000):
        # Get center of circle
        center = circ.getCenter()
        circ.move(dx,dy)

        y = center.getY()
        x = center.getX()

        if x <= 135 or y <= 135:
            dx = r.randint(1, 15)
            dy = r.randint(1, 15)
            circ.setFill(color_rgb(r.randint(1,255),r.randint(1,255),r.randint(1,255)))

        if x >= 465 or y >= 465:
            dx = r.randint(-15, -1)
            dy = r.randint(-10, -1)
            circ.setFill(color_rgb(r.randint(1, 255), r.randint(1, 255), r.randint(1, 255)))



        print(x,y)
        time.sleep(.003)

    # programme hold
    win.getMouse()

main()