import random

class GeneticAlgorithm:

    def __init__(self, inputFile, items, weight, mutationRate, initialPopulation):
        self.maxWeight = weight
        self.numberOfItems = items
        self.mutationRate = mutationRate
        self.initialPopulation = initialPopulation
        self.items = []
        self.chromosome = []

        self.read(inputFile)

    def initialPopulation(self):

        population = []
        for x in range(self.initialPopulation):

            population.add()




    def read(self, filename):

        with open(filename) as file:
            data = [tuple(line.split()) for line in file]

        return data


    def selection(self):
        
    def fitness(self):
        # total utility of 400 selections
        for item in self.items:
            if self.chromosome[item] == True:
                total += item.utility

        return total



        total = sum()

    def fitness(self, value, weight):
        if (weight > max):
            return 1
        else:
            return 0
    def mutation(self, population):
        return
    def crossover(self, parent1, parent2, crossoverProbability):
        child1 = parent1.copy
        child2 = parent2.copy

        if random() < crossoverProbability:
            print()



        #random crossover point


    def selection(self, fitness ):

        for x in range(self.populationSize):
            print()



if __name__ == '__main__':
    print('Starting...')
    print( GeneticAlgorithm("Program2Input.txt", 400, 500, 0.0001, 1000).read("Program2Input.txt"))





