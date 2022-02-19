"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def name_reverse():
    name = input('enter a name (first last): ')
    listed = name.split()
    reverse_list = listed[1] + ", " + listed[0]
    print(reverse_list)

def company_name():
    domain = input('enter the domain: ')
    no_periods = domain.split(".")
    print(no_periods[1])

def initials():
    stud_num = eval(input('how many students are in the class: '))

    for i in range(stud_num):
        text = 'what is the name of student ' + str(i+1) + "? "
        name = input(text)
        name_split = name.split(" ")
        print(name_split[0][0] + name_split[1][0])

def names():
    pass

def thirds():
    pass

def word_average():
    pass


def pig_latin():
    pass


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
