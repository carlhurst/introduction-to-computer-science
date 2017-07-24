import time
from graphics import *
import random
import time

# This programme is designed to create a number of squares based on user clicks
# Author Carl Hurst


# Create a window

win = GraphWin("",300,300)


def draw_Square(x,y):
    s1 = Rectangle(Point(x,y),Point(x+30,y+30))
    s1.setFill("Red")
    s1.draw(win)


# for clicks in range(10000):
#     click1 = win.getMouse()
#     x = click1.getX()
#     y = click1.getY()
#     draw_Square(x,y)
#     click1.draw(win)

start = time.time()

for i in range(10000):
    draw_Square(random.randint(10,270),random.randint(10,270))



print(start - time.time())

msg = Text(Point(150,150),"Click anywhere to quit programme")

msg.draw(win)

win.getMouse()



