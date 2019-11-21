"""
Created By: Nicholas Ruppel
System Biology Exercise Practice
Week 8 Exercise
Move/Maze 
2019/11/20
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

universe=100 #Set the universe size to 12 to give the osolator space to animate
grid = np.zeros((universe,universe)) #create the grid

#The cross  is what I choose and this what the binary array looks like

alive = 1 #one life 
dead = 0 #zero deth
vals = [alive,dead]


def animated_maze(framenumber, *args, **kwargs): #first is for maze
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
                if (total <= 5) and (total >= 1):
                    newGrid[i,j] = alive
                else:
                    newGrid[i,j] = dead
            else:
                if total == 3:
                    newGrid[i,j] = alive

    grid = newGrid.copy()
    mat.set_data(grid)
    return mat
def animated_move(framenumber, *args, **kwargs):
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
                if (total == 2) or (total == 4) or (total == 5):
                    newGrid[i,j] = alive
                else:
                    newGrid[i,j] = dead
            else:
                if (total == 3) or (total == 6) or (total == 8):
                    newGrid[i,j] = alive
                else:
                    newGrid[i,j] = dead

    grid = newGrid.copy()
    mat.set_data(grid)
    return mat



if __name__ == "__main__":
    '''
    user choice then result 
    need to be 1 for maze 2 for move function
    '''
    while True:
        choice = input("Choose 1 for maze or 2 for move")
        try:
            userin = int(choice)
            if userin < 1 or userin > 2:
                print("Please choose 1 or 2")
            elif userin == 1:
                grid = np.random.choice(vals,universe*universe,p=[0.05,0.95]).reshape(universe,universe)# ratio for maze 
                fig, ax = plt.subplots()
                mat = ax.matshow(grid)
                frameInterval = 100 #set the frame rate to slow it down to get a better picture (don't like hard coded values)
                #Animate the cross 
                ani = animation.FuncAnimation(fig,animated_maze,interval=frameInterval)
                #Plot the final picture
                plt.show()
                break
            elif userin ==2:
                grid = np.random.choice(vals,universe*universe,p=[0.2,0.8]).reshape(universe,universe)# ratio for move 
                fig, ax = plt.subplots()
                mat = ax.matshow(grid)
                frameInterval = 100 #set the frame rate to slow it down to get a better picture (don't like hard coded values)
                #Animate the cross 
                ani = animation.FuncAnimation(fig,animated_move,interval=frameInterval)
                #Plot the final picture
                plt.show()
                break
            else: 
                break
        except:
            print("Please choose 1 or 2")

