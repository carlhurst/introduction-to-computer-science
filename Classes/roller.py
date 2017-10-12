# Roller.py
# Graphics programme to roll a pair of dice. uses custom widgets
# Button and DieView

import random
from graphics import GraphWin, Point
from ButtonClass import Button
from DieView import DieView


def main():
    # create the application window
    win = GraphWin("Dice Window", 600, 600)
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")

    # Draw the interface widgets
    die1 = DieView(win, Point(3, 7), 2)
    die2 = DieView(win, Point(5, 7), 2)

    rollButton = Button(win, Point(5, 5), 1.5, 1, "Roll Dice")
    quitButton = Button(win, Point(3, 5), 1.5, 1, "Roll Dice")
    rollButton.activation()


    # Event Loop

    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            value1 = random.randrange(1, 7)
            die1.setValue(value1)
            value2 = random.randrange(1, 7)
            die2.setValue(value2)
            quitButton.activation()
        pt = win.getMouse()

    # close up shop
    win.close()

if __name__ == '__main__':
    main()
