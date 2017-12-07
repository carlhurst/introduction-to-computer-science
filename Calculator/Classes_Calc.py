from graphics import *


class calculator:
    def __init__(slef):

        # Create window
        win = GraphWin(600, 600, "Calculator")

        win.setCoords(0, 0, 6, 7)
        win.setBackground("Slategray")
        self.win = win
        self.createButtons()
        self.createDisplay()

    def __createButtons(self):
        # create list of buttons to loop throguh
        # start with same sized buttons
        # bSpecs give centre of coords and label of buttons

        bSpec = [(2, 1, '0'), (3, 1, '.'),
                 (1, 2, '1'), (2, 2, '2'), (3, 2, '3'), (4, 2, '+'), (5, 2, '-')
                 (1, 3, '4'), (2, 3, '5'), (3, 3, '6'), (4, 3, '*'), (5, 3, '/')
                 (1, 4, '7'), (2, 4, '8'), (3, 4, '9'), (4, 4, '<-'), (5, 4, 'C')]
        self.buttons = []

        for cx, cy, label in bSpec:
            self.buttons.append(Button(self.win, Point(cx, cy), .75, .75, label))

        for b in self.buttons:
            b.activate()

    def __createDisplay(self):

        bg = Rectangle(Point(.5, 5.5), Point(5.5, 6.5))
        bg.setFill('white')
        bg.draw(self.win)
        text = Text(Point(3, 6), "")
        text.setFace("currier")
        text.setStyle("Bold")
        text.setSize(16)
        self.display = text
