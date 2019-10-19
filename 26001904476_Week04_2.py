import timeit
import numpy as np
import matplotlib.pyplot as plt


def ElephantValley():
    Equation(1000,100,0.24,0.4,-0.1,0.1)

def SeahorseValley():
    Equation(1000,100,-0.85,-0.65,0.0,0.2)

def Mandelbrot():   
    Equation(1000,100,-2,0.5,-1,1)

def Equation(n,itteration_num,xMin,xMax,yMin,yMax):
    M = np.zeros([n,n],int)
    xval = np.linspace(xMin,xMax,n)
    yval = np.linspace(yMin,yMax,n)
    for u,x in enumerate(xval):
        for v,y in enumerate(yval):
            z= 0+0j
            C =complex(x,y)
            for n in range(itteration_num):
                z=z*z + C
                if abs(z)> 2.0:
                    M[v,u]=1
                    break
    plt.imshow(M,origin="lower",extent=(xMin,xMax,yMin,yMax))
   
if __name__ == "__main__":

    u_input_Text = input("Choose which plot you would like to see [1-3]:")
    u_input_num=int(u_input_Text)
    if(u_input_num==1):
        Mandelbrot()     
    elif(u_input_num==2):
        ElephantValley()
    elif(u_input_num==3):
        SeahorseValley()

    plt.gray()
    plt.show()


