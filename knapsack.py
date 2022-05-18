
import numpy as np
import random

from bitarray import bitarray

class GeneticAlgorithm:

    def __init__(self, inputFile, items, weight, mutationRate, cutoff, initialPopulation, generations):
        self.generations = generations
        self.maxWeight = weight
        self.numberOfItems = items
        self.mutationRate = mutationRate
        self.populationSize = initialPopulation
        self.bestSolutionFound = []
        self.highestFitnessFound = 0

        self.population =[]
        self.pop_fitness = []
        self.items = self.read(inputFile)
        self.initialPopulation()
        # clears output files before running
        open('Average Fitness Data.txt', 'w').close()
        open('Highest Fitness Data.txt', 'w').close()
        open('Best Solution found.txt', 'w').close()

        self.run( generations, cutoff)
        self.best_solution_report()
    def read(self, filename):

        with open(filename) as file:
            data = [tuple(line.split()) for line in file]

        return data

    def generation_report(self, generation_id, population, fitness):
        avg_file = open("Average Fitness Data.txt", "a")
        max_file = open("Highest Fitness Data.txt", "a")
        highest_fitness = max(fitness)
        average_fitness = sum(fitness) / float(len(fitness))
        if highest_fitness > self.highestFitnessFound:
            self.highestFitnessFound = highest_fitness
            index = fitness.index(highest_fitness)

            self.bestSolutionFound = population[index]
        avg_file.write("#{} Average fitness: {}\n".format(generation_id, average_fitness))

        max_file.write("#{} Highest fitness: {}\n".format(generation_id, highest_fitness))

        return average_fitness
    def best_solution_report(self):
        best_file = open("Best Solution found.txt","a")
        utility = 0
        for i in range(self.numberOfItems):
            if self.bestSolutionFound[i] == 1:
                best_file.write("Item#{} Utility:{} Weight:{}\n".format(i, self.items[i][0],self.items[i][1]))
                utility += float(self.items[i][0]);
        best_file.write("\nTotal utility: {}".format(utility))

    def initialPopulation(self):


        for individual in range(self.populationSize):
            chronosome = bitarray(self.numberOfItems)
            chronosome.setall(0)
            for selection in range ( int((1/10)* self.numberOfItems) ):
                i = np.random.randint(0, self.numberOfItems)
                chronosome[i] = True
            self.population.append(chronosome)

        self.fitness()



    def run(self, generations, cutoff_percent):
        average_fitnesses = []
        for gen_id in range(generations):

            parents = self.selection()
            children = self.crossover(parents)
            mutated_children = self.mutate_population(children)
            self.pop_fitness = self.fitness()
            average = self.generation_report(gen_id, mutated_children,  self.pop_fitness)
            average_fitnesses.append(average)
            if (gen_id >= 10):
                average_fitnesses.pop(0)
            if (self.average_across_generations(average_fitnesses) < cutoff_percent and gen_id > 100 ):
                break


    def average_across_generations(self, last_fitnesses):
        difference = np.abs(last_fitnesses[-1] - last_fitnesses[0] )/len(last_fitnesses)

        return difference





    def fitness(self):
        fitness_list = [0] * len(self.population)
        for individual in range(len(self.population)):

            weight = 0
            utility = 0
            for i in range(self.numberOfItems):

                if (self.population[individual][i] == True ):
                    utility += float(self.items[i][0])
                    weight += float(self.items[i][1])
            if (weight > self.maxWeight):
                fitness_list[individual] = 0

            else:
                 fitness_list[individual] = utility

        self.pop_fitness = fitness_list
        return fitness_list






    def mutate_population(self, children):
        for child in children:
            for bit in range(self.numberOfItems):
                r = np.random.random_sample()
                if (r < self.mutationRate):
                    child.invert(bit)

        self.population = children
        return children



    def pair_parents(self, parents):

        #splits list of all parents into sublists of 2
        for i in range(0, len(parents),2):
            yield parents[i:i + 2]
    def crossover(self, parents):

        children = []
        parent_pairs = list(self.pair_parents(parents))


        for pair in parent_pairs:
            crossoverIndex = np.random.randint(0, len(pair[0]))
            child = bitarray(self.numberOfItems)
            child[:crossoverIndex] = pair[0][:crossoverIndex]
            child[crossoverIndex:] = pair[1][crossoverIndex:]

            children.append(child)

        return children


    def selection(self):
        cdf = self.cdf()

        parents = random.choices(self.population, cum_weights=cdf, k=2*len(self.population))
        return parents




    def cdf(self):
        cdf = np.cumsum(self.pdf())
        return cdf
    def pdf(self):

        pdf = [0] * len(self.population)
        sumOfSquares = np.sum(np.square(self.pop_fitness))

        for parent in range(len(self.population)):

            pdf[parent] = np.divide(np.square(self.pop_fitness[parent]) , sumOfSquares)
        return pdf


if __name__ == '__main__':
    print('Starting...')

    print(GeneticAlgorithm("Program2Input.txt", 400, 500, 0.0001, 0.001, 2000, 1000))
    print('Complete')