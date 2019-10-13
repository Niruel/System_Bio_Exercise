"""
System Biology Exercise Practice
Week 3 Exercise
10/12/19
"""
import string
import random


# First function To deal with random number generation
def randomword3(length):
    String = set(string.ascii_lowercase)  # array of ascii characters

    mystring = " "
    i = 0
    while i < length:  # while the length has not run out do something
        r = random.randint(1, len(String))  # set r to a random int in the string array
        count = 0
        for str in String:
            count += 1
            if count == r:
                mystring += str  # let the varibile increment
        i += 1
    return mystring  # return final string


def randomwordOdd(length):
    String = set(string.ascii_lowercase)
    StrigH = string.ascii_uppercase
    Oddchar = set(StrigH[0:25:2])
    String.update(Oddchar)
    print(String)
    mystring = ""
    i = 0
    while i < length:  # while the length has not run out do something
        r = random.randint(1, len(String))  # set r to a random int in the string array
        count = 0
        for str in String:
            count += 1
            if count == r:
                if str.isupper():
                    str = str.lower()
                mystring += str  # let the varibile increment
        i += 1
    return mystring  # return final string


finalString1 = randomword3(10)
finalString2 = randomwordOdd(10)
print(finalString1)
print(finalString2)
