"""
Name: Kaala Bajo
hw2.py

Problem: This program uses arithmatic and the math import
to solve a series of mathematical problems.

Certification of Authenticity
I certify that this assignment is entirely my own work.
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
    side_a = eval(input("What is the length of side a? "))
    side_b = eval(input("Next, what is the length of side b? "))
    side_c = eval(input("Finally, what is the length of side c? "))
    sum_div = ((side_a + side_b + side_c)/2)
    area_squared = (sum_div*(sum_div-side_a)*(sum_div-side_b)*(sum_div-side_c))
    area = math.sqrt(area_squared)
    print("area is", area)
#triangle_area()

def sum_squares():
    lower = eval(input("Enter lower range: "))
    upper = eval(input("Enter upper range: "))
    sum_squares_acc = 0
    for i in range(lower, upper + 1, 1):
        sum_squares_acc = sum_squares_acc + (i*i)
    print(sum_squares_acc)

def power():
    base = eval(input("Enter base: "))
    exponent = eval(input("Enter exponent: "))
    power_acc = 1
    for i in range(exponent):
        power_acc = power_acc * base
    print(base, "^", exponent, "=", power_acc)


if __name__ == '__main__':
    pass
