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

def objectiveFunction(chromosome):
    #menghitung nilai objektif, yaitu hasil perhitungan
    x = decodeX(chromosome)
    y = decodeY(chromosome)

    return (math.cos(x)+math.sin(y))**2 / (x**2 + y**2)

def fitnessFunction(chromosome):
    #menghitung nilai fitness
    x = decodeX(chromosome)
    y = decodeY(chromosome)
    #
    return 1/(0.0001+((math.cos(x)+math.sin(y))**2) / (x**2 + y**2))

def generatePopulation(pop_size):
    #membuat populasi
    population = []
    for i in range(pop_size):
        chromosome = generateChromosome()
        population.append(chromosome)

    return population

def calculateFitness(population):
    #memasukkan nilai fitness ke dalam array
    fitness = []
    for i in range(len(population)):
        fitness_temp = fitnessFunction(population[i])
        fitness.append(fitness_temp)

    return fitness

def fitnessSort(population):
    #mengurutkan kromosom berdasarkan nilai fitnessnya secara descending
    fitness = calculateFitness(population)
    pas = 1
    while pas < len(population):
        idx = pas - 1
        i = pas
        while i < len(population):
            if fitness[idx] < fitness[i]: #perbandingan
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
    #mengambil elitisme
    elitism = []
    for i in range(30):
        elitism.append(population[i])

    return elitism

def parentSelection(population):
    #mengambil parent
    parent = []
    for i in range(20, 90):
        parent.append(population[i])
    
    return parent

def matingPool(parent):
    #parent dijadikan berpasangan secara acak
    pasangan = []
    for i in range(len(parent)//2):
        pasangan_temp = []
        p1 = 0
        p2 = random.randint(1, (len(parent)-1))
        pasangan_temp.append(parent[p1])
        pasangan_temp.append(parent[p2])
        pasangan.append(pasangan_temp)
        parent.pop(p2); parent.pop(p1)

    return pasangan

def crossover(p1, p2, pc):
    #melakukan crossover
    r = random.uniform(0, 1)
    c1 = []; c2 = []
    if r < pc:
        t = random.randint(1, 4)
        c1 = p1[:t] + p2[t:]
        c2 = p2[:t] + p1[t:]
    else:
        c1 = p1
        c2 = p2

    return [c1, c2]

def mutation(child, pm):
    #melakukan mutasi
    r = random.uniform(0, 1)
    r1 = random.randint(0, 5)
    r2 = random.randint(0, 5)
    if r < pm:
        child[0][r1] = random.randint(0, 9)
        child[1][r2] = random.randint(0, 9)

    return child

def generationalReplacement(pop_size, pc, pm, generation):
    #melaukan seleksi survivor dengan metode generational replacement
    popu = generatePopulation(pop_size)
    pembagi = generation // 4
    for i in range(generation):
        fitnessSort(popu)
        newPopu = getElitism(popu)
        parent = parentSelection(popu)
        pasangan = matingPool(parent)
        for j in range(len(pasangan)):
            offspring = crossover(pasangan[j][0], pasangan[j][1], pc)
            offspring = mutation(offspring, pm)
            newPopu.append(offspring[0])
            newPopu.append(offspring[1])
        popu = newPopu
        if (i+1) % pembagi == 0 or i == 0:
            printHasil(popu[0], i+1)

def printHasil(best_chrom, i):
    #mencetak hasil kromosom terbaik
    best_fitness = fitnessFunction(best_chrom)
    nilaiX = decodeX(best_chrom)
    nilaiY = decodeY(best_chrom)
    nilaiFungsi = objectiveFunction(best_chrom)
    print("=============================================================")
    print("--------------------HASIL GENETIC ALGORITHM------------------\n")
    print("Generasi ke \t\t:", i)
    print("Jumlah populasi \t:", pop_size)
    print("Kromosom terbaik\t:",best_chrom)
    print("Nilai x \t\t:", nilaiX)
    print("Nilai y \t\t:", nilaiY)
    print("Nilai fitness terbaik\t: {}".format(best_fitness))
    print("Hasil fungsi objektif \t: {:.20f}".format(nilaiFungsi))
    
pop_size = 100; pc = 0.75; pm = 0.04; generation = 100 # inisialiasi beberapa nilai yang digunakan
generationalReplacement(pop_size, pc, pm, generation)

# -------------------------------------------------------------
# --------------------HASIL GENETIC ALGORITHM------------------

# Generasi ke             : 1
# Jumlah populasi         : 100
# Kromosom terbaik        : [4, 9, 1, 9, 7, 2]
# Nilai x                 : -0.08508508508508505
# Nilai y                 : 4.72972972972973
# Nilai fitness terbaik   : 9946.565816179831
# Hasil fungsi objektif   : 0.00000053721238875481
# -------------------------------------------------------------
# --------------------HASIL GENETIC ALGORITHM------------------

# Generasi ke             : 25
# Jumlah populasi         : 100
# Kromosom terbaik        : [8, 8, 8, 7, 3, 1]
# Nilai x                 : 3.8888888888888893
# Nilai y                 : 2.3173173173173183
# Nilai fitness terbaik   : 9998.646613530507
# Hasil fungsi objektif   : 0.00000001353569659779
# -------------------------------------------------------------
# --------------------HASIL GENETIC ALGORITHM------------------

# Generasi ke             : 50
# Jumlah populasi         : 100
# Kromosom terbaik        : [2, 0, 6, 0, 4, 9]
# Nilai x                 : -2.937937937937938
# Nilai y                 : -4.50950950950951
# Nilai fitness terbaik   : 9999.915450172239
# Hasil fungsi objektif   : 0.00000000084550542635
# -------------------------------------------------------------
# --------------------HASIL GENETIC ALGORITHM------------------

# Generasi ke             : 75
# Jumlah populasi         : 100
# Kromosom terbaik        : [1, 8, 5, 0, 2, 9]
# Nilai x                 : -3.148148148148148
# Nilai y                 : -4.70970970970971
# Nilai fitness terbaik   : 9999.999001826034
# Hasil fungsi objektif   : 0.00000000000998174066
# -------------------------------------------------------------
# --------------------HASIL GENETIC ALGORITHM------------------

# Generasi ke             : 100
# Jumlah populasi         : 100
# Kromosom terbaik        : [1, 8, 5, 0, 2, 9]
# Nilai x                 : -3.148148148148148
# Nilai y                 : -4.70970970970971
# Nilai fitness terbaik   : 9999.999001826034
# Hasil fungsi objektif   : 0.00000000000998174066
