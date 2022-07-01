import numpy as np

def griewank(x):
    indices = np.arange(1, len(x) + 1)

    return np.sum(x * x / 4000.0) \
        - np.product(np.cos(x / np.sqrt(indices))) \
        + 1.0