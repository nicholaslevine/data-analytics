import numpy as np
import pandas as pd
import os
import scipy.stats
def load():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "iris.csv")
    return pd.read_csv(path).drop("species", axis = 1).values
def lengths():
    arr = load()
    sepal_length = arr[:, 0]
    sepal_width = arr[:, 2]
    return scipy.stats.pearsonr(sepal_length, sepal_width)[0]

def correlations():
    arr = load()
    return np.corrcoef(arr, rowvar= False)
print(correlations())
print(lengths())
