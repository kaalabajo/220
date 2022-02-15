"""Name: Ka'ala Bajo
lab5.py

Problem:

Certification of Authenticity:
I certify that this assignment is entirely my own work."""
from graphics import *
import math

def triangle():
    win = GraphWin("Triangle", 400,400)
    win.setBackground("pink")

    start_msg = Text(Point(200, 350), "click anywhere 3 times to draw a triangle")
    start_msg.draw(win)

    click1 = win.getMouse()
    start_msg.undraw()
    click2 = win.getMouse()
    click3 = win.getMouse()

    my_triangle = Polygon(click1, click2, click3)
    my_triangle.draw(win)

    #math for perim
    dx1 = click1.getX() - click2.getX()
    dy1 = click1.getY() - click2.getY()
    length1 = math.sqrt(dx1**2 + dy1**2)

    dx2 = click2.getX() - click3.getX()
    dy2 = click2.getY() - click3.getY()
    length2 = math.sqrt(dx2**2 + dy2**2)

    dx3 = click3.getX() - click1.getX()
    dy3 = click3.getX() - click1.getY()
    length3 = math.sqrt(dx3**2 + dy3**2)

    perim = length3 + length2 + length1
    perim_msg = "Perimeter: " + str(perim)
    perim_text = Text(Point(200,350), perim_msg)
    perim_text.draw(win)

    #math for area
    s_var = perim/2
    tri_area = math.sqrt(s_var * (s_var-length1) * (s_var-length2) * (s_var-length3))
    area_msg = str("Area: " + str(tri_area))
    area_text = Text(Point(200,380), area_msg)
    area_text.draw(win)

    close_click = Text(Point(200,200), "click anywhere to close")
    close_click.draw(win)
    win.getMouse()
    win.close()

def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    #add a entry box



    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    #add a entry box


    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    #add a entry box


    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    red_amt = Entry(Point(win_width / 2 + 10, win_height / 2 + 40), 5)
    red_amt.draw(win)
    green_amt = Entry(Point(win_width / 2 + 10, win_height / 2 + 70), 5)
    green_amt.draw(win)
    blue_amt = Entry(Point(win_width / 2 + 10, win_height / 2 + 100), 5)
    blue_amt.draw(win)
    win.getMouse()
    for i in range(4):
        red = eval(red_amt.getText())
        blue = eval(blue_amt.getText())
        green = eval(green_amt.getText())

        shape.setFill(color_rgb(red,green,blue))
        win.getMouse()

    # Wait for another click to exit
    inst.undraw()
    msg = "click to close"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)
    win.getMouse()
    win.close()

def process_string():
    get_str = input("Hey there!\nEnter a string for me. Any string really!\nString: ")
    print("1. first character: " + get_str[0])
    print("2. last character: " + get_str[-1])
    print("3. 2 - 5 : " + get_str[1:5])
    print("4. first and last: " + get_str[0] + get_str[-1])
    print("5. the first three characters repeating, for some reason: ")
    print(get_str[0:3]*10)
    print("6. now line by line for some reason lol: ")
    for i in get_str:
        print(i)
    print("7. total number of characters in your string: " + str(len(get_str)))

def process_list():
    pt = Point(5,10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = (values[1]+ values[3])
    print(x)
    x = (values[0] + values[2])
    print(x)
    x = values[1]*5
    print(x)
    x = values[2:5]
    print(x)
    x = values[2:4]
    x.append(values[0])
    print(x)
    x = []
    x.append(values[2])
    x.append(values[0])
    x.append(float(values[5]))
    print(x)
    x = values[2] + values[0] + float(values[5])
    print(x)
    x = len(values)
    print(x)


def another_series():
    ask = eval(input("how many terms in the series do you want: "))
    acc = 0
    for i in range(ask):
        current = i%3
        current = (current + 1)*2
        acc = acc + current
        print(current, end = " ")
    print()
    print('sum = ', acc)

def target():
    win = GraphWin("Target", 400,400)
    win.setBackground("pink")

    circle1 = Circle(Point(200,200), 40*5)
    circle1.setFill('white')

    circle2 = Circle(Point(200,200), 40*4)
    circle2.setFill('black')

    circle3 = Circle(Point(200,200), 40*3)
    circle3.setFill('blue')

    circle4 = Circle(Point(200,200), 40*2)
    circle4.setFill('red')

    circle5 = Circle(Point(200,200), 40)
    circle5.setFill('yellow')

    circle1.draw(win)
    circle2.draw(win)
    circle3.draw(win)
    circle4.draw(win)
    circle5.draw(win)

    close_text = Text(Point(200,200), "click to close")
    close_text.draw(win)
    win.getMouse()
    win.close()

