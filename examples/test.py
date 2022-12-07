import sys
sys.path.append('../')

from nia import ParticleSwarmOptimization
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def fit(X):
    x = X[0]
    y = X[1]
    return np.sin(np.sqrt(x**2 + y**2))

#create plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
fits = []
i = 0
def log(pso):
    #clear 
    plt.cla()
    #plot surface
    X = np.arange(-10, 10, 0.5)
    Y = np.arange(-10, 10, 0.5)
    X, Y = np.meshgrid(X, Y)
    Z = np.sin(np.sqrt(X**2 + Y**2))
    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                        linewidth=0, antialiased=False, alpha=0.2)
    # Add a color bar which maps values to colors.
    for particle in pso.particles:
        ax.scatter(particle.position[0], particle.position[1], particle.fitness, marker='o')
    fig.canvas.draw()
    plt.pause(0.001)

lower = np.array([-10,-10])
upper = np.array([10,10])

nia = ParticleSwarmOptimization(cost_function=fit,
                                iteration_function=log,
                                lower_bond=lower,
                                upper_bond=upper,
                                c1=0.1,
                                c2=0.1,
                                num_variable=2,
                                quit_criteria=-0.99999,
                                num_particles = 10,
                                max_iterations=200)
nia.run()
print(nia.message);
