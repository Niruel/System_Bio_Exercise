import random
import string



def randomword1(length):
    String=string.ascii_lowercase
    r=random.randint(0,len(String)-1)
    mystring=String[r]
   
    while(len(mystring)!=length):
        r=random.randint(0,len(String)-1)
        mystring+=String[r]

    return mystring



finalString =randomword1(2)
print(finalString)