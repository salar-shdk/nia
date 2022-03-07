from .. import NiaInterface
import numpy as np
from random import random
from copy import copy

class ParticleSwarmOptimization(NiaInterface):
    @NiaInterface.initializer
    def __init__(self, 
                cost_function,              #fitness function
                lower_bond,                 #lower band of parameters
                upper_bond,                 #upper band of parameters
                iteration_function = None,  #will be called in each iteration
                num_particles = 10,         #number of particles
                max_iterations = 100,       #max number of iterations
                num_variable = 1,           #number of parameters to be optimized
                c1 = 0.1,                   #cognitive coefficent ,c1>=0
                c2 = 0.1,                   #social coefficent    ,c2<=4
                quit_criteria = 0.0001,     #acceptable fitness value
                ):
        self.lower_bond = np.array(lower_bond)
        self.upper_bond = np.array(upper_bond)
        self.fitness = np.zeros(shape=(num_particles,1))


    def get_best(self):
        return {
            'result': self.best_particle.position,
            'fitness': self.best_particle.fitness
            }

    def get_iteration_info(self):
        return {
            'population': self.particles,
            'interation': self.iteration,
            'best': self.get_best(),
        }

    class Particle:
        
        def __init__(self):
            self.position = None
            self.fitness = None
            self.velocity = None
            self.personal_best = None

        def __repr__(self):
            return str(self.__dict__)

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

    def run(self):
        self.generate_particles()
        self.best_particle = copy(self.particles[0])
        for self.iteration in range(self.max_iterations):
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

            super().run_iteration_function()
            if fitness < self.quit_criteria:
                super.finilize(True)
                return self

        super().finilize(False)
        return self
        






