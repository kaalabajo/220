"""
Name: Kaala Bajo
lab2.py

Problem: This program calculates 3 different means.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def means():
    vals = eval(input("How many values do you need to enter? "))

    #here are my little variables to add up stuff
    rms_acc = 0
    harm_acc = 0
    geom_acc = 1

    for i in range(vals):
        number = eval(input("Enter a number: "))
        x_square = number ** 2
        rms_acc = rms_acc + x_square
        harm_acc = harm_acc + 1/number
        geom_acc = geom_acc * number

    geometric = geom_acc ** (1 / vals)

    print("RMS:", (rms_acc/vals)**.5)
    print("Harmonic:", vals/harm_acc)
    print("Geometric:", (geometric))


means()