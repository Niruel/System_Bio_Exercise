import  string
import  random


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

finalString = randomwordOdd(10)
print(finalString)

