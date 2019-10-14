"""
Created By: Nicholas Ruppel
System Biology Exercise Practice
Week 3 Exercise
10/14/19
"""
import  string
import  random


def randomwordOdd(length):
    String = set(string.ascii_lowercase) # is a set of lower case ascii characters
    StrigH = string.ascii_uppercase #make an list of ascii uppercase characters
    Oddchar = set(StrigH[0:25:2]) #make the upper case ascii into a set and set it to a varible
    String.update(Oddchar) #add the odd characters to the exsisting set
    mystring = ""
    i = 0
    while i < length:  # while the length has not run out do something
        r = random.randint(1, len(String))  # set r to a random int in the string array
        count = 0
        for str in String:
            count += 1
            if count == r:
                if str.isupper(): #if the value chosen is an upper case odd
                    str = str.lower() #make it lowercase
                mystring += str  # let the varibile increment
        i += 1
    return mystring  # return final string

finalString = randomwordOdd(10)
print(finalString)

