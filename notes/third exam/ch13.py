"""
searching sorting recursion
searching is important
there are  many sorting algorithms out there

"""

def linear_search(my_list, target):
    for i in range(len(my_list)):
        if my_list[i] == target:
            return i
    return -1

"""
easier to search if things are sorted
"""

def binary_search(my_list, target):
    left_index = 0
    right_index = len(my_list) - 1
    while left_index <= right_index:
        middle_index = (left_index + right_index)//2
        middle_value = my_list[middle_index]
        if middle_value== target:
            return middle_index
        elif middle_value < target:
            left_index = middle_index + 1
        else:
            right_index = middle_index - 1
    return -1
"""
big o notation
worst case
how many comps do i have to make in the worst case scenarios

Linear
Best case
O(1)
Worse case
O(n)

Binary
Worst case
O(log n)
if n = 8 -> 4
Best case
O(1) in the middle
"""

"""recursion"""
def print_hi():
    print("hi")
    print_hi() #python will stop the recursive function at some point automatically

"""
so whats happening?
runs through what has been put
if you go too deep its stack overflow
base case: how many times to loop? when are we done
"""

def print_repeat(s,n):
    if n == 0:
        return
    else:
        print(s)
    print_repeat(s, n-1)

"""
creates looping behavior w no loops
"""

def sum_list(l):
    if len(l) == 0:
        return 0
    else:
        return l[0] + sum_list(l[1:])

def sum_list_tail(l,s):
    if len(l) == 0:
        return s
    else:
        s += l[0]
        return sum_list_tail(l[1:], s)

def rev(word):
    acc = ''
    for i in range(len(word)):
        acc = word[i] + acc
    return acc

def rev_rec(word):
    if len(word) <= 1:
        return word
    return rev_rec(word[1:]) + word[0]

def rev_rec_tail(word,acc):
    if len(word) <= 1:
        return word + acc
    acc = word[0] + acc
    return rev_rec_tail(word[1:],acc)

def fib(n):
    curr = 1
    prev = 1
    for i in range(n-2):
        sum = curr + prev
        prev = curr
        curr = sum
    return curr

def fib_rec(n):
    if n < 3:
        return 1
    return fib_rec(n-1) + fib_rec(n-2)

"""
SELECTION SORT
keeps track of first then loops through rest of items
is this smaller than this? yes? move to front

MERGE SORT
splits everything til its down to 1
compares the branches to eachother and puts them back in order
does it recursively
"""

if __name__ == '__main__':
    print(rev_rec('walrus'))
    print(rev_rec_tail('walrus', ''))
    print(fib(10))
    print(fib_rec(10))

    # print_repeat('boobies',4)
    # s = sum_list([1,2,3,4])
    # t = sum_list_tail([1,2,3,4], 0)
    #
    # print(t)


    # my_list = [3,4,5,2,6,81,45,69,101]
    # target = 3
    # #result = linear_search(my_list,7)
    # my_list.sort()
    # result = binary_search(my_list,target)
    # if result >= 0:
    #     print('found it', result)
    # else:
    #     print('no')