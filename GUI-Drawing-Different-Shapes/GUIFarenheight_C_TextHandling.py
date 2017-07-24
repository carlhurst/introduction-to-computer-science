# ConvertGui.py
# GUI Programme to desing an programme that takes a input in farenhieght and converts it to C
# using a graphical interface

from graphics import *

def main():

    win = GraphWin("Temp Converter", 400, 300)
    win.setCoords(0.0,0.0,3.0,4.0)


    # Draw the interface

    Text(Point(1,3), "    Celsius Temperature:").draw(win)
    Text(Point(1,1), "Farenheit Tempreture:").draw(win)
    input = Entry(Point(2,3), 5)
    input.setText("0.0")
    input.draw(win)
    output = Text(Point(2,1), "")
    output.draw(win)
    button = Text(Point(1.5,2.0),"Convert It")
    button.draw(win)
    Rectangle(Point(1,1.5), Point(2,2.5)).draw(win)

    # Wait for mouse click
    win.getMouse()

    # Convert input
    celsius = eval(input.getText())
    fahrenheit = 9.0 / 5.0 * celsius + 32

    # Display output and change button
    output.setText(fahrenheit)
    button.setText("Quit")

    # Wait for click and then quit
    win.getMouse()
    win.close()

main()