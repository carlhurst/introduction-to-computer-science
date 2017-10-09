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
        self.xmax, self,xmin = x + w, x - w
