"""
Created By: Nicholas Ruppel
System Biology Exercise Practice
Week 12 Exercise
Swarn intelegence 
2019/12/25
"""
import random
import math
import matplotlib.pyplot as plt
#Plotting f(x) function from documentation
y = ([5 * (i - 20)**2 for i in range(-100, 100)])
x = [i for i in range(-100, 100)]
plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("F(x)")
plt.show()