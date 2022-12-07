import sys
sys.path.append('..\src')

from nia.algorithms import ArtificialBeeColony
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def ackley(X):
    x = X[0]
    y = X[1]
    return -20*np.exp(-0.2*np.sqrt(0.5*(x**2+y**2)))-np.exp(0.5*(np.cos(2*np.pi*x)+np.cos(2*np.pi*y)))+np.e+20

#create plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
fits = []
i = 0
x = np.arange(-10, 10, 0.5)
y = np.arange(-10, 10, 0.5)
x, y = np.meshgrid(x, y)
z = -20*np.exp(-0.2*np.sqrt(0.5*(x**2+y**2)))-np.exp(0.5*(np.cos(2*np.pi*x)+np.cos(2*np.pi*y)))+np.e+20

def log(abc):
    #clear 
    plt.cla()
    # Plot the surface.
    surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm,
                        linewidth=0, antialiased=False, alpha=0.2)
    # Add a color bar which maps values to colors.
    for food in abc.food_sources:
        ax.scatter(food.solution[0], food.solution[1], food.fitness, marker='o')
    fig.canvas.draw()
    plt.pause(0.001)

lower = np.array([-5,-5])
upper = np.array([5,5])

nia = ArtificialBeeColony(cost_function=ackley,
                                iteration_function=log,
                                lower_bond=lower,
                                upper_bond=upper,
                                quit_criteria = 0.0001,
                                num_variable = 2,
                                )
nia.run()
print(nia.message);
