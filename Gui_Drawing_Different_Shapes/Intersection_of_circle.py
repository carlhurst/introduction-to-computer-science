"""
This programme is designed to find the intersection of a horizontal line with a circle
Author: Carl Hurst

Formula:

intersention = srt (dx2 - dy2)

"""

from graphics import  *
import math

# Draw Window
win = GraphWin("Intersection",500,500)


# Set The Co-Ordinates System

win.setCoords(-10.0,-10.0,10.0,10.0)

# Draw Circle
Radius = 2

circ = Circle(Point(0.0, 0.0), Radius)
circ.setOutline("orange")
circ.setFill("black")
circ.draw(win)

# Draw a Horizontal Line

Lin = Line(Point(-10.0, 0.0), Point(10.0, 0.0))
Lin.setFill("red")
Lin.draw(win)

x = math.sqrt((Radius * Radius) - (0*0))


print(x)


# Pause
win.getMouse()