"""
Name: Kaala Bajo
hw3.py

Problem: This program utilizes for loops and
arithmatic to solve basic math problems.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def average():
    grades = eval(input("How many grades will you enter?"))
    grade_acc = 0
    for each_grade in range(grades): #just easier to read
        grade_acc = grade_acc + (eval(input("Enter grade: ")))
    avg_grade = grade_acc/grades
    print("Average is", avg_grade)
#average()

def tip_jar():
    tip = 0 #start 0 for acc w addition
    for each_tipper in range(5):
        tip = tip + (eval(input("How much would you like to donate? ")))
    print("total tips: ", tip)
#tip_jar()

def newton():
    number = eval(input("What number do you want to square root? "))
    approx = number
    times_to_improve = eval(input("Hpw many times should we improve the approximation? "))
    for approximation in range(times_to_improve):
        approx = (approx + (number/approx))/2
    print("The square root is approximately ", approx)
#newton()

def sequence():
    terms = eval(input("How many terms do ya want? "))

    for each_term in range(1, terms+1): #start 1 stop at terms +1 bc weird 0 system
        print((each_term-1) + each_term%2,end ="\t")
#sequence()

def pi():
    terms = eval(input("How many terms do ya want? "))
    #here be thine accumulators
    overall_acc = 1 #doing multiplication so start at 1
    num_track = 0
    denom_track = 0

    #and here is ye old for loop
    for i in range(terms):
        num_track = (i + (2 - (i % 2))) #term we r on + (2- (2, 4, 4, 6...)) 2- for 2 twice
        denom_track = (i + (1 + (i % 2)))
        overall_acc = overall_acc * (num_track/denom_track)
    print(overall_acc*2)
#pi()
if __name__ == '__main__':
    pass
