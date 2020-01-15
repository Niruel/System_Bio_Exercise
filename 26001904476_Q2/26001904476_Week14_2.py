"""
Created By: Nicholas Ruppel
System Biology Exercise Practice
Week 14 Exercise
AIS(Artificail Immune System) exercise
20/01/15
"""
import random
import string
import numpy as np
# open the named AIS dieases
with open("AISdisease_4.txt", "r") as loadDiseases:
    listOfDiseases = loadDiseases.read().split("\n")
# open the file named AISmeroryCell
with open("AISmemoryCell.txt", "r") as loadMemoryCell:
    memoryCell = loadMemoryCell.read().split("\n")

with open("AISvaccines.txt", "r") as loadVaccines:
    listOfVaccines = loadVaccines.read().split("\n")
"""
Set gloabaly acessed variables
"""

antigen = random.choice(listOfDiseases)
antigenLength = len(antigen)
antibodyNumber = 200
generations = 500
mutationChance = 10
selectPenalty = 2
memoryCellFraction = 10
extraCells = len(memoryCell) + len(listOfVaccines) - 20
# make sure extra cells is greater then zero and then pop the front 5 of memorycell to replace with vaccine
if extraCells > 0:
    for i in range(extraCells):
        memoryCell.pop(0)
for vaccine in listOfVaccines:
    memoryCell.insert(0, vaccine)


# return a random string
def randomGene():
    return random.choice(string.printable)


# set the initial population of antibodes and return the list
def intialAntibodyPopulation():
    initPop = []
    for i in range(antibodyNumber):
        initPop.append(''.join(
            random.choice(string.printable) for i in range(antigenLength)))
    return initPop


# This is where i set the penalty from the last lesson and made the fittness apply here
def affintyPenaltyMetric(antiBodyAttack):
    fitness = 0
    for i in range(antigenLength):
        temp = (ord(antiBodyAttack[i]) - ord(antigen[i]))**2
        fitness += temp

    return fitness


# weight the probabilty on a scale of 1
def weightedAntibodyChoice(listOfAntibodyAffinity):
    probs = [
        listOfAntibodyAffinity[i][1]
        for i in range(len(listOfAntibodyAffinity))
    ]
    probs = np.array(probs)
    probs /= probs.sum()
    return listOfAntibodyAffinity[np.random.choice(len(listOfAntibodyAffinity),
                                                   1,
                                                   p=probs)[0]][0]


# mutate the strings from the list of the text file
def mutaion(antibodyMutate, mutationRatio):
    mutatedDNA = ""
    for gene in range(antigenLength):
        mutationCheck = random.randint(0, mutationRatio)
        if mutationCheck == 1:
            mutatedDNA += randomGene()
        else:
            mutatedDNA += antibodyMutate[gene]
    return mutatedDNA


currentAntibodyPopulation = intialAntibodyPopulation()
# Devise a way so that memory cell is memoryCellFraction-times smaller
for ik in memoryCell:

    if len(ik) == len(currentAntibodyPopulation[memoryCell.index(ik)]):
        currentAntibodyPopulation[memoryCell.index(ik)] = ik
# This for loop adds the pentaly
for i in range(generations):
    lastAffinityArray = []
    for k in currentAntibodyPopulation:
        lastAffinityArray.append(affintyPenaltyMetric(k))
    # Consolse print of the list of itterations and penalty
    print(
        "The antibody closest to the antigen at itteration:", i, "is--",
        currentAntibodyPopulation[lastAffinityArray.index(
            min(lastAffinityArray))], "---with penalty of:",
        min(lastAffinityArray))

    populationWeighted = []
    # added a individual counter  with the penelty
    for individul in currentAntibodyPopulation:
        individualPenalty = affintyPenaltyMetric(individul)
        if individualPenalty == 0:
            antibodyFitnessPair = (individul, 1.0)
        else:
            antibodyFitnessPair = (individul, 1.0 / individualPenalty)
        populationWeighted.append(antibodyFitnessPair)

    currentAntibodyPopulation = []
    # check the members of antibody number divide by 2 and mutate.
    for m in range(int(antibodyNumber / 2)):
        bestAntibody1 = weightedAntibodyChoice(populationWeighted)
        bestAntibody2 = weightedAntibodyChoice(populationWeighted)

        bestAntibody1 = mutaion(bestAntibody1, mutationChance)
        bestAntibody2 = mutaion(bestAntibody2, mutationChance)

        currentAntibodyPopulation.append(bestAntibody1)
        currentAntibodyPopulation.append(bestAntibody2)

lastAffinityArray = []
# append the current antibody to the lastaffinity matrix
for g in currentAntibodyPopulation:
    lastAffinityArray.append(affintyPenaltyMetric(g))


with open("AISmemoryCell.txt", "r") as loadMemoryCell:
    memoryCell = loadMemoryCell.read().split("\n")

if min(lastAffinityArray) < 50:
    putIntoMemory = currentAntibodyPopulation[lastAffinityArray.index(
        min(lastAffinityArray))]
    memoryCellSize = int(antibodyNumber / memoryCellFraction)
    if len(memoryCell) < 20:
        if len(memoryCell) == 1:
            newMemoryCell = putIntoMemory
        newMemoryCell = "\n".join(memoryCell)
    else:
        memoryCell.pop(0)
        newMemoryCell = "\n".join(memoryCell)
    # print the statment of fittest string and add it to new text file
    print("Fittest String ", generations, " is", putIntoMemory)
    newMemoryCell += "\n" + putIntoMemory
    with open("AISmemoryCell.txt", "w") as writeMemoryCell:
        writeMemoryCell.write(newMemoryCell)
else:
    putIntoMemory = ""
    print("No antibody to put into memory"
          )  # if the list is empty return 0 results

del memoryCell
del listOfDiseases
print(antigen)
