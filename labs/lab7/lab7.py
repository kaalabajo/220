"""
Name: Kaala Bajo
lab7.py

Problem: This program attempts to do a bumper car simulation.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math
from random import randint
from graphics import *

def get_random(move_amount):
    return randint(-1*move_amount,move_amount)

def did_collide(ball_1,ball_2):
    ball_1c = ball_1.getCenter()
    ball_2c = ball_2.getCenter()
    ball_1r = ball_1.getRadius()
    ball_2r = ball_2.getRadius()
    distance_center = math.sqrt((ball_1c.getX() - ball_2c.getX())**2 + (ball_1c.getY() - ball_2c.getY())**2)
    #if dist from centers + radius = 0 theyre touching
    return distance_center - (ball_1r + ball_2r) <= 0

def hit_vertical(ball, window):
    ball_center = ball.getCenter()
    if ball_center.getY() + ball.getRadius() <= 0:
        return True
    if ball_center.getY() + ball.getRadius() >= window.getWidth():
        return True
    else:
        return False

def hit_horizontal(ball, window):
    ball_center = ball.getCenter()
    if ball_center.getX() + ball.getRadius() <= 0:
        return True
    if ball_center.getX() + ball.getRadius() >= window.getWidth():
        return True
    else:
        return False

def get_random_color():
    return color_rgb(randint(0,255),randint(0,255),randint(0,255))

def bumper():
    # create win
    win = GraphWin("Bumper Sim", 400, 400)
    win.setBackground("pink")

    # create 2 balls with random color and position
    ball_1 = Circle(Point(randint(10,390), randint(10,390)), 10)
    ball_1.setFill(get_random_color())
    ball_2 = Circle(Point(randint(10,390), randint(10,390)), 10)
    ball_2.setFill(get_random_color())

    #draw them
    ball_1.draw(win)
    ball_2.draw(win)

    ball_1x = get_random(10)
    ball_1y = get_random(10)
    ball_2x = get_random(10)
    ball_2y = get_random(10)

    while not win.checkMouse():

        ball_1.move(ball_1x,ball_1y)
        ball_2.move(ball_2x,ball_2y)
        time.sleep(.02)

        if hit_vertical(ball_1, win) :
            ball_1y = (-1)*ball_1y
        if hit_horizontal(ball_1, win) :
            ball_1x = (-1)*ball_1x
        if hit_vertical(ball_2, win):
            ball_2y = -ball_2y
        if hit_horizontal(ball_2, win):
            ball_2x = -ball_2x
        if did_collide(ball_1, ball_2):
            ball_1y = (-1) * ball_1y
            ball_1x = (-1)*ball_1x
            ball_2y = -ball_2y
            ball_2x = -ball_2x

    win.close()