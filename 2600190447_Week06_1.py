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
alive = 1 #one life 
dead = 0 #zero deth
vals = [alive,dead]
grid[2:10,2:10]=cross #set the grids position 

def animated_universe(framenumber, *args, **kwargs):
    global grid
   # global animatedcount (not sure what this is for therefore i commented it out)
    newGrid = grid.copy()
    for i in range(universe):
        for j in range(universe):
            total = (grid[i,(j-1)%universe]+
            grid[i,(j+1)%universe] +
            grid[i-1%universe,j] + grid[(i+1)%universe,j] +
            grid[(i-1)%universe, (j-1)%universe] +grid[(i-1)%universe, (j+1)%universe] +
            grid[(i+1)%universe,(j-1)%universe]+ grid[(i+1)%universe, (j+1)%universe])/alive 
            #Rules for life and death of cells
            if grid[i,j] == alive:
                if (total < 2) or (total > 3):
                    newGrid[i,j] = dead
            else:
                if total == 3:
                    newGrid[i,j] = alive
    if(cross== grid[2:10,2:10]).all():
        print("pattern cross is detected")#Detects that patern is running

    grid = newGrid.copy()
    mat.set_data(grid)
    return mat

fig, ax = plt.subplots()
mat = ax.matshow(grid)
frameInterval = 400 #set the frame rate to slow it down to get a better picture (don't like hard coded values)
#Animate the cross 
ani = animation.FuncAnimation(fig,animated_universe,interval=frameInterval)

#Plot the final picture
plt.show()

