import numpy as np
def multiplication_table(n):
    rows = np.arange(0, n)
    columns = rows.copy().reshape(n, 1)
    return rows * columns
print(multiplication_table(4))
