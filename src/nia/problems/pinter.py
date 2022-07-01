import numpy as np

def pinter(x):
    sub = np.roll(x, 1)
    add = np.roll(x, -1)
    indices = np.arange(1, len(x) + 1)
    a = sub * np.sin(x) + np.sin(add)
    b = (sub * sub) - 2.0 * x + 3.0 * add - np.cos(x) + 1.0
    return np.sum(indices * (x * x)) \
           + np.sum(20.0 * indices * np.power(np.sin(a), 2.0)) \
           + np.sum(indices * np.log10(1.0 + indices * np.power(b, 2.0)))