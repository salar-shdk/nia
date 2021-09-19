from .selection import Selection
import numpy as np

class Tournament(Selection):
    @Selection.initializer
    def __init__(self, size=20, replace=False):
        pass

    def select(self, population, fitness):
        indexes = np.random.choice(population.shape[0], self.size, replace=self.replace)
        population = population[indexes]
        fitness = fitness[indexes]
        indexes = fitness.argsort()
        return population[indexes], fitness[indexes]
