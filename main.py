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

def fitness(chromosome):
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
    for i in range(len(population)):
        fitness_temp = fitness(population[i])
        population[i].append(fitness_temp)
    return population

def fitnessSort(population):
    step = 1
    while step < len(population):
        

pop = generatePopulation(10)
calculateFitness(pop)
print(pop)
fitnessSort(pop)
print(pop)





