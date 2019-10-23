import numpy as np
import matplotlib.pyplot as plt

def random_n(length):
    x = np.random.randint(0,10,length)
    
    plt.hist(x)
    plt.show()

def Mean(length):
     cltman = []
     x = np.random.randint(0,10,length)
     plt.plot([length/11 for i in range(10)])
     xMean = np.mean(x)
     cltman.append(xMean)
     plt.hist(xMean)
     plt.show()

#random_n(100)
Mean(100)