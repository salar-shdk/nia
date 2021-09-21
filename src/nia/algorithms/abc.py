from .. import NiaInterface
import numpy as np
import random
from operator import attrgetter

class ArtificialBeeColony(NiaInterface):
    @NiaInterface.initializer
    def __init__(self, 
                cost_function,                 #fitness function
                iteration_function,            #will be called in each iteration
                lower_bond,                    #lower band of parameters
                upper_bond,                    #upper band of parameters
                num_bees = 10,                 #number of bees (food sources)
                max_iterations = 100,          #max number of iterations
                num_variable = 1,              #number of parameters to be optimized
                employed_bees_percentage = 50, #percentage of employed bees ,[0,100]
                quit_trial = 5,                #quit after n trials without any improvement ,n>1
                quit_criteria = 0.0001,        #acceptable fitness value
                ):
        self.lower_bond = np.array(lower_bond)
        self.upper_bond = np.array(upper_bond)
        self.employed_bees = round(num_bees * employed_bees_percentage / 100)
        self.onlooker_bees = num_bees - self.employed_bees

    def generate_food_sources(self):
        self.food_sources = []
        for i in range(self.employed_bees):
            source = self.create_food_source()
            self.food_sources.append(source)

    def employed_bees_stage(self):
        for i in range(self.employed_bees):
            food_source = self.food_sources[i]
            new_solution = self.generate_solution(i)
            best_solution = self.best_solution(food_source.solution, new_solution)
            self.set_solution(food_source, best_solution)

    def onlooker_bees_stage(self):
        for i in range(self.onlooker_bees):
            probabilities = [self.probability(fs) for fs in self.food_sources]
            selected_index = self.selection(range(len(self.food_sources)), probabilities)
            selected_source = self.food_sources[selected_index]
            new_solution = self.generate_solution(selected_index)
            best_solution = self.best_solution(selected_source.solution, new_solution)
            self.set_solution(selected_source, best_solution)

    def scout_bees_stage(self):
        for i in range(self.employed_bees):
            food_source = self.food_sources[i]
            if food_source.trials > self.quit_trial:
                food_source = self.create_food_source()

    def generate_solution(self, current_solution_index):
        solution = self.food_sources[current_solution_index].solution
        k_source_index = self.random_solution_excluding([current_solution_index])
        k_solution = self.food_sources[k_source_index].solution
        d = random.randint(0, len(self.lower_bond) - 1)
        r = random.uniform(-1, 1)
        new_solution = np.copy(solution)
        new_solution[d] = solution[d] + r * (solution[d] - k_solution[d])
        return new_solution

    def random_solution_excluding(self, excluded_index):
        available_indexes = set(range(self.employed_bees))
        exclude_set = set(excluded_index)
        diff = available_indexes - exclude_set
        selected = random.choice(list(diff))
        return selected

    def best_solution(self, current_solution, new_solution):
        if self.fitness(new_solution) < self.fitness(current_solution):
            return new_solution
        else:
            return current_solution

    def probability(self, solution_fitness):
        fitness_sum = sum([fs.fitness for fs in self.food_sources])
        probability = solution_fitness.fitness / fitness_sum
        return probability

    def fitness(self, solution):
        return self.cost_function(solution)

    def selection(self, solutions, weights):
        return random.choices(solutions, weights)[0]

    def set_solution(self, food_source, new_solution):
        if np.array_equal(new_solution, food_source.solution):
            food_source.trials += 1
        else:
            food_source.solution = new_solution
            food_source.fitness  = self.fitness(new_solution)
            food_source.trials = 0

    def best_source(self):
        best = min(self.food_sources, key=attrgetter('fitness'))
        return best

    class FoodSource:
        pass
        
    def create_food_source(self):
        food_source = self.FoodSource()
        food_source.solution = np.array([random.random() for i in range(self.num_variable)]) * (self.upper_bond - self.lower_bond) + self.lower_bond
        food_source.fitness = self.fitness(food_source.solution)
        food_source.trials = 0
        return food_source 

    def run(self):
        self.generate_food_sources()
        for i in range(self.max_iterations) :
            self.employed_bees_stage()
            self.onlooker_bees_stage()
            self.scout_bees_stage()
            fitness = self.best_source().fitness
            if fitness < self.quit_criteria:
                self.message = 'quit criteria reached best answer is: ' + str(self.best_source().solution) + ' and best fitness is: ' + str(self.best_source().fitness) + ' iteration : ' + str(i)
                return self
            self.iteration_function(self)
        self.message = 'max itteration reached last answer is : ' + str(self.best_source().solution) + ' and best fitness is: ' + str(self.best_source().fitness)
        return self
        






