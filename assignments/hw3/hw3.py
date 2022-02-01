"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def average():
    grades = eval(input("How many grades will you enter?"))
    grade_acc = 0
    for i in range(grades):
        grade_acc = grade_acc + (eval(input("Enter grade: ")))
    avg_grade = grade_acc/grades
    print("Average is", avg_grade)
#average()

def tip_jar():
    tip = 0
    for i in range(5):
        tip = tip + (eval(input("How much would you like to donate? ")))
    print("total tips: ", tip)
tip_jar()
def newton():
    pass


def sequence():
    pass


def pi():
    pass


if __name__ == '__main__':
    pass
