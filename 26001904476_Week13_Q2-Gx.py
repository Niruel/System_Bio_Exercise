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

#plotting g(x) function from documentation
y = [50 * math.sin(i) + i**2 + 100 for i in range(-30, 30)]
x = [i for i in range(-30, 30)]
plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("G(x)")
plt.show()