import numpy as np

def cosine_mixture(x):
    return -0.1 * np.sum(np.cos(5 * np.pi * x)) + np.sum(x ** 2) + 0.1*4