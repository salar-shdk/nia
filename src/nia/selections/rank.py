from .selection import Selection
import numpy as np

class Rank(Selection):
    @Selection.initializer
    def __init__(self, size=20):
        pass

    def select(self, population, fitness):
        indexes = fitness.argsort()
        return (population[indexes])[:self.size], (fitness[indexes])[:self.size]
