from .crossover import CrossOver
import random
import numpy as np

class KPoint(CrossOver):
    @CrossOver.initializer
    def __init__(self, k=1):
        pass

    def get_shape(self, rands, size):
        result = np.zeros(size)
        rands.append(np.math.inf)
        rands = sorted(rands)
        rand_index = 0
        for i in range(size):
            if i >= rands[rand_index]:
                rand_index += 1
            if rand_index % 2 == 1:
                    result[i] = 1
        return result

    def generate(self, population):
        children = []
        for i in range(int(len(population)/2)):
            father1, father2 = population[i], population[i+1]
            rands = random.sample(range(1, population.shape[1]), k=self.k)
            first_shape = self.get_shape(rands, population.shape[1])
            second_shape = np.where(first_shape == 0, 1, 0)
            children.append(first_shape * father1 + second_shape * father2)
            children.append(first_shape * father2 + second_shape * father1)

        return np.array(children)
