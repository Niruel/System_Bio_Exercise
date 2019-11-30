"""
Created By: Nicholas Ruppel
System Biology Exercise Practice
Week 10 Exercise
Genetic Algorithm Fitness Function Creation
2019/11/30
"""
import random
import string
import numpy as np

target = "Nicholas"
dnaLen= len(target)
populationSize = 20
generations =50000
mutationChance = 100

"""

"""
def randomGene():
    return random.choice(string.printable)
"""

"""
def initPopulation():
    initPop = [] #create the list to be returned
    for i in range(populationSize): #Check population size
        initPop.append(''.join(random.choice(string.printable)for i in range(dnaLen)))
    return initPop
"""

"""
def fitnessFunc1(competingDNA):
    fitness = 0
    
    for i in range(dnaLen):
        temp = abs(ord(competingDNA[i])-ord(target[i]))
        fitness +=temp
    return fitness
"""

"""
def fitnessFunc2(competingDNA):
    fitness = 0
    for i in range(dnaLen):
        temp = (ord(competingDNA[i]) - ord(target[i]))**2
        fitness +=temp

    return fitness
"""

"""
def fitnessFunc3(competingDNA):
    fitness = 0
    competingDNA_List = [ord(c) for c in competingDNA]
    DNATarget_List = [ord(t) for t in target]
    for i in range(dnaLen):
           if competingDNA_List[i] != DNATarget_List[i]:
               fitness+=1

    return fitness
"""

"""
def fitnessFunc(competingDNA):
    return fitnessFunc3(competingDNA)

"""

"""
def mutation(competingDNA, mutationChance):
    mutatedDNA = ""
    rand = random.randint(1, mutationChance)
    if rand == 1:
        mutantGene = randomGene()   
        geneNum = random.randint(0, dnaLen - 1)
        
        DNAlist = list(competingDNA)
        DNAlist[geneNum] = mutantGene
        mutatedDNA = ''.join(DNAlist)
    else:
        mutatedDNA = competingDNA
    return mutatedDNA

"""

"""
def recombination(competingDNA_1,competingDNA_2):
    crossOverPoint = random.randint(0, dnaLen - 1)
    DNAout_1 = competingDNA_1[:crossOverPoint] + competingDNA_2[crossOverPoint:]
    DNAout_2 = competingDNA_2[:crossOverPoint] + competingDNA_1[crossOverPoint:]
    return (DNAout_1, DNAout_2)
"""

"""
def weightedDNAchoice(competingDNAfitnessPairs):
    probs = [competingDNAfitnessPairs[i][1] for i in range(len(competingDNAfitnessPairs))]
    probs = np.array(probs)
    probs /= probs.sum()
    return competingDNAfitnessPairs[np.random.choice(len(competingDNAfitnessPairs),1,p = probs)[0]][0]

"""

"""
currentpop = initPopulation()
for i in range(generations):
    lastfitnessarray = []
    for k in currentpop:
        #Change fitnessfunc to which function you want 1, 2, 3
        lastfitnessarray.append(fitnessFunc(k))

    print("The last fittest DNA", i , "is---", currentpop[lastfitnessarray.index(min(lastfitnessarray))],
            "--- With penalty", min(lastfitnessarray))

    populationWeighted = []
    for individuals in currentpop:
        
        individualsPenalty = fitnessFunc(individuals)
        if individualsPenalty == 0:
            DNAFitnessPair = (individuals, 1.0)
        else:
            DNAFitnessPair= (individuals,1.0/individualsPenalty)
        populationWeighted.append(DNAFitnessPair)

    currentpop=[]
    for m in range(int(populationSize/2)):
        fitnessDNA_1 = weightedDNAchoice(populationWeighted)
        fitnessDNA_2 = weightedDNAchoice(populationWeighted)

        fitnessDNA_1,fitnessDNA_2 =recombination(fitnessDNA_1,fitnessDNA_2)


        fitnessDNA_1=mutation(fitnessDNA_1,mutationChance)
        fitnessDNA_2=mutation(fitnessDNA_2,mutationChance)

        currentpop.append(fitnessDNA_1)
        currentpop.append(fitnessDNA_2)

lastfitnessarray = []
for g in currentpop:
    #Change fitnessfunc to which function you want 1, 2, 3
    lastfitnessarray.append(fitnessFunc(g))

print("fitesst string at: ", generations, " is", currentpop[lastfitnessarray.index(min(lastfitnessarray))])