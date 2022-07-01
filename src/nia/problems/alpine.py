import numpy as np

def alpine(x):
    return np.sum(np.abs(np.multiply(x, np.sin(x)) + 0.1 * x))