"""
Mandelbrot function
Created By: Nicholas Ruppel
Class: System Bio Exercise
2019/10/23
"""
#import necessary libraries
import timeit
import numpy as np
import matplotlib.pyplot as plt

#Function for Elaphant valley values to be held
def ElephantValley():
    Equation(1000,100,0.24,0.4,-0.1,0.1)
#function for Seahorse valley values to be hel
def SeahorseValley():
    Equation(1000,100,-0.85,-0.65,0.0,0.2)
#Function for mandelbrot 
def Mandelbrot():   
    Equation(1000,100,-2,0.5,-1,1)

def Equation(n,itteration_num,xMin,xMax,yMin,yMax): #Create the the function with 6 input params
    
    M = np.zeros([n,n],int) #line resulotion 
    xval = np.linspace(xMin,xMax,n) #region spacing on the X axis
    yval = np.linspace(yMin,yMax,n) #region spacing for Y axis
    for u,x in enumerate(xval):
        for v,y in enumerate(yval):
            z= 0+0j #intailazation
            C =complex(x,y)
            for n in range(itteration_num):
                z=z*z + C
                #The absolute value of z going to indinity
                if abs(z)> 2.0:
                    M[v,u]=1
                    break
    plt.imshow(M,origin="lower",extent=(xMin,xMax,yMin,yMax))#Plot values that are inputed
   
if __name__ == "__main__": #Call main function

    u_input_Text = input("Choose which plot you would like to see [1-3]:") #String to choose an input number
    u_input_num=int(u_input_Text)#Cast string to int valley
    #Check input user chose and show appropriate function
    if(u_input_num==1):
        Mandelbrot()     
    elif(u_input_num==2):
        ElephantValley()
    elif(u_input_num==3):
        SeahorseValley()

    plt.gray()#Plot as a grayscale image
    plt.show()#output the graph


