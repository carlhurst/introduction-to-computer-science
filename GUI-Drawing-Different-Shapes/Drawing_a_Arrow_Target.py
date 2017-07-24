from graphics import *

# Programme to draw a arrow target



# Draw a circle function
def draw_Target(x,y,Radius,Colour):

    circle = Circle(Point(x,y),Radius)
    circle.setFill(str(Colour))
    circle.setOutline("black")
    circle.draw(win)






# Create the window
win = GraphWin("Target", 300,300)

#Declare Radius as Variable
Radius = 20

colours = ["", "Black", "Blue", "Red" ,"Yellow"]

# Define list index
i = 0

# Loop Through number of Circles in target
for c in range(5,0,-1):

    draw_Target(150,150,(Radius*c),colours[i])

    # Add one to the colour index
    i += 1



# Pause
win.getMouse()