"""
Created By: Nicholas Ruppel
System Biology Exercise Practice
Week 3 Exercise
10/14/19
"""
import string
import random


# First function To deal with random number generation
def randomword3(length):
    String = set(string.ascii_lowercase)  # Set of ascii characters

    mystring = " " # my string is the created varible to hold info
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

finalString1 = randomword3(10)
print(finalString1)
