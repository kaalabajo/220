"""

"""
import math
def my_first_while():
    for i in range(5):
        print(i, end = ' ')
    print('\n{0:-<70}'.format(""))

    i = 0
    while i <5:
        print(i, end=' ')
        i = i + 1

def is_equal(p1,p2):
    if p1.getX() == p2.getX() and p1.getY() == p2.getY():
        return True
    else:
        return False

#make this more efficient

def is_equal_2(p1,p2):
    return p1.getX() == p2.getX() and p1.getY() == p2.getY()

"""
not/and/or
not is a unary operator
ORDER OF OPERATIONS
    not -> and -> or 
    parentheses obvi take importance
        "a or not b and c" assume all bools
        (a or ((not b) and c)) 
"""

def is_game_over3(p1_points, p2_points):
    if p1_points >= 15 and p1_points - p2_points >= 2: #must win by 2 and be over 15
        return True
    if p2_points >= 15 and p2_points - p1_points >= 2:
        return True
    return False

#def is_game_over(p1,p2):
#    over_fifteen = if p1 >= 15 or p2 >= 15
#    won_two = abs(p1 -p2)>=2
#    skunked = p1 >= 7 and p2 == 0 or p2 >= 7 and p1 == 0
##        return True
 #   return False


#if __name__ == '__main__':
    player1 = 0
    player2 = 0
    game_over = is_game_over(player1,player2)
    while not is_game_over(player1,player2):
        onepoints, twopoints = eval(input("enter scores "))
        player1 = player1 + onepoints
        player2 = player2 + twopoints
        print(player1,player2)
    print('over!')

'''
Distributive property
a or (b and c) == (a or b) and (a or c)
a and (b or c) == (a and b) or (a and c)

DeMorgan's law
not (a or b) == not a and not b
not (a and b) == not a or not b
'''
def deMorgan_one(a,b):
    return not (a or b) == (not a and not b)

def deMorgan_test():
    my_tests = [
        [True, True], [True,False], [False, True], [False,False]
    ]
    for test in my_tests:
        a = test[0]
        b = test[1]
        result = deMorgan_one(a,b)
        print(result)

"""
break
breaks out of a loop
if x happens:
    break
    
truthy/falsey values
    if 0:
        print('ok') considered false
    if -1:
        print('ok') considered true


x!= 0 is true
0 is false

for any list:
if it has values, its true
if its empty its false

True or False
"" and "hello" (returns blank)
"hello" or "world" (returns hello)
not 0 = true
not 1 = false
not "" = true
not "hello" = false
1 or sqrt(9) = 1
1 or sqrt(-9) = 1 because it never got to run
sqrt(-9) or 1 = short circuit

x = -9
if x > 0 and sqrt(x)>3

a and y = if x is false return x. else return y
x or y = if x is true, return x. else return y
not x = if x is false, return true. else return false
"""

def whoops():
    user_input = input("do u wanna donate all ur money to Henry?: ")
    if user_input == "y" or "YES": #this doesnt work because any input evals to true
        print("Transferring...") #or'ing with a true value. Anything or true will always be true
    else: #we will never hit this
        print("boo")

def correct():
    user_input = input("do u wanna donate all ur money to Henry?: ")
    if user_input == "y" or user_input=="Y" or user_input=="yes":
        print("yessah")
    else:
        print("boo")

def icecream():
    favorite = input('what is your fav icecream [vanilla]: ') or 'vanilla'
    print('your fav is {}'.format(favorite))
    #refactored to hell

def average():
    n = eval(input('how many numbers'))
    sum = 0
    for i in range(n):
        userinput = eval(input('enter number'))
        sum = sum + userinput
    print("average is {}".format(sum/n))

def while_interactive():
    ans = 'y'
    sum = 0
    count = 0
    while ans[0] == "y":
        userinput = eval(input('enter number: '))
        sum = sum + userinput
        count = count + 1
        ans = input('do u have any more numbers: ')
    print("average is {}".format(sum/count))

def while_sentinel():
    ans = 'y'
    count = -1
    num = eval(input('enter a number (neg to exit) >>> '))

    acc = 0
    while num >= 0:
        acc = acc + num
        count = count + 1
        num = eval(input('enter a number (neg to exit) >>> ' ))

    print("average is {}".format(acc/count))

def better_sentinel():
    count = 0
    num = input('enter a number (enter to exit) >>> ')
    acc = 0
    while num != "":
        acc = acc + eval(num)
        count = count + 1
        num = input('enter a number (enter to exit) >>> ' )

    print("average is {}".format(acc/count))

def avg_file():
    acc = 0
    count = 0
    file_name = 'file_data.txt'
    file = open(file_name, 'r')
    for line in file:
        num = eval(line)
        acc = acc + num
        count = count + 1
    print("average is {}".format(acc / count))


def avg_file_while():
    acc = 0
    count = 0
    file_name = 'file_data.txt'
    file = open(file_name, 'r')
    line = file.readline()
    while line != "":
        num = eval(line)
        acc = acc + num
        count = count + 1
        line = file.readline()
    print("average is {}".format(acc / count))

def avg_file_nested():
    acc = 0
    count = 0
    file_name = 'nested_data.txt'
    file = open(file_name, 'r')
    for line in file:
        nums_string = line.split(',')
        for num in nums_string:
            acc = acc + num
            count = count + 1
    print("average is {}".format(acc / count))

def avg_file_nested_while():
    acc = 0
    count = 0
    file_name = 'nested_data.txt'
    file = open(file_name, 'r')
    line = file.readline()
    while line != "":
        nums_string= line.split(",")
        i = 0
        while i < len(nums_string) :
            num = nums_string[i]
            acc = acc + eval(num)
            count = count + 1
            i = i+1
        line = file.readline()
    print("average is {}".format(acc / count))