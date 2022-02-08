"""Name: Ka'ala Bajo
lab4.py

Problem: Draw's a valentine's day card! And Jeff the frog!

Certification of Authenticity:
I certify that this assignment is entirely my own work."""

import time

from graphics import *

def greeting_card():
    win = GraphWin("Valentine's Card", 500, 400)
    win.setBackground("pink3")
    #here are all points for left side
    mid = Point(250, 150)
    p2 = Point(210, 130)
    p3 = Point(170, 135)
    p4 = Point(140, 150)
    p5 = Point(130, 180)
    p6 = Point (150, 210)
    p7 = Point (180, 230)
    p8 = Point (250, 275)
    left_side = Polygon(mid, p2, p3, p4, p5, p6, p7, p8)
    left_side.setFill("pink")
    left_side.setOutline("pink")
    left_side.draw(win)

    #now lets copy these points to the right
    #did it manually bc i can't do math lol
    p2r = Point(300, 130)
    p3r = Point(340, 135)
    p4r = Point(370, 150)
    p5r = Point(380, 180)
    p6r = Point(360, 210)
    p7r = Point(330, 230)
    right_side = Polygon(mid, p2r, p3r, p4r, p5r, p6r,p7r, p8)
    right_side.setFill("pink")
    right_side.setOutline("pink")
    right_side.draw(win)

    #add text
    label = Text(Point(250, 30), "happy valentines bro")
    label.setSize(20)
    label.setFace("times roman")
    love_jeff = Text(Point(250, 60), "love, jeff")
    love_jeff.draw(win)
    label.draw(win)

    #create an arrow
    line_start = Point(70, 290)
    line_end = Point(160, 260)
    arrow_line = Line(line_start, line_end)

    head_p1 = Point(130, 260)
    head_p2 = Point(145, 275)
    arrow_head = Polygon(head_p1, line_end, head_p2)
    arrow_head.setFill('black')

    arrow_line.draw(win)
    arrow_head.draw(win)

    for i in range(0, 55):
        arrow_line.move(10, -5)
        arrow_head.move(10, -5)
        time.sleep(.03)

    end_message = Text(Point(250, 375), "click to close")
    end_message.draw(win)


    #here's a frog, his name is jeff

    centerpoint = Point(250, 200)
    face = Circle(centerpoint, 100)
    face.setFill('green')
    face.draw(win)

    left_eye = Circle(Point(200, 140), 40)
    left_eye.setFill('black')
    left_eye.setOutline('green')

    right_eye = left_eye.clone()
    right_eye.move(100, 0)

    left_eye.draw(win)
    right_eye.draw(win)

    eye_white_l = Circle(Point(290, 120), 15)
    eye_white_l.setFill('white')
    eye_white_r = eye_white_l.clone()
    eye_white_r.move(-100, 0)

    eye_white_l.draw(win)
    eye_white_r.draw(win)

    mouth_left = Line(Point(250,280), Point(200, 240))
    mouth_right = Line(Point(250,280), Point(300, 240))
    mouth_left.draw(win)
    mouth_right.draw(win)

    thats_jeff = Text(Point(370, 280), "(he's jeff)")
    thats_jeff.draw(win)

    win.getMouse() #keep open
    win.close()

greeting_card()