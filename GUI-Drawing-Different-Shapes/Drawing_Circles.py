
from graphics import *


def main():
# Draw Window

    win = GraphWin("Shape Generation", 300, 300)

    # Draw Circle
    circ = Circle(Point(50,50),20)
    circ.setFill('red')
    circ.setOutline('blue')
    circ.draw(win)

    for i in range(10):
        p = win.getMouse()
        c = circ.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()

        circ.move(dx,dy)

    text = Text(Point(150,150),"Press mouse to quit")
    text.draw(win)

    win.getMouse()
    win.close()
main()



