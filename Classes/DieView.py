from graphics import *
class DieView:
    """DieView is a widget that displays a graphical representation of a standard six-sided die."""

def __init__(self, win, center, size):
    # first define some standard values
    self.win = win  # save this for drawing pips later
    self.background = "white" # color of die face
    self.forground = "black" # color of the pips
    self.psize = 0.1 * size #radius of each pips
    hsize = size / 2.0 # half the size of the die
    offset = 0.6 * hsize # distance from center to outer pips

    # create a square for the face
    cx, cy = center.geyX(), center.getY()
    p1 = Point(cx-hsize, cy-hsize)
    p2 = Point(cx+hsize, cy+hsize)
    rect = Rectangle(p1, p2)
    rect.draw(win)
    rect.setFill(self.background)

    # Draw a initail value
    self.setValue(1)

    def __MakePip(self, x, y):
        "Internal Helper MEthod to draw a pip at (x, y)"
        pip = Circle(Point(x, y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

    def setValue(self, value):
        "Set the die to display value."
        # Turn all pips off
        self.pip1.setFill(self.background)
        self.pip2.setFill(self.background)
        self.pip3.setFill(self.background)
        self.pip4.setFill(self.background)
        self.pip5.setFill(self.background)
        self.pip6.setFill(self.background)
        self.pip7.setFill(self.background)

    # Turn correct pips on
        if value == 1:
            self.pip4.setFill(self.forground)
        elif value == 2:
            self.pip1.setFill(self.forground)
            self.pip7.setFill(self.forground)
        elif value == 3:
            self.pip1.setFill(self.forground)
            self.pip7.setFill(self.forground)
            self.pip4.setFill(self.forground)
        elif value == 4:
            self.pip1.setFill(self.forground)
            self.pip3.setFill(self.forground)
            self.pip5.setFill(self.forground)
            self.pip7.setFill(self.forground)
        elif value == 5:
            self.pip1.setFill(self.forground)
            self.pip3.setFill(self.forground)
            self.pip4.setFill(self.forground)
            self.pip5.setFill(self.forground)
            self.pip7.setFill(self.forground)
        else:
            self.pip1.setFill(self.forground)
            self.pip2.setFill(self.forground)
            self.pip3.setFill(self.forground)
            self.pip4.setFill(self.forground)
            self.pip5.setFill(self.forground)
            self.pip6.setFill(self.forground)
            self.pip7.setFill(self.forground)
