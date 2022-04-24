"""ACTUALLY CH12 i have no clue i stopped listening when he started talking"""
def aug():
    pass
from graphics import *
"""you can add lists together"""
#acc= []
#acc += [float(user_in)]
"""acc + [4,5,6] returns a NEW list but += changes original"""
#acc = [1,2,3]
#acc * 3
"""the above returns one list containing 1,2,3 three times not 3 lists"""
#acc = [1,2,3]
#acc[2:] this returns [3]
"""
.append
.sort
.reverse
.index(x)
.insert(i,x)
.count
.remove(x)
.pop(i)
"""
a = [1,2,3]
print(a.index(3))
print(a.count(3))
print()
"""more about sort:
you can sort any type of object but you must tell it how"""

from graphics import *

def print_circle(circles):
    for circle in circles:
        print('({},{}) {} |'.format(circle.getCenter().getX(), circle.getCenter().getY(), circle.getRadius()          ))

c1 = Circle(Point(12,70),45)
c2 = Circle(Point(1,7),4)
c3 = Circle(Point(120,700),32)
circles = [c1,c2,c3]
print_circle(circles)
print()
#def x(circle):
#   return circle.getCenter().getX()

def x_sort(circle):
    return circle.getCenter().getX()

circles.sort(key=x_sort)
print(circles)

"""
tuple
like a list. behaves almost identical to list
once tuple is set cant be changed. immutable
tuple is own data type and use () instead
tend to be faster and use less memory
"""

"""
dictionary
uses {}
each element in a dictionary has a KEY and VALUE
key is like index value. but key can be anything
"""

def circle_ting():
    my_data = [(2,3,9),(20,30,29),(12,230,90)]
    circle_list = []
    for data in my_data:
        circle_list.append(
            Circle(Point(data[0],data[1]),data[2]))
    print_circle(circle_list)
    circle_list.sort(key=x_sort)
    print_circle(circle_list)

def dict_prac():
    d = {'henry':7, 'ole':3, 'rydawg':9}

    names = d.keys() #returns a sequence keys
    cool_points = d.values()
    #key in dict

    #for name in names:
    #    print(name)
    print(list(cool_points)[0])
    for cool_points in d.values():
        print(cool_points)

    k_v = d.items()
    for item in k_v:
        print(item) #items returns seq of TUPLES rep key val pair

    for key,value in d.items():
        print(key,value)

    for kv in d.items(): #each indiv item is a tuple. returns data type tuple
        print(kv[0],kv[1])

    d['dappa'] = d.get('dappa',1)

    a = d.get('mice',9)
    print(a)
    print()

    del(d['dappa'])
    d['mouses'] = 9
    print(d)
dict_prac()