"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
import math


def sum_of_threes():
    upper = eval(input("What's the upper bound? ")) #get num
    rounded_upper = upper//3 #round down
    current_sum = 0 #placeholder
    for i in range(rounded_upper + 1): #+1
        current_sum = current_sum + (i*3)
    print("Sum of threes is", current_sum)
#sum_of_threes()


def multiplication_table():
    for i in range(10): #do the following 10x
        for j in range(10):
            print((i + 1) * (j + 1), end="\t")
        print()


def triangle_area():
    a = eval(input("What is the length of side 1? "))
    b = eval(input("Next, what is the length of side 2? "))
    c = eval(input("Finally, what is the length of side 3? "))
    s = ((a + b + c)/2)
    area_not_squared = (s*(s-a)*(s-b)*(s-c))
    area = math.sqrt(area_not_squared)
    print("area is", area)
triangle_area()
def sum_squares():
    pass


def power():
    pass


if __name__ == '__main__':
    pass
