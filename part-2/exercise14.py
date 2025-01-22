import numpy as np
def vector_lengths(arr):
    n = arr.shape[0]
    final_arr = np.zeros(n)
    for i, row in enumerate(arr):
        vector_sum = np.sqrt(np.sum(row ** 2))
        final_arr[i] = vector_sum
    return final_arr