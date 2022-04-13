"""
Name: Kaala Bajo
lab12.py

Problem: Uses while loops to do various things.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from random import randint
def find_and_remove_first(list, value):
    #list.remove(value)
    list.insert(list.index(value),"Ka'ala")
    list.remove(value)

def good_input():
    user_input = eval(input("Enter a number between 1 and 10 inclusive: "))
    good_fr = ""
    while good_fr == "":
        if user_input in range(1,11):
            good_fr = user_input
        else:
            print("...it needs to be from 1 to 10 dude")
            user_input = eval(input("Enter a number between 1 and 10 inclusive: "))

def num_digits():
    user_input = eval(input("Enter a positive integer, 0 or - to stop: "))
    current_input = 1
    while user_input != 0 and user_input > 0:
        if type(user_input) == float:
            print('number must be a positive integer')
            user_input = eval(input("Enter a positive integer, 0 or - to stop: "))
            current_input = user_input
        else:
            current_input = user_input

            num_acc = 0
            lil_placeholder = current_input

            while lil_placeholder != 0:
                lil_placeholder = lil_placeholder//10
                num_acc += 1
            print(num_acc)
            user_input = eval(input("Enter another positive integer, 0 or - to stop: "))

def hi_lo_game():
    secret_num = randint(1,100)
    print(secret_num)
    guess_acc = 0
    i = 0

    user_guess = eval(input("enter a guess (1 - 100): "))
    while i == 0:
        if user_guess > secret_num:
            print("too high")
            guess_acc += 1
            user_guess = eval(input("enter a guess (1 - 100): "))
        elif user_guess < secret_num:
            print("too low")
            guess_acc += 1
            user_guess = eval(input("enter a guess (1 - 100): "))
        else:
            print("correct!\nyou win in {} guesses".format(guess_acc))
            i += 1
        if guess_acc == 6:
            print('Sorry, you lose. The number was {}'.format(secret_num))
            i+=1
