import numpy as np

def powel(x):
    x1 = x[range(0, len(x) - 3, 4)]
    x2 = x[range(1, len(x) - 2, 4)]
    x3 = x[range(2, len(x) - 1, 4)]
    x4 = x[range(3, len(x) , 4)]

    return np.sum((x1 + 10 * x2) ** 2.0
                  + 5 * (x3 - x4) ** 2.0
                  + (x2 - 2 * x3) ** 4.0
                  + 10 * (x1 - x4) ** 4.0)