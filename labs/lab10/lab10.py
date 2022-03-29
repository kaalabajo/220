"""
Name: Ka'ala Bajo
lab10.py

Problem: Uses a list of objects to run a door opening simulation.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


from button import Button
from door import Door
from graphics import *

def main():
    label = ""

    win = GraphWin("Test", 700,700)
    exit_butt = Button(Rectangle(Point(200,70),Point(500,200)),"Exit")
    exit_butt.draw(win)

    my_door = Door(Rectangle(Point(200,220),Point(500,675)),"Closed")
    my_door.color_door("red4")
    my_door.draw(win)

    while not exit_butt.is_clicked(win.getMouse()):
        clicked = win.getMouse()

        if my_door.is_clicked(clicked) and my_door.get_label() == "Closed":
            my_door.color_door("white")
            my_door.set_label("Open")
        elif my_door.is_clicked(clicked) and my_door.get_label() == "Open":
            my_door.color_door("red4")
            my_door.set_label("Closed")

    win.close()
if __name__ == '__main__':
    main()