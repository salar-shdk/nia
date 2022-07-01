import numpy as np

def expanded_schaffer(x):
    tmp = x[0] ** 2 + x[1] ** 2
    return np.sum( 0.5 + (np.sin(np.sqrt(tmp)) ** 2 - 0.5) / (1 + 0.001 * tmp) ** 2 )