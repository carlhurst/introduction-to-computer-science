# This programme build a small house with the use of the graphics library

from graphics import  *

# todo build window for the house to be built within

win = GraphWin("house", 500,500)

# todo build co-ordinate system
win.setCoords(0.0,0.0,100.0,100.0)

# todo build outline of the house and details
sqre = Rectangle(Point(20.0,20.0),Point(70.0,70.0))
sqre.draw(win)

window = Rectangle(Point(25,25),Point(35,35))
window.draw(win)





win.getMouse()