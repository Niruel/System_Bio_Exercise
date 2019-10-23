"""
Mandelbrot function
Created By: Nicholas Ruppel
Class: System Bio Exercise
2019/10/23
"""
#import correct libraries
import timeit
import numpy as np
import matplotlib.pyplot as plt

startTime = timeit.default_timer() # Track time start of function running
def Mandelbrot(n,itteration_num,xMin,xMax,yMin,yMax): # Create the the function with 6 input params
    
   
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
    plt.gray() #Plot as a grayscale image
    plt.show() #output the graph

Mandelbrot(1000,100,-2,0.5,-1,1) #Call the funtion to be used
stopTimer=timeit.default_timer()#Stop time for function
print("This took " + str(stopTimer-startTime)[0:5] + " Seconds to run") #Print the value it took for function to run





