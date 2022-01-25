def means():
    vals = eval(input("How many values do you need to enter? "))

    #basic mean
    #for i in range(vals):
    #    sum = sum + eval(input("Enter value: "))
    #mean = sum/vals

    #user_input = []
    #user_input_sqd = []
    #for i in range(vals):
    #    x = eval(input("Enter a number: "))
    #    vals_sqrd = x ** 2
    #    user_input.append(vals_sqrd)
    #    user_input_sqd.append(x)
    number_current = 0
    for j in range(3):
        number_current = eval(input("Enter a number"))

        #RMS
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
        print(harmonic)

    #geometric
    #pi (x1*x2*x3)

means()