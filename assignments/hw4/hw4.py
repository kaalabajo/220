"""
Name: Ka'ala Bajo
hw4.py

Problem: This program uses the graphics library to create shapes
based off user clicks and estimates pi.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math

from graphics import Point,Circle,Rectangle,Text,GraphWin

def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move square
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to make a square")
    instructions.draw(win)

    # builds a square
    shape = Rectangle(Point(50, 50), Point(100, 100))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        click = win.getMouse()
        #center = shape.getCenter()  # center of circle

        # move amount is distance from center of circle to the
        # point where the user clicked
        #change_x = click.getX() - center.getX()
        #change_y = click.getY() - center.getY()
        click_up = Point(click.getX() + 25, click.getY() + 25)
        click_down = Point(click.getX() - 25, click.getY() - 25)
        shape_new = Rectangle(click_up, click_down)
        shape_new.setFill("red")
        shape_new.draw(win)

    click_close = Text(Point(200,200), "click to close")
    click_close.draw(win)
    win.getMouse()
    win.close()

def rectangle():
    win = GraphWin("Draw a Rectangle", 400, 400)
    corner_1 = win.getMouse()
    corner_2 = win.getMouse()
    my_rec = Rectangle(corner_1, corner_2)
    my_rec.setFill('pink2')
    my_rec.draw(win)

    change_x = corner_1.getX() - corner_2.getX()
    absolute_x = ((change_x**2)**.5) #this is the length of side 1/3
    change_y = corner_1.getY() - corner_2.getY()
    absolute_y = ((change_y**2)**.5) #length of side 2/4

    perimeter = (absolute_x * 2) + (absolute_y * 2)
    perimeter_text = "Perimeter: " + str(perimeter)
    per_text = Text(Point(200, 350), perimeter_text)
    per_text.draw(win)

    area = absolute_x * absolute_y
    area_text = "Area:" + str(area)
    show_area_text = Text(Point(200, 375), area_text)
    show_area_text.draw(win)

    close_text = Text(Point(200,200), 'click anywhere to close!')
    close_text.draw(win)
    win.getMouse()


def circle():
    win = GraphWin("Draw a Circle", 400, 400)
    center = win.getMouse()
    circum = win.getMouse()

    radius = ((center.getX() - circum.getX())**2 + (center.getY() - circum.getY())**2 ) **.5

    my_circle = Circle(center,radius)
    my_circle.setFill("orange4")
    my_circle.draw(win)

    radius_set_text = "radius: " + str(radius)
    radius_text = Text(Point(200,375), radius_set_text)
    radius_text.draw(win)

    close_text = Text(Point(200,200), 'click anywhere to close!')
    close_text.draw(win)

    win.getMouse()

def pi2():
    number = eval(input("Enter number of terms to sum: "))
    denom = 1 #lil denom acc
    overall = 0
    for i in range(0,number):
        pos_neg = (2 * (i%2) - 1) #i mod 2 to flip back n forth
        overall = overall + (pos_neg * 4/denom)
        denom = denom + 2
    ans = overall * -1
    print("Pi approximation: ", ans)

    accuracy = math.pi - ans
    print("accuracy: ", accuracy)

if __name__ == '__main__':
    pass
