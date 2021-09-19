from .crossover import CrossOver
import random
import numpy as np

class RandomSBX(CrossOver):
    @CrossOver.initializer
    def __init__(self, eta=2):
        pass

    def generate(self, population):
        children = []
        for i in range(int(len(population)/2)):
            father1, father2 = random.choices(population, k=2)
            rand = random.random()
            rand = 1 - rand if rand >= 0.5 else rand
            beta = (2 * rand) ** (1 / (1 + self.eta))
            son1 = 0.5 * (1 + beta) * father1 + (1 - beta) * father2
            son2 = 0.5 * (1 - beta) * father1 + (1 + beta) * father2
            children += [son1, son2]
        return np.array(children)