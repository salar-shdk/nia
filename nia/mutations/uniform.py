from .mutation import Mutation
import numpy as np

class Uniform(Mutation):
    @Mutation.initializer
    def __init__(self, rate):
        pass

    def mutate(self, population, random_population):
        random_rates = np.random.rand(len(population), len(population[0])) # check this
        random_population_zeros = np.where(random_rates >= self.rate, 0, 1)
        population_zeros = np.where(random_rates < self.rate, 0, 1)
        random_population = random_population * random_population_zeros
        population = population * population_zeros
        return population + random_population