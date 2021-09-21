from .. import NiaInterface
from ..crossovers import SBX
from ..mutations import Uniform
from ..selections import Rank
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
                max_iteration = 100,
                num_variable = 1,
                quit_criteria = 0.001,
                crossover = SBX(2),
                mutation = Uniform(0.05),
                selection = Rank(20)
                ):
        self.lower_bond = np.array(lower_bond)
        self.upper_bond = np.array(upper_bond)
        if type(num_population) is int:
            self.num_population = np.array([num_population] * max_iteration)

    def generate_population(self, volume):
        return np.random.rand(volume, self.num_variable) * (self.upper_bond - self.lower_bond) + self.lower_bond

    def get_fitness(self, population):
        fitness = np.zeros(shape=(len(population)))
        for i ,pop in enumerate(population):
            fitness[i] = self.cost_function(pop)
        return fitness

    def migrate(self, population, fitness):
        indexes = fitness.argsort()
        return (population[indexes])[:self.num_population[self.iteration]], (fitness[indexes])[:self.num_population[self.iteration]]

    def run(self):
        self.population = self.generate_population(self.num_population[0])
        self.fitness = self.get_fitness(self.population)

        for self.iteration in range(self.max_iteration):
            selected_population, selected_fitness = self.selection.select(self.population, self.fitness)
            children = self.crossover.generate(selected_population)
            children = self.mutation.mutate(children, self.generate_population(children.shape[0]))
            children_fittness = self.get_fitness(children)      
            self.population , self.fitness = self.migrate(
                np.concatenate((self.population, children), axis=0),
                np.concatenate((self.fitness, children_fittness), axis=0)
            )
            self.best = (self.population[0], self.fitness[0])
            if self.iteration_function:
                self.iteration_function(self)
            if self.fitness[0] < self.quit_criteria:
                self.message = 'quit criteria reached best answer is: ' + str(self.best[0]) + ' and best fitness is: ' + str(self.best[1]) + ' iteration : ' + str(self.iteration)
                return self
        self.message = 'max iteration reached best answer so far: ' + str(self.best[0]) + ' with best fitness: ' + str(self.best[1]) + ' iteration : ' + str(self.iteration)
        return self
        