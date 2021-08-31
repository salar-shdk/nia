from .. import NiaInterface
import numpy as np
from random import random
from copy import copy

class ParticleSwarmOptimization(NiaInterface):
    @NiaInterface.initializer
    def __init__(self, 
                cost_function,          #fitness function
                iteration_function,     #will be called in each iteration
                lower_bond,             #lower band of parameters
                upper_bond,             #upper band of parameters
                num_agents = 10,        #number of agents
                max_iterations = 100,   #max number of iterations
                num_variable = 1,       #number of parameters to be optimized
                c1 = 0.1,               #cognitive coefficent ,c1>=0
                c2 = 0.1,               #social coefficent    ,c2<=4
                quit_criteria = 0.0001, #acceptable fitness value
                ):
        self.lower_bond = np.array(lower_bond)
        self.upper_bond = np.array(upper_bond)
        self.fitness = np.zeros(shape=(num_agents,1))
        
    class Agent:
        pass

    def generate_agents(self):
        self.agents = []
        for i in range(self.num_agents):
            agent = self.Agent()
            agent.position = np.array([random() for i in range(self.num_variable)]) * (self.upper_bond - self.lower_bond) + self.lower_bond
            agent.fitness  = self.calculate_fitness(agent)
            agent.velocity = 0.0
            agent.personal_best     = agent.fitness
            self.agents.append(agent)

    def calculate_fitness(self,agent):
        return self.cost_function(agent.position)
        
    def log(self):
        print(self.population)
        print(self.fitness)

    def run(self):
        self.generate_agents()
        self.best_agent = copy(self.agents[0])
        for i in range(self.max_iterations) :
            for agent in self.agents:
                fitness = self.calculate_fitness(agent)
                if fitness < agent.fitness:
                    agent.personal_best = agent.position
                agent.fitness = fitness

                if fitness < self.best_agent.fitness:
                    self.best_agent = copy(agent)
                
                agent.velocity = agent.velocity + self.c1 * random() * (agent.personal_best - agent.position) \
                                 + self.c2 * random() * (self.best_agent.position - agent.position)
                agent.position = agent.position + agent.velocity

            self.iteration_function(self)
            if fitness < self.quit_criteria:
                self.message = 'quit criteria reached best answer is: ' + str(self.best_agent.position) + ' and best fitness is: ' + str(self.best_agent.fitness) + ' iteration : ' + str(i);
                return self
        self.message = 'max itteration reached last answer is : ' + str(self.best_agent.position) + ' and best fitness is: ' + str(self.best_agent.fitness);
        return self
        






