"""
Name: Kaala Bajo
algorithms.py

Problem: Adds read data to a list and does a linear search

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def read_data(filename):
    in_f = open(filename, "r")
    all_text = in_f.read()
    all_text = all_text.replace("\n", " ")
    split_text = all_text.split(" ")
    i = 0
    num_list = []
    while i < len(split_text):
        num_list.append(eval(split_text[i]))
        i += 1
    in_f.close()
    return num_list

def is_in_linear(search_val, values):
    #return search_val in values
    i = 0
    while i < len(values):
        if search_val == values[i]:
            i += 1
            return True
        else:
            i += 1
    return False


