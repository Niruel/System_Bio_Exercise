"""
Created By: Nicholas Ruppel
System Biology Exercise Practice
Week 12 Exercise
Neuroal Network Part 2
2019/12/18
"""
import numpy as np
import matplotlib.pyplot as plt
#Make a global varible for all functions to use and setit to 900
trainingNumber = 900


# the sigmoid function will return one / one + -x to exponent
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


#the slope is calculated by taking the dirivative of the sigmoid function
def sigmoidSlope(x):
    return x * (1 - x)


"""
This code has multiple functions named respectively as multilayer and single layer with number at the end
Therefore i will only indicate in the first two functions and the only one change in the other two functions.
"""


def multilayerNeuralNetwork01():
    y = []
    #The first output and input data that we are expecting.
    inputData = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
    referenceOutput = [[0], [1], [1], [0]]
    #need to set the seed before the random selection is preformed
    np.random.seed(42)

    #set a random weight for both the 3x4 matrix and the 4x1 matrix
    weights01 = 2 * np.random.random((3, 4)) - 1
    weights02 = 2 * np.random.random((4, 1)) - 1

    for i in range(trainingNumber):
        #Set the inputlayer for the rest of the function
        inputLayer = inputData
        hiddenLayer = sigmoid(np.dot(inputLayer, weights01))
        outputPerceptronLayer = sigmoid(np.dot(hiddenLayer, weights02))
        #This will be the difference between the output preception and the reference output
        outputError = referenceOutput - outputPerceptronLayer
        #need to set the output reference divergence to a variable
        outputDelta = outputError * sigmoidSlope(outputPerceptronLayer)
        meanValue = np.mean(
            np.abs(outputError))  #Take the mean output error subtraction
        y.append(meanValue)  # append the mean to give the y value to the graph

        hiddenLayerError = outputDelta.dot(weights02.T)
        hiddenLayerDelta = hiddenLayerError * sigmoidSlope(hiddenLayer)

        weights02 += hiddenLayer.T.dot(outputDelta)
        weights01 += inputData.T.dot(hiddenLayerDelta)

    x = [i for i in range(trainingNumber)
         ]  #put the training number for the x value
    return plt.plot(x, y)  #Finally plot the value


def multilayerNeuralNetwork02():
    y = []

    inputData = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
    referenceOutput = np.array([[0], [0], [1], [
        1
    ]])  #This reference output is the only difference to multilayer01 function

    np.random.seed(42)

    weights01 = 2 * np.random.random((3, 4)) - 1
    weights02 = 2 * np.random.random((4, 1)) - 1

    for i in range(trainingNumber):

        inputLayer = inputData
        hiddenLayer = sigmoid(np.dot(inputLayer, weights01))
        outputPerceptronLayer = sigmoid(np.dot(hiddenLayer, weights02))

        outputError = referenceOutput - outputPerceptronLayer

        outputDelta = outputError * sigmoidSlope(outputPerceptronLayer)
        meanValue = np.mean(np.abs(outputError))
        y.append(meanValue)

        hiddenLayerError = outputDelta.dot(weights02.T)
        hiddenLayerDelta = hiddenLayerError * sigmoidSlope(hiddenLayer)

        weights02 += hiddenLayer.T.dot(outputDelta)
        weights01 += inputData.T.dot(hiddenLayerDelta)
    x = [i for i in range(trainingNumber)]
    return plt.plot(x, y)


def SingleNerualNetwork01():
    y = []
    #Same input output reference as multilayernetwork01
    inputData = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
    referenceOutput = [[0], [1], [1], [0]]

    np.random.seed(42)  #set seed to the same number
    weights01 = 2 * np.random.random(
        (3, 1)) - 1  #Only set the random to only a 3x1 matrix

    for i in range(trainingNumber):

        #takes the input array
        inputLayer = inputData
        multiplier = np.dot(inputLayer, weights01)

        slopeChangeFactor = 1
        #get the miltiplied value of slope change factor and the multiplier
        outputPerceptronLayer = sigmoid(slopeChangeFactor * multiplier)

        roundedValue = np.round(
            outputPerceptronLayer,
            decimals=2)  #round the outputperception to two decimal places
        #This will be the difference between the output preception and the reference output
        outputError = referenceOutput - outputPerceptronLayer

        meanValue = np.mean(np.abs(outputError))  #again take mean
        y.append(meanValue)  #set mean to y axis
        outputDelta = outputError * slopeChangeFactor * (
            sigmoidSlope(outputPerceptronLayer))

        weights01 += np.dot(inputLayer.T, outputDelta)
        #same to sext x axis value for the graph
    x = [i for i in range(trainingNumber)]
    return plt.plot(x, y)


def SingleNerualNetwork02():
    y = []
    inputData = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
    referenceOutput = np.array([[0], [0], [1], [1]])

    np.random.seed(42)
    weights01 = 2 * np.random.random((3, 1)) - 1

    for i in range(trainingNumber):

        inputLayer = inputData
        multiplier = np.dot(inputLayer, weights01)

        slopeChangeFactor = 1
        outputPerceptronLayer = sigmoid(slopeChangeFactor * multiplier)

        roundedValue = np.round(outputPerceptronLayer, decimals=2)

        outputError = referenceOutput - outputPerceptronLayer

        meanValue = np.mean(np.abs(outputError))
        y.append(meanValue)
        outputDelta = outputError * slopeChangeFactor * (
            sigmoidSlope(outputPerceptronLayer))

        weights01 += np.dot(inputLayer.T, outputDelta)
    x = [i for i in range(trainingNumber)]
    return plt.plot(x, y)


"""
Finally set lines to the functions they need to represent
plot the lengend with specified values
last set the labels for x, y axis
"""
line1, = multilayerNeuralNetwork01()
line2, = SingleNerualNetwork01()
line3, = multilayerNeuralNetwork02()
line4, = SingleNerualNetwork02()
plt.legend([line1, line2, line3, line4], [
    "Multilayer:[0,1,1,0]", "SingleLayer:[0,1,1,0]", "Multilayer:[0,0,1,1]",
    "Singlelayer:[0,0,1,1]"
])
plt.xlabel("Training Number")
plt.ylabel("Error Mean")
plt.show()
