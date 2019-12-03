"""
Created By: Nicholas Ruppel
System Biology Exercise Practice
Week 10 Exercise
Genetic Algorithm Fitness Function Creation
2019/12/03

Please choose in the FitnessFunc where it returns which fitness function
to run replace the number with 1, 2, or 3
"""
import random
import string
import numpy as np

target = "Nicholas"
dnaLen= len(target)
populationSize = 20
generations =50000
mutationChance = 100
fitnessMode = 1

"""
create random varibles that represent different genes
"""
def randomGene():
    return random.choice(string.printable)
"""
create initial population of size and jion to length of target dna
"""
def initPopulation():
    initPop = [] #create the list to be returned
    for i in range(populationSize): #Check population size
        initPop.append(''.join(random.choice(string.printable)for i in range(dnaLen)))
    return initPop
"""
Takes absolute value of competeing dna strand - target location and and that varible to fitness
"""
def fitnessFunc1(competingDNA):
    fitness = 0
    
    for i in range(dnaLen):
        temp = abs(ord(competingDNA[i])-ord(target[i]))
        fitness +=temp
    return fitness
"""
square competing dna - target dna length and square it at that to fitness
"""
def fitnessFunc2(competingDNA):
    fitness = 0
    for i in range(dnaLen):
        temp = (ord(competingDNA[i]) - ord(target[i]))**2
        fitness +=temp

    return fitness
"""
check weather competeing dna = target dna and if not add one to penalty
"""
def fitnessFunc3(competingDNA):
    fitness = 0
    for i in range(dnaLen):
           if competingDNA[i] != target[i]:
               fitness+=1

    return fitness
"""
choose which fitness function to run
 replace the number with 1, 2, or 3
"""
def fitnessFunc(competingDNA):
    if fitnessMode == 1:
        return fitnessFunc1(competingDNA)
    elif fitnessMode == 2:
        return fitnessFunc2(competingDNA)
    elif fitnessMode == 3:
        return fitnessFunc3(competingDNA)

    

"""
randomly mutate based on given list 
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
recombine each dna with mutated choice
"""
def recombination(competingDNA_1,competingDNA_2):
    crossOverPoint = random.randint(0, dnaLen - 1)
    DNAout_1 = competingDNA_1[:crossOverPoint] + competingDNA_2[crossOverPoint:]
    DNAout_2 = competingDNA_2[:crossOverPoint] + competingDNA_1[crossOverPoint:]
    return (DNAout_1, DNAout_2)
"""
weight the chance by 1/100
"""
def weightedDNAchoice(competingDNAfitnessPairs):
    probs = [competingDNAfitnessPairs[i][1] for i in range(len(competingDNAfitnessPairs))]
    probs = np.array(probs)
    probs /= probs.sum()
    return competingDNAfitnessPairs[np.random.choice(len(competingDNAfitnessPairs),1,p = probs)[0]][0]

"""
check penalty of each potision of population
"""
def Runner():
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


if __name__ == "__main__":
    while True:
        choice = input("Choose 1, 2, or 3 for the fitness function you want to run. ")
        try:
            fitnessMode = int(choice)
            Runner()
        except:
            print("Please choose 1 or 2 or 3")

