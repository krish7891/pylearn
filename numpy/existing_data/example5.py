import numpy as np

list = range(5)
it = iter(list)

a = np.fromiter(it, dtype=float)
print a
