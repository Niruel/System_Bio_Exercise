import numpy as np
import matplotlib as plt
def random_n(length):
    x = np.random.randint(0,10,length)
    plt.plot([length/11 for i in range(10)])
    plt.hist(x)
    plt.show()

random_n(100)