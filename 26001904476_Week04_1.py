import timeit
import numpy as np
import matplotlib.pyplot as plt

startTime = timeit.default_timer()
def Mandelbrot(n, itteration_num, m_origin=" "):
    
   
    M = np.zeros([n,n],int)
    xval = np.linspace(-2,0.5,n)
    yval = np.linspace(-1,1,n)
    for u,x in enumerate(xval):
        for v,y in enumerate(yval):
            z= 0+0j
            C =complex(x,y)
            for n in range(itteration_num):
                z=z*z + C
                if abs(z)> 2.0:
                    M[v,u]=1
                    break
    plt.imshow(M,origin=m_origin,extent=(-2,0.5,-1,1))
    plt.gray()
    plt.show()
Mandelbrot(200,100,"upper")
stopTimer=timeit.default_timer()

print("This took " + str(stopTimer-startTime)[0:5] + " Seconds to run")





