"""
Created By: Nicholas Ruppel
System Biology Exercise Practice
Week 8 Exercise
Wolfram Rules
2019/11/20
"""
import string
import math
import random

size = 0 #set the a global size varible to be used in multiple locations

def RuleFunc(Num): #Set the rule with a varible for the rule number that can be entered by the user
    wolf_rule_string = "{0:{fill}8b}".format(int(Num), fill="0")

    wolfDict = {"111":wolf_rule_string[0],
            "110":wolf_rule_string[1],
            "101":wolf_rule_string[2],
            "100":wolf_rule_string[3],
            "011":wolf_rule_string[4],
            "010":wolf_rule_string[5],
            "001":wolf_rule_string[6],
            "000":wolf_rule_string[7]}
    return wolfDict #return the dictionary that will be used as the dictionary


def wolfram_fkt(wolfDict, itSize): #Call the dictionary and set a varible for iterration size (that the user will interact with)
    
    iterstr= "0"*math.floor(size/2)+ "1" + "0"*math.floor(size/2)
    
    for _ in range(itSize):
        x =""
        for i in range(len(iterstr)-2):
            x += wolfDict[iterstr[i:i+3]]
        
        b="0{}0".format(x)
        iterstr=b          
        c=b.replace("1", "#")
        print(c.replace("0", "*"))

def wolfram_fkt_rand(wolfDict, itSize):#--This function is for random user choice-- Call the dictionary and set a varible for iterration size (that the user will interact with)
    randSelect = ["0","1"]
    iterstr = ""
    for _ in range(size+1):
        iterstr = iterstr + random.choice(randSelect)
    
    for _ in range(itSize):
        x =""
        for i in range(len(iterstr)-2):
            x += wolfDict[iterstr[i:i+3]]
        
        b="0{}0".format(x)
        iterstr=b          
        c=b.replace("1", "#")
        print(c.replace("0", "*"))


'''
Because this is all about user input I prefer one comment block 

First we have 3 while loops if the user input is not the desierd input
Then get three different user input and if asked for an interger it must be casted to an int
Try/Except if user input is correct
'''
if __name__ == "__main__":
    while True:
        userInput= input("Enter a  Number between 0 ~ 255: ")
        try:
            userInt = int(userInput)

            if userInt < 0 or userInt >255:
                print("Please Enter a number between 0 ~ 255")
            else:
               
                break
        except:
            print("Please Enter a number between 0 ~ 255")
    while True:
        userIttSize = input("Enter a number for itteration size: ")
        try:
            userIt= int(userIttSize)
            size = userIt * 2
            break
        except:
            print("Please Enter a number")
    
    while True:
        randChoicein = input("Choose a character R for random or N for not random ")
        if randChoicein=='r':
            wolfram_fkt_rand(RuleFunc(userInt),userIt)
            break
        if randChoicein=='n':
            wolfram_fkt(RuleFunc(userInt),userIt)
            break








