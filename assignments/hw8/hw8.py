"""
Name: Ka'ala Bajo
hw8.py

Problem: Solves a bunch of problems using logic expressions.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math
from graphics import Circle, GraphWin, Text, Point

def add_ten(nums):
    for i in range(len(nums)):
        nums[i] += 10

def square_each(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2

def sum_list(nums):
    num_acc = 0
    for i in range(len(nums)):
        num_acc += nums[i]
    return num_acc

def to_numbers(nums):
    for i in range(len(nums)):
        nums[i] = eval(nums[i])


def sum_of_squares(nums):
    new_list = []
    for each_string in nums:
        each_string.split(",")
        mini_list = []
        each_string = [each_string]
        for mini_list in each_string:
            mini_list = mini_list.split(", ")

            to_numbers(mini_list)
            square_each(mini_list)
            summed = sum_list(mini_list)
            new_list.append(summed)
        #for i in range(len(each_string)):
        #    mini_list.append(each_string[i])

        #to_numbers(mini_list)
        #square_each(mini_list)
        #summed = sum_list(mini_list)
        #new_list.append(summed)

    return new_list

def starter(weight, wins):
    return (weight <= 150 and weight >= 160 and wins >= 5) or weight > 199 or wins > 20

def leap_year(year):
    if year == 0:
        return True
    return (year%4==0) and (year%400==0 or not year%100 == 0)

def did_overlap(circle_one, circle_two):
    circle_1c = circle_one.getCenter()
    circle_2c = circle_two.getCenter()
    circle_1r = circle_one.getRadius()
    circle_2r = circle_two.getRadius()
    distance_center = math.sqrt((circle_1c.getX() - circle_2c.getX()) ** 2 + (circle_1c.getY() - circle_2c.getY()) ** 2)
    # if dist from centers + radius = 0 theyre touching
    return distance_center - (circle_1r + circle_2r) <= 0

def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)
#sorry im lazy. but hey look the second is pink
    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY()  - circumference_point.getY()) ** 2)
    circle_two = Circle(center, radius)
    circle_two.setFill("pink")
    circle_two.draw(win)

    did_it = did_overlap(circle_one,circle_two)
    if did_it is True:
        msg = "The circles overlap.\n\nClick again to close"
    else:
        msg = "The circles do not overlap.\n\nClick again to close"
    inst = Text(Point(5,5),msg)
    inst.draw(win)
    win.getMouse()
    win.close()

if __name__ == '__main__':
    pass
