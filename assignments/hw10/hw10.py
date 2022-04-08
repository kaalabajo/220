"""
Ka'ala Bajo
hw10.py

This program practices using while loops and booleans!

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def fibonacci(num):
    #set up accs
    loop_acc = 2
    fib_minus_one = 1
    fib_acc = 1
    #if its the first few numbers just cheat lol
    if num < 1:
        return None
    if num in (2,1):
        return 1
#1, 1, 2, 3, 5, 8,
    #while loop handles at only n = 3 and up
    while loop_acc != num:
        fib_acc += fib_minus_one

        loop_acc += 1
        fib_minus_one = fib_acc - fib_minus_one
    return fib_acc

def double_investment(principle, rate):
    year_acc = 0
    total_money = principle

    while total_money < principle*2:
        total_money = total_money + (total_money * rate)
        year_acc += 1
    return year_acc

def syracuse(num):
    current = num
    syra_list = [num]
    while current != 1:
        if current%2 == 0:
            syra_list.append(current//2)
        else:
            syra_list.append((current*3)+1)
        current = syra_list[-1]
    return syra_list

def is_prime(number):
    #to use in my next one, takes a number and returns True if prime
    i = 2 #fake for loop acc
    end = number/2 #div by two bc if the num can be /2 it aint prime
    while i < end:
        if number%i == 0:
            return False
            break
        i+=1
    return True

def goldbach(num):
    if num%2 == 0:
        loop = 2
        primes = []
        i = 0
        two_primes = []
        while loop < num:
            if is_prime(loop):
                primes.append(loop)
            loop += 1
        while i < len(primes):
            if num - primes[i] in primes:
                two_primes.append(primes[i])
                two_primes.append(primes[primes.index(num-primes[i])])
                break
            i += 1
        return two_primes
    return None
