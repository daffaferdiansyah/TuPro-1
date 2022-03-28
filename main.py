import math
import random

def generateChromosome():
    #membuat chromosome kosong
    chromosome = []
    for _ in range(6):
        chromosome.append(random.randint(0, 9))
    return chromosome

def decodeX(chromosome):
    #mendekode nilai x
    bot, top = (-5, 5)
    return bot + ((top - bot)/(9 * 10**(-1) + 9 * 10**(-2)+ 9 * 10**(-3))) * (chromosome[0] * 10 ** (-1) + chromosome[1] * 10 ** (-2) + chromosome[2] * 10 ** (-3))

def decodeY(chromosome):
    bot, top = (-5, 5)
    return bot + ((top - bot)/(9 * 10**(-1) + 9 * 10**(-2)+ 9 * 10**(-3))) * (chromosome[0] * 10 ** (-1) + chromosome[1] * 10 ** (-2) + chromosome[2] * 10 ** (-3))

def fitness(chromosome):
    x = decodeX(chromosome)
    y = decodeY(chromosome)
    return ((math.cos(x)+math.sin(y))**2) / (x**2 + y**2)

def generatePopulation(pop_size):
    population = []
    for i in range(pop_size):
        chromosome = generateChromosome()
        population.append(chromosome)
    return population

print(generatePopulation(10))




