"""
Created By: Nicholas Ruppel
System Biology Exercise Practice
Week 11 Exercise
Neuroal Network
2019/12/12
"""
import numpy as np
import matplotlib.pyplot as plt

#inputData = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
#referenceOutput = np.array([[0], [0], [1], [1]])

inputData = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
referenceOutput = [[0], [1], [1], [0]]


def sigmoid(x):

    return 1 / (1 + np.exp(-x))


def sigmoidSlope(x):
    return x * (1 - x)


np.random.seed(42)

weights01 = 2 * np.random.random((3, 4)) - 1
weights02 = 2 * np.random.random((4, 1)) - 1

trainingNumber = 900  #How many times run the program
y = []
for i in range(trainingNumber):

    #take sigmoid and do some math to satisfy the function

    #slopeChangeFactor = 2
    inputLayer = inputData
    hiddenLayer = sigmoid(np.dot(inputLayer, weights01))
    outputPerceptronLayer = sigmoid(np.dot(hiddenLayer, weights02))

    outputError = referenceOutput - outputPerceptronLayer

    outputDelta = outputError * sigmoidSlope(outputPerceptronLayer)
    meanValue = np.mean(np.abs(outputError))
    y.append(meanValue)
    '''if np.round(meanValue, decimals=3) == 0.004:
        print(outputError)
        break'''

    hiddenLayerError = outputDelta.dot(weights02.T)
    hiddenLayerDelta = hiddenLayerError * sigmoidSlope(hiddenLayer)

    weights02 += hiddenLayer.T.dot(outputDelta)
    weights01 += inputData.T.dot(hiddenLayerDelta)

x = [i for i in range(trainingNumber)]

plt.plot(x, y)
plt.show()
print("Output values after " + str(i) + " training itteration: ")
print(np.round(outputPerceptronLayer))
