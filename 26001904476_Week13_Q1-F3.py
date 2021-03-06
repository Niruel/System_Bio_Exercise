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


#create the g(x) function from the documentation
def errorFunction(x):
    return sum([(15 * math.sin(x[i] / 5)**2) * (75 * math.cos(x[i] / 13)) *
                (3 * math.sin(x[i] / 7)) + (x[i]**2) + 300
                for i in range(len(x))])


#Create the class for indivual particles
class individualParticle:
    def __init__(self, x0):
        #This is the constructor where varibles are created for use in the class
        self.individualPostion = []
        self.individualVelocity = []
        self.individualBestPostion = []
        self.individualBestError = -1
        self.individualError = -1

        ###Exercise
        #Here we set the inital postion and velocity
        for i in range(0, numStartingLocation):
            self.individualVelocity.append(random.uniform(-1, 1))
            self.individualPostion.append(x0[i])

    #This function is evaluating the postion of the particle and its errors
    def evaluate(self, costFunction):
        self.individualError = costFunction(self.individualPostion)

        if self.individualError < self.individualBestError or self.individualBestError == -1:
            self.individualBestPostion = self.individualPostion
            self.individualBestError = self.individualError
    #Here we update the velocity of the particle
    def update_velocity(self, groupBestPosition):
        w = 0.5
        c1 = 1
        c2 = 2

        for i in range(0, numStartingLocation):
            r1 = random.random()
            r2 = random.random()

            cognitiveVelocity = c1 * r1 * (self.individualBestPostion[i] -
                                           self.individualPostion[i])
            socialVelocity = c2 * r2 * (groupBestPosition[i] -
                                        self.individualPostion[i])
            #Here we want to add 3.5 to the value of individual velocity which
            #adds to the wieght value to equal 4.0 as extra add push needed.
            self.individualVelocity[i] = w * self.individualVelocity[
                i] + cognitiveVelocity + socialVelocity +3.5
    #This fuction is used to update the postion of the particle with the updated velocity
    def positionUpdate(self, bounds):
        for i in range(0, numStartingLocation):
            self.individualPostion[
                i] = self.individualPostion[i] + self.individualVelocity[i]
            if self.individualPostion[i] > bounds[i][1]:
                self.individualPostion[i] = bounds[i][1]
            if self.individualPostion[i] < bounds[i][0]:
                self.individualPostion[i] = bounds[i][0]


#Outside the class now we update and optimize the swarm
def particleSwarmOptimization(costFunction, x0, bounds, num_particles,
                              maxiter):
    global numStartingLocation
    numStartingLocation = len(x0)
    bestGroupError = -1
    groupsBestPosition = []
    swarm = []

    for i in range(0, num_particles):
        swarm.append(individualParticle(x0))

    for i in range(0, maxiter):

        for j in range(0, num_particles):
            swarm[j].evaluate(costFunction)

            if swarm[
                    j].individualError < bestGroupError or bestGroupError == -1:
                groupsBestPosition = list(swarm[j].individualPostion)
                bestGroupError = float(swarm[j].individualError)

        for j in range(0, num_particles):
            swarm[j].update_velocity(groupsBestPosition)
            swarm[j].positionUpdate(bounds)
    print(
        'After running the swarm of computer agents, the group\'s best position is'
        + str(groupsBestPosition) + " with an error of " + str(bestGroupError))

#Set the x,y minimum for each swarm to move
initialStartingPosition = [-15, 15]
minMaxBounds = [(-100, 100), (-2500, 11000)]
particleSwarmOptimization(errorFunction,
                          initialStartingPosition,
                          minMaxBounds,
                          num_particles=150,
                          maxiter=30)

#Exercise 4: The problem is around the min/max perameraters set at the buttom here
#after graphing the function the min max has to be increased to -2500 and 11000 to get the particles
#to move off the 15 line mark.