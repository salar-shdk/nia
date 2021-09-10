from .. import NiaInterface
from ..crossovers import SBX, RandomSBX
from ..mutations import Uniform
import numpy as np
from random import random

class GeneticAlgorithm(NiaInterface):
    @NiaInterface.initializer
    def __init__(self, 
                cost_function,
                lower_bond,
                upper_bond,
                iteration_function = None,
                num_population = 100,
                num_parents = 20,
                max_iteration = 100,
                num_variable = 1,
                quit_criterion = 0.001,
                crossover = RandomSBX(2),
                mutation = Uniform(0.05)
                ):
        self.lower_bond = np.array(lower_bond)
        self.upper_bond = np.array(upper_bond)

    def generate_population(self, volume):
        return np.random.rand(volume, self.num_variable) * (self.upper_bond - self.lower_bond) + self.lower_bond

    def get_fitness(self, population):
        fitness = np.zeros(shape=(len(population),1))
        for i ,pop in enumerate(population):
            fitness[i] = self.cost_function(pop)
        return fitness

    def sort_by_fitness(self, population, fitness):
        new_population = np.append(population, fitness, axis=1)
        new_population = new_population[new_population[:, -1].argsort()]
        return new_population[:,:-1], new_population[:,-1:]

    def run(self):
        self.population = self.generate_population(self.num_population)
        self.fitness = self.get_fitness(self.population)
        self.population, self.fitness = self.sort_by_fitness(self.population, self.fitness)
        for self.iteration in range(self.max_iteration):
            children = self.crossover.generate(self.population[:self.num_parents], self.num_parents)
            children = self.mutation.mutate(children, self.generate_population(self.num_parents))
            children_fittness = self.get_fitness(children)            
            self.population , self.fitness = self.sort_by_fitness(
                np.concatenate((self.population, children), axis=0),
                np.concatenate((self.fitness, children_fittness), axis=0)
            )
            self.population = self.population[:self.num_population]
            self.fitness = self.fitness[:self.num_population]
            self.best = (self.population[0], self.fitness[0])
            if self.iteration_function:
                self.iteration_function(self)
            if self.fitness[0][0] < self.quit_criterion:
                break
        return self.best
        