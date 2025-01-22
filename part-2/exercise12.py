import numpy as np
def get_row_vectors(arr):
    final_list = []
    for row in arr:
        vector = np.array([row])
        final_list.append(vector)
    return final_list
def get_column_vectors(arr):
    new_arr = arr.T
    return get_row_vectors(new_arr)

m = np.random.random((2, 3))
print(m)
print(get_row_vectors(m))
print(get_column_vectors(m))