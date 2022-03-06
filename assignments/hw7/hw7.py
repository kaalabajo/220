"""
Kaala Bajo
hw7.py

Problem: This program solves a series of problems
         involving reading/writing files.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def number_words(in_file_name, out_file_name):
    # My_file = open("data.txt", "r")
    #my_file.read()
    my_file = open(in_file_name, "r")
    out_f = open(out_file_name, "w")
    line = my_file.read().split()
    for i in range(len(line)):
        print(i+1, line[i], file=out_f)

    my_file.close()
    out_f.close()
def hourly_wages(in_file_name, out_file_name):
    in_f = open(in_file_name, "r")
    out_f = open(out_file_name, "w")
    line = in_f.readlines()
    for name in line:
        name = name.split(" ")
        first_last = str(name[0]+" "+ name[1])
        pay_og = float(name[2])
        hours = float(name[3])
        new_pay= pay_og+1.65
        this_week = hours*new_pay
        print(first_last + " {0:0.2f}".format(this_week), file=out_f)

    in_f.close()
    out_f.close()
def calc_check_sum(isbn):
    no_dash = (isbn.replace("-", ""))
    acum = 0
    list_of_nums = [10,9,8,7,6,5,4,3,2,1]
    new_list = []
    for number in no_dash:
        new_list.append(int(number))
    for i in list_of_nums:
        acum = acum + (i * new_list[list_of_nums.index(i)])
    return acum

def send_message(file_name, friend_name):
    in_files = open(file_name, "r")
    alt = friend_name+".txt"
    out_files = open(alt, "w")


    all_lines = in_files.readlines()
    for thing in all_lines:
        print(thing.replace("\n",""),file=out_files)

    in_files.close()
    out_files.close()
#send_message("hourly_wages.txt", "beep")

def encode(my_msg, my_key):
    code = ""
    for letter in my_msg:
        num = ord(letter)
        code = code + chr(num + my_key)
    return code

def send_safe_message(file_name, friend_name, key):
    the_in = open(file_name, "r")
    alt = friend_name+".txt"
    the_out = open(alt, "w")
    all_lines = the_in.readlines()
    for thing in all_lines:
        print(encode(thing.replace("\n",""),key),file=the_out)

    the_out.close()
    the_in.close()

def send_uncrackable_message(file_name, friend_name, pad_file_name):
    pass
if __name__ == '__main__':
    pass
