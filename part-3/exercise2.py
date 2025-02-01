import numpy as np
import math
def first_half_second_half(arr):
    shape = arr.shape
    m = math.ceil(shape[1]/2)
    print(m)
    print(arr[:, m : ], arr[:, : m])
    filtered_rows = np.sum(arr[:, : m], axis = 1) > np.sum(arr[:, m : ], axis = 1)
    return arr[filtered_rows]
a = np.array([[1, 3, 4, 2],
              [2, 2, 1, 2]])
print(first_half_second_half(a))
