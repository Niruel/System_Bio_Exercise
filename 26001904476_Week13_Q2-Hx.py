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

#plot h(x) function from documentation
y = [
    15 * math.sin(i / 5)**2 * 75 * math.cos(i / 13) * 3 * math.sin(i / 7) +
    i**2 + 300 for i in range(-100, 100)
]
x = [i for i in range(-100, 100)]
plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("H(x)")
plt.show()