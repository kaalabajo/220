"""
Kaala Bajo
hw6.py

Problem: This program solves a series of problems
         involving strings and formatting.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math
def cash_converter():
    the_int = eval(input("enter an integer "))
    print("That is ${0:0.2f}".format(float(the_int)))

def encode():
    my_msg = input("enter a message: ")
    my_key = eval(input('enter a key: '))
    code = ""
    for letter in my_msg:
        num = ord(letter)
        code = code + chr(num+my_key)
    print(code)
#The time has come, the Walrus said

def sphere_area(radius):
    #4pirad**2
    return 4 * math.pi * (radius**2)

def sphere_volume(radius):
    #4/3 pi r**2
    return (4/3) * math.pi * (radius**3)

def sum_n(number):
    num_acc = 0
    for i in range(number+1):
        num_acc = num_acc + i
    return num_acc

def sum_n_cubes(number):
    num_acc = 0
    for i in range(number+1):
        num_acc = num_acc + i**3
    return num_acc


def encode_better():
    code = input("enter a message: ")
    key = input("enter a key: ")

    track_code = []
    track_key = []
    for letter in code:
        track_code.append(ord(letter) - 65)
    for letter in key:
        track_key.append(ord(letter) - 65)
    #print(track_code,track_key)
    # make a new list to keep track of the number versions
    nums = []
    for i in range(len(code)):
        looped = int(track_code[i]) + int(track_key[i % len(key)])
        nums.append(looped%58)

    # ciphered is a blank string that will add all our letters
    ciphered = ''
    for i in nums:
        ciphered = ciphered + chr(i+65)
    print(ciphered)
if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
