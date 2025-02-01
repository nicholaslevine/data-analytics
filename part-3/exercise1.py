import numpy as np
def column_comparison(array):
    correct = array[:, 1] > array[:,-2]
    return array[correct]

x = np.array([[8, 9, 3, 8, 8],
 [0, 5, 3, 9, 9],
 [5, 7, 6, 0, 4],
 [7, 8, 1, 6, 2],
 [2, 1, 3, 5, 8]])
print(column_comparison(x))