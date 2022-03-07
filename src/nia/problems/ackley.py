import numpy as np

def ackley(X):
    x = X[0]
    y = X[1]
    return -20 * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2))) - np.exp(0.5 *
        (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y))) + np.e + 20
