import numpy as np
def get_rows(two_dimensional_arr : int):
    shape = two_dimensional_arr.shape
    newArr = np.zeros(shape)
    for i in range(shape[1]):
        newArr[i] = two_dimensional_arr[i]
    return f"{newArr}, {two_dimensional_arr}"

def get_columns(two_dimensional_arr: int):
    flipped = two_dimensional_arr.T
    return get_rows(flipped)
a=np.random.randint(0, 10, (4,4))

print(get_rows(a))
print(get_columns(a))