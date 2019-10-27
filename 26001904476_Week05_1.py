"""
Created By: Nicholas Ruppel
System Biology Exercise Practice
Cross osolator
Week 5 Exercise
10/28/19
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


universe=12 #Set the universe size to 12 to give the osolator space to animate
grid = np.zeros((universe,universe)) #create the grid

#The cross  is what I choose and this what the binary array looks like
cross = [
        [0,0,1,1,1,1,0,0],
        [0,0,1,0,0,1,0,0],
        [1,1,1,0,0,1,1,1],
        [1,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,1],
        [1,1,1,0,0,1,1,1],
        [0,0,1,0,0,1,0,0],
        [0,0,1,1,1,1,0,0]
        ]

grid[2:10,2:10]=cross #set the grids position
#plot the Cross osolator in black and white
plt.imshow(grid,cmap='binary')
plt.show()
