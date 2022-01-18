"""
Ka'ala Bajo
lab1.py
This program calculates monthly interest on a credit card!
I certify that this assignment is entirely my own work.

"""
def credit_card_calc ():
    an_interest = eval(input("First, please enter your card's annual interest rate: "))
    monthly_interest_rate = an_interest/100/12
    billing_cycle = eval(input("Please enter the number of days in your billing cycle: "))
    prev_bal = eval(input("Please enter your previous balance: "))
    payment_amount = eval(input("Now please enter your payment amount: "))
    day_of_cycle = eval(input("Finally, please enter the day of the cycle when that payment was made: "))


    #step 1
    step_1 = prev_bal * billing_cycle
    #step 2
    step_2 = payment_amount * (billing_cycle - day_of_cycle)
    #step 3
    step3 = step_1 - step_2
    #step 4
    step_4 = step3 / billing_cycle

    monthly_interest = step_4 * monthly_interest_rate
    monthly_rounded = round(monthly_interest,2)
    print("Your monthly interest charge is: $", monthly_rounded)
    # print(MonthlyInterestRounded)

credit_card_calc()