"""
class - definition of what a object is
    elements:
        1) constructor (Circle(P(1,2),2)
        2) instance vars
           data describing object (ie radius)
           this data is stored in some variable
           can't always tell what the instance vars are
        3) methods
           what an object can do. often acts on instance variables (like move)
           we use these to do something to the object

object - instance of a class

circle
c = Circle(Point(3,4),3)
d = Circle(P(4,5),5) these are two diff objects

if its a car
you can have a class of car that makes cars (like factory analogy)
we can use that to make specific cars (all have  wheels, engine, weight, type)

lets make a class for a die
instance var:
    # of sides
    value

class Die:
    #constructor vvvv
    def __init__(self,num_sides):
        self.sides = num_sides #self is particular instance of the function
        self.value = 1 #instance vars
    def get_value(self): #returns self.value #methods. This is a GETTER. Usually have these for all parts
        return self.value
    def set_value(self,value):
        self.value=value
    def roll(self):
        new_val = randint(1,self.sides)
        self.value = new_val




d = Die(4)
d.get_value()
    that returns 4



used like this:
from Die import Die
    main():
    d = Die(3) #3 sided die
"""

from Die import Die
from Die import Student
def main():
    num_of_sides =  eval(input('how many '))
    my_die = Die(num_of_sides)
    playing = True
    while playing:
        my_die.roll()
        print(my_die.get_value())
        stopping = input('hit enter to reroll ')
        playing = not stopping

def main2():
    my_student = Student("joe",8,12)
    student_file = open("../second exam/student.txt", 'r')
    student_file.readline() #throwing first line away

    students = []
    for line in student_file.readlines():

        split_line = line.split(",")
        name = split_line[0]
        credit_hours = split_line[1]
        qp = split_line[2]
        student = Student(name,credit_hours,qp)
        students.append(student)
    best = students[0]
    for student in students:
        print(student.get_name(), student.get_gpa())
        if student.get_gpa() > best.get_gpa():
            best = student
    print('best student is {0} with gpa {1}'.format(best.get_name(),best.get_gpa()))

if __name__ == '__main__':
    main2()

"""
doc strings describe whats going on in a class for documentation purposes and you should
see employee.py
"""