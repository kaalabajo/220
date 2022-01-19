"""
Name: Ka'ala Bajo
hw1.py

Problem: These take user input and run arithmatic on them to solve simple problems!

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    v_length = eval(input("Enter the length: "))
    v_width = eval(input("Enter the width: "))
    v_height = eval(input("Enter the height: "))
    volume = v_height * v_length * v_width
    print("Volume =", volume)


def shooting_percentage():
    total_shots = eval(input("Enter the player's total shots: "))
    shots_made = eval(input("Enter how many shots the player made: "))
    shooting_per = (shots_made/total_shots) * 100
    print("Shooting percentage: ", shooting_per,"%")


def coffee():
    coffee_order = eval(input("How many pounds of coffee would you like? "))
    raw_cost = (coffee_order * 10.50) + (coffee_order * .86) + 1.50
    rounded_total = round(raw_cost, 2)
    print("Your total is: $", rounded_total)

def kilometers_to_miles():
    km_traveled = eval(input("How many kilometers did you travel? "))
    miles = km_traveled / 1.61
    print("That's", miles, "miles!")

kilometers_to_miles()


if __name__ == '__main__':
    pass
