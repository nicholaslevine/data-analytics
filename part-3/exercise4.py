import numpy as np
from functools import reduce
def matrix_power(matrix, v : int):
    shape = matrix.shape
    if ((shape[0] == 0 or shape[0] != shape[1]) or v <= 0):
        if (v == -1):
            return np.linalg.inv(matrix)
        return "Invalid arguments"
    if (v == 1):
        return matrix
    result = matrix.copy()
    for _ in range(v - 1):
        result = np.matmul(result, matrix)
    return result

matrix = np.random.randint(0, 10, (10, 10))  
power = 3
print(matrix_power(matrix, power))