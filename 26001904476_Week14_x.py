import random
import string
import numpy as np

with open("AISdiseases.txt", "r") as loadDiseases:
    listOfDiseases = loadDiseases.read().split(",")

with open("AISmemoryCell.txt", "r") as loadMemoryCell:
    memoryCell = loadMemoryCell.read().split(",")

antigen = randam.choice(listOfDiseases)
antigenLength = len(antigen)
antibodyNumber = 200
generations = 20
mutationChance = 10
selectPenalty = 2
memCellFraction = 10

def randomGene():
    return random.choice(string.printable)

def intialAntibodyPopulation():
    initPop = []
    for i in range(antibodyNumber):
        initPop.append(''.join(random.choice(string.printable)for i in range(antigenLength)))
        return initPop

def affintyPenaltyMetric(antiBodyAttack):

def weightedAntibodyChoice(listOfAntibodyAffinity):
    probs = [listOfAntibodyAffinity[i][1] for i in range(len(listOfAntibodyAffinity))]
    probs = np.array(probs)
    probs /= probs.sum()
    return listOfAntibodyAffinity[np.random.choice(len(listOfAntibodyAffinity), 1, p = probs)[0]][0]
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

for ik in memoryCell:
    if len(ik)== len(currentAntibodyPopulation[memoryCell.index(ik)]):
        currentAntibodyPopulation[memoryCell.index(ik)] = ik

for i in range(generations):
    lastAffinityArray = []

    print("The antibody closest to the antigen at itteration:", i , "is--", 
    currentAntibodyPopulation[lastAffinityArray.index(min(lastAffinityArray))],"---with penalty of:", min(lastAffinityArray))

    populationWeighted = []
    for individul in currentAntibodyPopulation:
        individualPenalty = affintyPenaltyMetric(individul)
        if individualPenalty == 0:
            antibodyFitnessPair = (individul, 1.0)
        else:
            antibodyFitnessPair = (individul, 1.0/individualPenalty)
        populationWeighted.append(antibodyFitnessPair)

    currentAntibodyPopulation = []
    for m in range(int(antibodyNumber/2)):
        bestAntibody1 = weightedAntibodyChoice(populationWeighted)
        bestAntibody2 = weightedAntibodyChoice(populationWeighted)

        bestAntibody1 = mutaion(bestAntibody1, mutationChance)
        bestAntibody2 = mutaion(bestAntibody2, mutationChance)

        currentAntibodyPopulation.append(bestAntibody1)
        currentAntibodyPopulation.append(bestAntibody2)

lastAffinityArray = []
for g in currentAntibodyPopulation:
    lastAffinityArray.append(affintyPenaltyMetric(g))
fileName = "AISmemoryCell.txt"
with open(fileName,"r") as loadMemoryCell:
    newMemoryCell = loadMemoryCell.read()

if min(lastAffinityArray) <50:
    putIntoMemory = currentAntibodyPopulation[lastAffinityArray.index(min(lastAffinityArray))]

    print("Fittest String ", generations, " is", putIntoMemory)
    newMemoryCell += "," + putIntoMemory
    with open(fileName, "w") as writeMemoryCell:
        writeMemoryCell.write(newMemoryCell)
else:
    putIntoMemory = ""
    print("No antibody to put into memory")

del memoryCell
del listOfDiseases
    