import math
import random

def generateChromosome():
    #membuat satu kromosom dengan panjang 6 dan tipe data integer
    chromosome = []
    for _ in range(6):
        chromosome.append(random.randint(0, 9))

    return chromosome

def decodeX(chromosome):
    #mendekode nilai x
    bot, top = (-5, 5)#-5 <= x <= 5

    return bot + ((top - bot)/(9 * 10**(-1) + 9 * 10**(-2)+ 9 * 10**(-3))) * (chromosome[0] * 10 ** (-1) + chromosome[1] * 10 ** (-2) + chromosome[2] * 10 ** (-3))

def decodeY(chromosome):
    #mendekode nilai y
    bot, top = (-5, 5) #-5 <= y <= 5

    return bot + ((top - bot)/(9 * 10**(-1) + 9 * 10**(-2)+ 9 * 10**(-3))) * (chromosome[3] * 10 ** (-1) + chromosome[4] * 10 ** (-2) + chromosome[5] * 10 ** (-3))

def fitnessFunction(chromosome):
    #menghitung nilai fitness
    x = decodeX(chromosome)
    y = decodeY(chromosome)
    #return ((math.cos(x**2)) * (math.sin(y**2))) + (x + y)
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

    return fitness

def fitnessSort(population):
    
    fitness = calculateFitness(population)
    pas = 1
    while pas < len(population):
        idx = pas - 1
        i = pas
        while i < len(population):
            if fitness[idx] < fitness[i]:
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

def getElitism(population):
    elitism = []
    for i in range(30):
        elitism.append(population[i])
    
    #print("ARRAY ELITISM")
    #print(elitism)
    #print("jumlah elitism ", len(elitism),"\n")
    return elitism

def parentSelection(population):
    parent = []
    for i in range(20, 90):
        parent.append(population[i])
    
    #print("ARRAY PARENT")
    #print(parent)
    #print("jumlah parent", len(parent),"\n")
    return parent

def matingPool(parent):
    pasangan = []
    for i in range(len(parent)//2):
        pasangan_temp = []
        p1 = 0
        p2 = random.randint(1, (len(parent)-1))
        pasangan_temp.append(parent[p1])
        pasangan_temp.append(parent[p2])
        pasangan.append(pasangan_temp)
        parent.pop(p2); parent.pop(p1)
    #print("ARRAY PASANGAN\n")
    #print(pasangan)
    #print("Jumlah pasangan", len(pasangan),"\n")
    return pasangan

def crossover(p1, p2, pc):
    r = random.uniform(0, 1)
    c1 = []; c2 = []
    if r < pc:
        t = random.randint(1, 4)
        c1 = p1[:t] + p2[t:]
        c2 = p2[:t] + p1[t:]
    else:
        c1 = p1
        c2 = p2
    #print(c1, c2)
    return [c1, c2]

def mutation(child, pm):
    r = random.uniform(0, 1)
    r1 = random.randint(0, 5)
    r2 = random.randint(0, 5)
    if r < pm:
        child[0][r1] = random.randint(0, 9)
        child[1][r2] = random.randint(0, 9)
    #print(child)
    return child

def generationalReplacement(pop_size, pc, pm, generation):
    popu = generatePopulation(pop_size)
    for i in range(generation):
        fitnessSort(popu)
        newPopu = getElitism(popu)
        parent = parentSelection(popu)
        pasangan = matingPool(parent)
        while len(newPopu) < pop_size:
            for i in range(len(pasangan)):
                offspring = crossover(pasangan[i][0], pasangan[i][1], pc)
                offspring = mutation(offspring, pm)
                newPopu.append(offspring[0])
                newPopu.append(offspring[1])
        popu = newPopu
    return popu

def printHasil():
    pop_size = 100; pc = 0.75; pm = 0.04; generation = 100
    gen = generationalReplacement(pop_size, pc, pm, generation)
    fitnessSort(gen)
    best_chrom = gen[0]
    best_fitness = fitnessFunction(gen[0])
    nilaiX = decodeX(best_chrom)
    nilaiY = decodeY(best_chrom)
    print("-------------------------------------------------------------\n")
    print("Kromosom terbaik\t:",best_chrom)
    print("Nilai fitness terbaik\t: {:.19f}".format(best_fitness))
    print("Nilai x \t\t:", nilaiX)
    print("Nilai y \t\t:", nilaiY)
    print("Jumlah generasi \t:", generation)

printHasil()