import numpy as np
def vector_angles(x, y):
    numerator = np.inner(x, y)
    denominator = np.sqrt(np.sum(x**2, axis=2)) * np.sqrt(np.sum(y ** 2, axis = 2))
    #axes go from least shallow to most shallow, starting from 0 
    theta = np.arccos(numerator/denominator)
    return theta.reshape(-1)
x = np.array([[[1, 2, 3]], [[1, 2, 3]], [[4, 5, 6]]])
y = np.array([[[4, 5, 6]], [[7,7, 9]], [[11, 22, 55]]])
print(vector_angles(x, y))

#used numpy.inner() as well, but stuck to the harder method

#numpy broadcasts by first scaling values and then recording them, so you can apply methods to all values in an array without a loop. 
## rules
# 1) All input arrays with ndim smaller than the input array of largest ndim, have 1’s prepended to their shapes.
# 2) The size in each dimension of the output shape is the maximum of all the input sizes in that dimension.
# 3) An input can be used in the calculation if its size in a particular dimension either matches the output size in that dimension, or has value exactly 1.
# 4) If an input has a dimension size of 1 in its shape, the first data entry in that dimension will be used for all calculations along that dimension. In other words, the stepping machinery of the ufunc will simply not step along that dimension (the stride will be 0 for that dimension).
# so this will not work

a=np.array([1,2,3])
b=np.array([4,5])
try:
    a+b                 # This does not work since it violates the rule 3 above.
except ValueError as e:
    import sys
    print(e, file=sys.stderr)