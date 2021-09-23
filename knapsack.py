import random

class GeneticAlgorithm:

    def __init__(self, size, max, mutationRate):
        self.maxWeight = max
        self.populationSize = size
        self.mutationRate = mutationRate



    def read(self, filename):
        list = []
        for line in open(filename).read().split():



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



        #random crossover point


    def selection(self, fitness ):

        for x in range(self.populationSize, ):


if __name__ == '__main__':
    print('Starting...')
    GeneticAlgorithm().run();
()


