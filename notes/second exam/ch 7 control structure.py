"""
control structure
 - for loop is a control structure. it makes program jump up
 - functions
 - decision structures
   - allows code to be executed depending on a condition

conditionals
  - conditionals return BOOLS (primitive) boolean
  - possible values: true, false (1, 0)

relational operators
  < less than
  < =
  >
  >=
  == is equal
  != not equal
"""
import math


def temp_convert():
    c_temp = eval(input("Enter the temp in C: "))
    f_temp = c_temp * 9 / 5 + 32 #expression
    print(f_temp)
    if f_temp >= 90:
        print("Heat warning")
    if f_temp <= 30:
        print("Cold warning")


if __name__ == '__main__':
    print(__name__)

"""
import ch7

def convert():

print(__name__)


MUTUALLY EXCLUSIVE
the disc here is either gonna be +0 or less than 0
"""

def quadratic(a,b,c):
    disc = b*b-4*a*c
    if disc >= 0:
        sqrt_discr = math.sqrt(b*b-4*a*c)
        denom = 2 * a
        root_1 = (-b + sqrt_discr) / denom
        root_2 = (-b - sqrt_discr) / denom
        return root_1,root_2
    else:
        return None,None
if __name__ == '__main__':
    r1, r2 = quadratic(2,3, -1)
    print('root 1:{} | root 2: {}'.format(r1,r2))

def quadratic2(a,b,c):
    disc = b*b-4*a*c
    if disc < 0:
        print('no root')
    else:
        if disc == 0: ###you can use elif here and it won't have to nest
            sqrt_discr = math.sqrt(disc)
            denom = 2*a
            root_1 = (-b + sqrt_discr) / denom
            print('double root at:',root_1)
        else:
            sqrt_discr = math.sqrt()

def quadratic3(a,b,c):
    disc = b*b-4*a*c
    if disc < 0:
        print('no root')
    elif disc == 0:
        sqrt_discr = math.sqrt(disc)
        denom = 2*a
        root_1 = (-b + sqrt_discr) / denom
        print('double root at:',root_1)

"""
LOGIC
    "and"
    whole will return true if all conditions are true
    
    "or"
    whole will return true if at least one is true
"""

def the_max(a,b,c):
    max_val = a
    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
    return max_val

print(the_max(1,2,3))

def bullshit(a,b,c):
    if a>b:
        if b > c:
            print("Spam please")
        else:
            print("its a late")
    elif b > c:
        print("cheese ")
        if a >= c:
            print("chddar")
        elif a < b:
            print("gouda")
        elif c == b:
            print("swiss")
    else:
        print("trees")
        if a == b:
            print("ches")
        else:
            print("larch")
    print("done")
bullshit(3,5,2)