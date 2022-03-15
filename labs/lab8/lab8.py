"""
Name: Kaala Bajo
lab8.py

Problem: This program takes numeric data from a file and
computes averages.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def weighted_average(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")
    line = in_file.readlines()

    for person in line:
        person = person.strip("\n").split(":")
        #above makes all lines a list. Obj 1 is name, obj 2 is grades

        name = person[0] #names of students
        grades = person[1] #grades as strings

        split_up_grades = grades.strip(" ").split(" ") #makes lists, each item is str
        for item in range(len(split_up_grades)):
            #print(split_up_grades[item]+split_up_grades[item+1])
            split_up_grades[item] = int(split_up_grades[item]) #aight, we have ints

            #listen, ik this isn't the most efficient way. but im dumb lmao
        multip_acc = 0
        weight_acc = 0
        for item in range(0, len(split_up_grades), 2):
            multip_acc += split_up_grades[item] * split_up_grades[item+1]
            weight_acc += split_up_grades[item]
        ending = 0
        weighted = multip_acc/100
        if weight_acc > 100:
            ending = "Error: The weights are more than 100."
        elif weight_acc < 100:
            ending = "Error: The weights are less than 100."
        elif weight_acc == 100:
            ending = weighted



        print(name.rstrip(" ")+"'s average: {}".format(ending),    file=out_file)

    in_file.close()
    out_file.close()


def main():
    weighted_average("grades.txt", "avg.txt")

if __name__ == '__main__':
    main()

