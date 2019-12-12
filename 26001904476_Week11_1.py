"""
Created By: Nicholas Ruppel
System Biology Exercise Practice
Week 11 Exercise
Neuroal Network
2019/12/09
"""
import numpy as np
import random
"""
Created 3 array sets for input data
and reference outputs
"""
inputData = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
referenceOutput = np.array([[0], [0], [1], [1]])

#inputData = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
#referenceOutput = [[0], [1], [1], [0]]

#inputData = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
#referenceOutput = np.array([[0], [1], [0], [1]])

weights01 = 0  # set the weight to zero for initalization


#create sigmoid function
def sigmoid(x):

    return 1 / (1 + np.exp(-x))


#create sigmoid slope
def sigmoidSlope(x):
    return x * (1 - x)


np.random.seed(1)  #set seed to 1
weights01 = 2 * np.random.random(
    (3, 1)) - 1  #this is the weght to change value of the matrix

trainingNumber = 100000  #How many times run the program
trainingCounter = 0

for i in range(trainingNumber):
    trainingCounter += 1  #increment while going through for loop

    #takes the input array
    inputLayer = inputData
    #inputLayer = inputData2
    # inputLayer = inputData3
    x = np.dot(inputLayer, weights01)

    #take sigmoid and do some math to satisfy the function
    #outputPerceptronLayer = sigmoid(x)
    '''
    slopeChangeFactor   
    Change to 2 for sigmoid slope times 2
    change to .5 for other version of sigmoid slope
    '''
    slopeChangeFactor = 2
    outputPerceptronLayer = sigmoid(slopeChangeFactor * x)

    roundedValue = np.round(
        outputPerceptronLayer,
        decimals=2)  #wanted to show the rounded value so i created the value

    #use np.array_equals  to check the input, but rounded with the reference we want
    if np.array_equal(referenceOutput, roundedValue):
        print(roundedValue)
        break
    outputError = referenceOutput - outputPerceptronLayer

    outputDelta = outputError * slopeChangeFactor * (
        sigmoidSlope(outputPerceptronLayer))

    weights01 += np.dot(inputLayer.T, outputDelta)

print("Output values after " + str(trainingCounter) + " training itteration: ")
print(outputPerceptronLayer)
