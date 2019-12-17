"""
Created By: Nicholas Ruppel
System Biology Exercise Practice
Week 11 Exercise
Neuroal Network
2019/12/09
"""
import numpy as np
import matplotlib.pyplot as plt
"""
Created 3 array sets for input data
and reference outputs
"""
#inputData = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
#referenceOutput = np.array([[0], [0], [1], [1]])

inputData = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
referenceOutput = [[0], [1], [1], [0]]

#inputData = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
#referenceOutput = np.array([[0], [1], [0], [1]])

weights01 = 0  # set the weight to zero for initalization


#create sigmoid function
def sigmoid(x):

    return 1 / (1 + np.exp(-x))


#create sigmoid slope
def sigmoidSlope(x):
    return x * (1 - x)


np.random.seed(42)  #set seed to 1
weights01 = 2 * np.random.random(
    (3, 1)) - 1  #this is the weght to change value of the matrix

trainingNumber = 900  #How many times run the program
trainingCounter = 0
y = []
for i in range(trainingNumber):

    #takes the input array
    inputLayer = inputData
    multiplier = np.dot(inputLayer, weights01)

    #take sigmoid and do some math to satisfy the function
    #outputPerceptronLayer = sigmoid(x)
    '''
    slopeChangeFactor   
    Change to 2 for sigmoid slope times 2
    change to .5 for other version of sigmoid slope
    '''
    slopeChangeFactor = 1
    outputPerceptronLayer = sigmoid(slopeChangeFactor * multiplier)

    roundedValue = np.round(
        outputPerceptronLayer,
        decimals=2)  #wanted to show the rounded value so i created the value

    #use np.array_equals  to check the input, but rounded with the reference we want

    outputError = referenceOutput - outputPerceptronLayer

    meanValue = np.mean(np.abs(outputError))
    y.append(meanValue)
    outputDelta = outputError * slopeChangeFactor * (
        sigmoidSlope(outputPerceptronLayer))

    weights01 += np.dot(inputLayer.T, outputDelta)

print("Output values after " + str(i) + " training itteration: ")
print(outputPerceptronLayer)
x = [i for i in range(trainingNumber)]

plt.plot(x, y)
plt.show()