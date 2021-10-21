
import numpy as np
from bitstring import BitStream, BitArray

class GeneticAlgorithm:

    def __init__(self, inputFile, items, weight, mutationRate, initialPopulation, generations):
        self.generations = generations
        self.maxWeight = weight
        self.numberOfItems = items
        self.mutationRate = mutationRate
        self.populationSize = initialPopulation


        self.population =[]
        self.fitness = []
        #self.read(inputFile)
        self.items = self.read(inputFile)
        self.initialPopulation()
        self.selection()


        #self.fitness()

    def initialPopulation(self):
        selections_per_individual = 3
        print(self.numberOfItems)
        for individual in range(self.populationSize):
            #chronosome = np.random.randint(0, 2, self.numberOfItems)
            chronosome = BitStream(self.numberOfItems)
            for selection in range ( int((1/20)* self.numberOfItems) ):
                i = np.random.randint(0, self.numberOfItems)
                chronosome[i] = True
            self.population.append(chronosome)


        #self.population = np.random.randint(2, size = self.populationSize)
        self.fitness2()


        #print('Initial population: {}'.format( self.population.b))


    def run(self, generations):
        for i in range(generations):
            self.fitness2()
            prob




    def read(self, filename):

        with open(filename) as file:
            data = [tuple(line.split()) for line in file]

        return data

    def selection(self):
        self.chronosome

    def update_fitness(self):
        # total utility of 400 selections
        fitness = np.zeros(self.numberOfItems)

        # each individual's weight
        for i in range(len(self.population)):
            fitness[i] = sum(np.multiply(self.items[0], self.population[i]))
            if (fitness[i]  > self.maxWeight):
                fitness[i] = 0


        total_fitness = sum(fitness)
        return total_fitness


    def fitness2(self):
        fitness_list = [0] * len(self.population)
       # weight = []
       # utility = []
        for individual in range(len(self.population)):
            fitness = 0
            weight = 0
            utility = 0
            for i in range(self.numberOfItems):

                if (self.population[individual][i] == True ):
                    utility += float(self.items[i][0])
                    weight += float(self.items[i][1])
            if (weight > self.maxWeight):
                fitness_list[individual] = 0

            else:
                 fitness_list[individual] += utility





                #utility += ( float (self.items[i][0])* self.population[individual] )
                #weight.append(float(self.items[i][1]) * individual[i])
            #if (weight > self.maxWeight):
            #    fitness = 0


           # else: fitness[individual] =

        self.fitness = fitness_list
        #self.print()
    #    print("total weight: " + weight)




    def print(self):
        for indv in range(len(self.population)):
            print("Selections: {} Indv#{} \n fitness:{}".format(self.population[indv].bin, indv, self.fitness[indv]) )
    def mutation(self, population):
        return

    def crossover(self, parent1, parent2, crossoverProbability):
        child1 = parent1.copy
        child2 = parent2.copy

        if random() < crossoverProbability:
            print()

        # random crossover point

    def selection(self):
        estimates = [0] * len(self.population)
        nextGeneration = []
        sumOfSquares = 0
        for i in range(len(self.population)):
            estimates[i] = self.fitness[i] * self.fitness[i]
            sumOfSquares += estimates[i]
        probabilities = [0] * len(self.population)
        for p in range(len(self.population)):
            probabilities[p] = estimates[p] / sumOfSquares



        for i in range(len(self.population)):

        return nextGeneration



if __name__ == '__main__':
    print('Starting...')

    print(GeneticAlgorithm("Program2Input.txt", 400, 500, 0.0001, 100, 5000))