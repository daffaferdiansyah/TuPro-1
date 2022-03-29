import math
import random

def generateChromosome():
    #membuat desain kromosom dengan panjang 6 dan tipe data integer
    chromosome = []
    for _ in range(6):
        chromosome.append(random.randint(0, 9))

    return chromosome

def decodeX(chromosome):
    #mendekode nilai x
    bot, top = (-5, 5) #-5 <= x <= 5

    return bot + ((top - bot)/(9 * 10**(-1) + 9 * 10**(-2)+ 9 * 10**(-3))) * (chromosome[0] * 10 ** (-1) + chromosome[1] * 10 ** (-2) + chromosome[2] * 10 ** (-3))

def decodeY(chromosome):
    #mendekode nilai y
    bot, top = (-5, 5) #-5 <= y <= 5

    return bot + ((top - bot)/(9 * 10**(-1) + 9 * 10**(-2)+ 9 * 10**(-3))) * (chromosome[0] * 10 ** (-1) + chromosome[1] * 10 ** (-2) + chromosome[2] * 10 ** (-3))

def fitnessFunction(chromosome):
    #menghitung nilai fitness
    x = decodeX(chromosome)
    y = decodeY(chromosome)

    return ((math.cos(x)+math.sin(y))**2) / (x**2 + y**2)

def generatePopulation(pop_size):
    #membuat populasi
    population = []
    for i in range(pop_size):
        chromosome = generateChromosome()
        population.append(chromosome)

    return population

def calculateFitness(population):
    fitness = []
    for i in range(len(population)):
        fitness_temp = fitnessFunction(population[i])
        fitness.append(fitness_temp)
        print(fitness[i])
    return fitness

def fitnessSort(population):
    fitness = calculateFitness(population)
    pas = 1
    while pas < len(population):
        idx = pas - 1
        i = pas
        while i < len(population):
            if fitness[idx] > fitness[i]:
                idx = i
            i += 1
        temp = population[pas-1]
        temp_fit = fitness[pas-1]
        population[pas-1] = population[idx]
        fitness[pas-1] = fitness[idx]
        population[idx] = temp
        fitness[idx] = temp_fit
        pas += 1

    return population

def tournamentSelection(population):
    

   
        

pop = generatePopulation(10)

print(pop)
fitnessSort(pop)
print(pop)





