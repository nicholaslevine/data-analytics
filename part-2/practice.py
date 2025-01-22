import numpy as np

np.array([1, 0, 3]) # one dimensional array

np.array([[1, 2, 3], [4, 5, 6]]) #two dimensional array

np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]) # three dimensional array

np.zeros((3, 4)) # 2d array with floats and 3 rows and 4 columns

np.zeros((3, 4), dtype=int) #changed type to int

np.full((2,3), fill_value=7) #fukks 2d array with fill value

np.empty((2,4)) #leaves elements uninitalized

np.eye(5, dtype=int) #creates identity matrix with 5 rows and columns

np.arange(0, 10 , 2) #creates array of elements sorted in ascending order going up by increments of two, non inclusive

np.linspace(0, np.pi, 5) #Evenly spaced, 5 elements, better for non-int values, is inclusive

np.random.random((3, 4)) #creates 2D array with 3 rows of 4 columns, all of which lie in the interval [0.0, 1.0)

np.random.normal(0, 1, (3, 4)) #bell curve (normal distribution) of values. The bell curve has a peak of 0

np.random.randint(-2, 10, (3, 4)) # random integers distributed for 3 rows of 4 columns

np.random.seed(0) #starting point to create random numbers deterministically , that uses the global random number generator, resulting in the same result every time a random function is called without creating a new seed.

np.random.randint(0, 100, 10) #results in 10 random integers from 0 to 100 in an array

np.random.normal(0, 1, 10) #like normal except for 1d 

new_generator = np.random.RandomState(seed=123)
#now you will get a different result with a new generator

new_generator.randint(0, 100, 10) # different numbers this time


def info(name, a):
    print(f"{name} has dimensions {a.ndim}, shape {a.shape}, size {a.size}, and data type {a.dtype}")
    print(a)

b = np.array([[1, 2, 3], [4, 5, 6]])

info ("b", b) # returns b has dim 2, shape (2, 3), size 6, and dtype int64:
# [[1 2 3]
# [4 5 6]]

#we can create a 3 dimensional array by making an array of two of the b array like so
c = np.array([b, b])
info("c", c)
#returns c has dim 3, shape (2, 2, 3), size 12, and dtype int64:
# [[[1 2 3]
# [4 5 6]]

# [[1 2 3]
# [4 5 6]]]

d = np.array([[1, 2, 3, 4]]) # a row vector
info("d", d)
# returns 
# d has dim 2, shape (1, 4), size 4, and dtype int64:
# [[1 2 3 4]]


#array in python work like arrays in any other language
dfg = np.array([[1, 2, 3], 
               [4, 5, 6]])
#print(dfg[1, 2]),  rows them columns, so would print 5
#print(dfg[0, -1], would print 3, 0th row, -1 (or last) column

# it is good to note that you can also modify lists, so b[0, 0] = 10 would be perfectly valid

#if you only provide one index of the array, it indexes the first dimension, or the rows

#a[1:3] works like it does in a list in Python, slices from index 1 (inclusive) to index 3 (exclusive)

#a[::-1] #Reverses the list

#for a 2d array, you just use a comma like:
# b[:, 0] -> all in the first column
# b[0, :] -> all in the first row
# b[:, 1:] -> all but the first column

b[:, 1:] = 7
#works for slicing

a = np.arange(9)
anew = a.reshape(3, 3)
info("anew", anew)

# returns anew has dim 2, shape (3, 3), size 9, and dtype int64:
# [[0 1 2]
# [3 4 5]
# [6 7 8]]

info("a", a)
 
#returns a has dim 1, shape (9,), size 9, and dtype int64:
#[0 1 2 3 4 5 6 7 8]

np.concatenate((a, b)) # how you can concatenate one function to the end of another

np.concatenate((a, b), axis = 1) # usually concatenates on axis 0, resulting in concatenation on the highest level, but can be concatenated on a lower level using 1 (or more)

x = [1, 3, 6]
np.stack((x, x))
# returns [[1,3,6], [1, 3, 6]]
#stacks things on top of each other unless specified otherwise (with axis)

d = np.arange(12).reshape(6, 2)
print(d)
d1, d2 = np.split(d, 2)
# printing these out you get d as
#[[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11]]
# you get d1 as [[0, 1], [2, 3], [4, 5]]
# and you get d2 as [[6, 7], [8, 9], [10, 11]]
#if you choose axis = 1, you get [0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]

np.random.seed(0)
a=np.random.randint(-100, 100, (4,5))
print(a)
print(f"Minimum: {a.min()}, maximum: {a.max()}")
print(f"Sum: {a.sum()}")
print(f"Mean: {a.mean()}, standard deviation: {a.std()}")
##you can use aggregations over rows at well
np.random.seed(9)
b=np.random.randint(0, 10, (3,4))
print("Row sums:", b.sum(axis=1))


## axis 0 is columns, axis 1 is rows

