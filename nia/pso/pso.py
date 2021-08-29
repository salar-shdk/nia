from .. import NiaInterface
import numpy as np
from random import random

class ParticelSwarmAlgirithm(NiaInterface):
    @NiaInterface.initializer
    def __init__(self, 
                cost_function,
                generation_function,
                num_population,
                num_parents,
                max_generation,
                num_variable,
                lower_bond,
                upper_bond,
                ):
        self.lower_bond = np.array(lower_bond)
        self.upper_bond = np.array(upper_bond)
        self.fitness = np.zeros(shape=(num_population,1))
        print(self.__dict__)

    def generate_population(self, volume):
        return np.random.rand(volume, self.num_variable) * (self.upper_bond - self.lower_bond) + self.lower_bond

    def sort_by_fitness(self):
        for i ,pop in enumerate(self.population):
             self.fitness[i] = self.cost_function(pop)
        new_population = np.append(self.population, self.fitness, axis=1)
        return new_population[new_population[:, -1].argsort()][:,:-1]

        
        
    def log(self):
        print(self.population)
        print(self.fitness)

    def run(self):
        self.population = self.generate_population(self.num_population)
        # self.log()
        self.population = self.calculate_fitness()
        






