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
                num_particles = 10,        #number of particles
                max_iterations = 100,   #max number of iterations
                num_variable = 1,       #number of parameters to be optimized
                c1 = 0.1,               #cognitive coefficent ,c1>=0
                c2 = 0.1,               #social coefficent    ,c2<=4
                quit_criteria = 0.0001, #acceptable fitness value
                ):
        self.lower_bond = np.array(lower_bond)
        self.upper_bond = np.array(upper_bond)
        self.fitness = np.zeros(shape=(num_particles,1))
        
    class Particle:
        pass

    def generate_particles(self):
        self.particles = []
        for i in range(self.num_particles):
            particle = self.Particle()
            particle.position = np.array([random() for i in range(self.num_variable)]) * (self.upper_bond - self.lower_bond) + self.lower_bond
            particle.fitness  = self.calculate_fitness(particle)
            particle.velocity = 0.0
            particle.personal_best     = particle.fitness
            self.particles.append(particle)

    def calculate_fitness(self,particle):
        return self.cost_function(particle.position)
        
    def log(self):
        print(self.population)
        print(self.fitness)

    def run(self):
        self.generate_particles()
        self.best_particle = copy(self.particles[0])
        for i in range(self.max_iterations) :
            for particle in self.particles:
                fitness = self.calculate_fitness(particle)
                if fitness < particle.fitness:
                    particle.personal_best = particle.position
                particle.fitness = fitness

                if fitness < self.best_particle.fitness:
                    self.best_particle = copy(particle)
                
                particle.velocity = particle.velocity + self.c1 * random() * (particle.personal_best - particle.position) \
                                 + self.c2 * random() * (self.best_particle.position - particle.position)
                particle.position = particle.position + particle.velocity

            self.iteration_function(self)
            if fitness < self.quit_criteria:
                self.message = 'quit criteria reached best answer is: ' + str(self.best_particle.position) + ' and best fitness is: ' + str(self.best_particle.fitness) + ' iteration : ' + str(i);
                return self
        self.message = 'max itteration reached last answer is : ' + str(self.best_particle.position) + ' and best fitness is: ' + str(self.best_particle.fitness);
        return self
        






