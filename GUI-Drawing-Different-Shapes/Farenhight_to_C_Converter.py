"""
This programme is designed to be a GUI for a farenheight to celcius converter and should
Both the programme and the GUI should accept user input from the user and look useful.

"""

from graphics import *

#create window
win = GraphWin("Unit Converter",300,300)

#set coordonate system
win.setCoords(0.0,0.0,10.0,10.0)
win.setBackground(color_rgb(102,153,255)) #set background

# Draw text to the screen
Text(Point(5.0,9.0),"Please Enter the Temprature in Farenheight").draw(win) # draw text to the screen

#Draw a input box
Farentheight = Entry(Point(5.0,8.0),30) # input box
Farentheight.setFill("pink") # set input box colour
Farentheight.draw(win) # draw box

Text(Point(5.0,6.0),"The Tempreture in C is:").draw(win) # set input text for celcius

Celcius = Entry(Point(5.0,5.0),30) # set entry point for celcius
Celcius.setFill("pink") # set colour
Celcius.draw(win) # draw box to screen

win.getMouse()

F = eval(Farentheight.getText())

C = (F -32) * 5/9

Celcius.setText(C)







win.getMouse() #pause


