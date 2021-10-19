
import numpy as np


class GeneticAlgorithm:

    def __init__(self, inputFile, items, weight, mutationRate, initialPopulation, generations):
        self.generations = generations
        self.maxWeight = weight
        self.numberOfItems = items
        self.mutationRate = mutationRate
        self.populationSize = initialPopulation
        self.items = []
        self.chromosome = []
        self.population =[]
        self.read(inputFile)
        self.initialPopulation()
        self.fitness()

    def initialPopulation(self):
        selections_per_individual = 3
        self.population = [np.random.randint(0, 2,  self.numberOfItems).tolist() for _ in range(self.populationSize)]
        #self.population = np.random.randint(2, size = self.populationSize)

        print('Initial population: \n{}'.format( self.population ))


    def read(self, filename):

        with open(filename) as file:
            data = [tuple(line.split()) for line in file]

        return data

    def selection(self):
        self.chronosome

    def fitness(self):
        # total utility of 400 selections
        fitness = np.zeros(self.numberOfItems)

        # for indv in range(self.populationSize):
        for i in range(self.populationSize):
            fitness[i] = sum(np.multiply(self.items[0], self.population[i]))
            if (fitness[i]  > self.maxWeight):
                fitness[i] = 0


        total_fitness = sum(fitness)
        return total_fitness





    def mutation(self, population):
        return

    def crossover(self, parent1, parent2, crossoverProbability):
        child1 = parent1.copy
        child2 = parent2.copy

        if random() < crossoverProbability:
            print()

        # random crossover point

    def selection(self, fitness):

        for x in range(self.populationSize):
            print()

if __name__ == '__main__':
    print('Starting...')

    print(GeneticAlgorithm("Program2Input.txt", 400, 500, 0.0001, 1000, 5000).read("Program2Input.txt"))