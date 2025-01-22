import numpy as np
import math

def reverse(a):
    arr = np.eye(a)
    mp = math.ceil(a / 2)
    for row in range(mp):
        stored = arr[row].copy()
        arr[row] = arr[-1-row]
        arr[-1-row] = stored
    return arr



def diamond(x : int):
    if (x < 2):
        return "Please choose a larger number"
    bottom_left = np.eye(x)
    top_right = bottom_left.copy()
    top_left = reverse(x)
    bottom_right = top_left.copy()
    if (x % 2 != 0):
        top_right = top_right[:, 1:]
        bottom_right = bottom_right[:, 1:]
    top = np.concatenate((top_left, top_right), axis = 1)
    if (x % 2 != 0):
        top = top[:x-1, :]
    bottom = np.concatenate((bottom_left, bottom_right), axis = 1)
    full = np.concatenate((top, bottom))
    print(full)

diamond(5)

