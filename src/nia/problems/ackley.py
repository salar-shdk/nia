import numpy as np

def ackley(x):
    val1 = np.sum(np.square(x))
    val2 = np.sum(np.cos(2 * np.pi * x))
    tmp1 = -0.2 * np.sqrt(val1 / 4)
    tmp2 = val2 / 4

    return -20.0 * np.exp(tmp1) - np.exp(tmp2) + 20.0 + np.exp(1)