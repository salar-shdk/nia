import numpy as np

def dixon_price(x):
    indices = np.arange(2, len(x)+1)

    return (x[0] - 1) ** 2 + np.sum(indices * (2 * x[1:] ** 2 - x[0: -1]) ** 2)