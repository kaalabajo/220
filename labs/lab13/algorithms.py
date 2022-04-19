"""
Name: Kaala Bajo
algorithms.py

Problem: Adds read data to a list and does a linear search

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
#ps, i did not talk to anyone but i did consult the book

from graphics import Rectangle, Point

def read_data(filename):
    in_f = open(filename, "r")
    all_text = in_f.read()
    all_text = all_text.replace("\n", " ")
    split_text = all_text.split(" ")
    i = 0
    num_list = []
    while i < len(split_text):
        num_list.append(eval(split_text[i]))
        i += 1
    in_f.close()
    return num_list

def is_in_linear(search_val, values):
    #return search_val in values
    i = 0
    while i < len(values):
        if search_val == values[i]:
            i += 1
            return True
        else:
            i += 1
    return False

def is_in_binary(search_val, values):
    l_ind = 0
    r_ind = len(values)-1
    values = values.sort()
    while l_ind <= r_ind:
        m_ind = (l_ind+r_ind)//2
        m_val = values[m_ind]

        if m_val == search_val:
            return True
        elif m_val < search_val:
            l_ind = m_ind + 1
        else:
            r_ind = m_ind - 1
    return False

def selection_sort(values):
    for lowest in range(len(values)-1):
        point = lowest
        for i in range(lowest + 1, len(values)):
            if values[i] < values[point]:
                point = i
    values[lowest], values[point] = values[point], values[lowest]

def calc_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    length = abs(p1.getX() - p2.getX())
    width = abs(p1.getY() - p2.getY())
    area = length * width
    return area

def rect_sort(rectangles):
    rectangles.sort(key=calc_area)



#calc_area(Rectangle(Point(3,2), Point(6,4)))
def main():
    R1 = Rectangle(Point(3, 2), Point(6, 4))
    R2 = Rectangle(Point(9000, 820000), Point(1000, 40000))
    R3 = Rectangle(Point(60, 120), Point(320, 30))

    rect_sort([R1, R2, R3])
