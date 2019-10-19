import timeit
import numpy as np
import matplotlib.pyplot as plt

startTime = timeit.default_timer()
def Mandelbrot(n,itteration_num,m_origin=" "):
    
   
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
Mandelbrot(32,40,"upper")
stopTimer=timeit.default_timer()

print("This took " + str(stopTimer-startTime)[0:5] + " Seconds to run")




#dType.GetHOMEParams(api)
#dType.SetHOMECmd(api, temp, isQueued=0)
dType.SetPTPJointParams(api, 200, 300, 500, 100, 400, 200, 600, 400, isQueued=0)
dType.GetPTPJointParams(api)

dType.SetPTPCoordinateParams(api, 100, 100, 100,  100,  isQueued=0)
pos = dType.GetPose(api)
moveX=0;moveY=0;moveZ=10;moveFlag=-1
x = pos[0]
y = pos[1]
z = pos[2]
rHead = pos[3]

while True:
moveFlag *= -1
   	for i in range(5):
        dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, x+moveX, y+moveY, z+moveZ, rHead, 1)
        moveX += 10 * moveFlag
        dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, x+moveX, y+moveY, z+moveZ, rHead, 1)
        dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, x+moveX, y+moveY, z, rHead, 1)
