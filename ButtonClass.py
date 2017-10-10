from graphics import *

class Button:
    """
    A button is a labeled rectangle in a window it is activated or deactivated with the activate() and deactivate()methods.
    The clicked(p) method returns true is the button is active and p is inside it.
    """
    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button , eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit'"""

        w, h = width/2.0, height/ 2.0
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x + w, x - w
        self.ymax, self.ymin = y + h, y - h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.xmax)
        self.rect = Rectangle(p1, p2)

        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self):
        "Returns True if button is active and p is inside"
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def active(self):
        "Sets this button to active"
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets the button to inactive"
        self.label.setFill('darkgray')
        self.rect.setWidth(1)
        self.active = False