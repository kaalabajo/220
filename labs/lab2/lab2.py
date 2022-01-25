"""
Name: Kaala Bajo
lab2.py

Problem: This program calculates 3 different means.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def means():
    vals = eval(input("How many values do you need to enter? "))

    #user_input = []
    #user_input_sqd = []

    rms_acc = 0
    harm_acc = 0
    for i in range(vals):
        x = eval(input("Enter a number: ")
        xsquare = x ** 2
        rms_acc = rms_acc + xsquare

        xs_squared_sum = 0
        for i in range(vals):
            xs_squared_sum = xs_squared_sum + (eval(input("Enter a number: "))**2)#raises each to power of 2 and adds to self
        print("RMS:", (xs_squared_sum/vals)**.5)

        #Harmonic
        h_sum = 0
        # summing 1/xn then div by n outside the loop
        for i in range(vals):
            h_sum = h_sum + ( 1/ eval(input("Enter a number: ")) )
        harmonic = vals/h_sum
        print("harmonic:", harmonic)

    #geometric
    g_prod = 1
    #pi (x1*x2*x3)
    for i in range(vals):
        g_prod = g_prod * eval(input("Input a number: "))
    geometric = g_prod**(1/vals)
    print("Geometric:", geometric)
means()