"""
Created By: Nicholas Ruppel
System Biology Exercise Practice
Week 11 Exercise
Neuroal Network
2019/12/12
"""
import numpy as np
import matplotlib.pyplot as plt

trainingNumber = 900


def sigmoid(x):

    return 1 / (1 + np.exp(-x))


def sigmoidSlope(x):
    return x * (1 - x)


def multilayerNeuralNetwork01():
    y = []
    inputData = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
    referenceOutput = [[0], [1], [1], [0]]

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


def multilayerNeuralNetwork02():
    y = []
    inputData = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
    referenceOutput = np.array([[0], [0], [1], [1]])

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
    inputData = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
    referenceOutput = [[0], [1], [1], [0]]

    np.random.seed(42)
    weights01 = 2 * np.random.random((3, 1)) - 1

    for i in range(trainingNumber):

        #takes the input array
        inputLayer = inputData
        multiplier = np.dot(inputLayer, weights01)

        #take sigmoid and do some math to satisfy the function
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
