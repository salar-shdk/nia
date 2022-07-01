import numpy as np

def qing(x):
    return np.sum(np.power(x ** 2.0 - np.arange(1, 4 + 1), 2.0))