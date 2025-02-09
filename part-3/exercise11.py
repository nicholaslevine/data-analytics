import numpy as np
import matplotlib.pyplot as plt
import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "painting.png")
painting = plt.imread(path)
def to_grayscale(image):
    grayscale = image * [[[0.7, 0.7, 0.7]]]
    return grayscale
d = to_grayscale(painting)

def to_red(image):
    redscale = image * [[[1, 0, 0]]]
    return redscale
def to_green(image):
    greenscale = image * [0, 1, 0]
    return greenscale
def to_blue(image):
    bluescale = image * [0, 0, 1]
    return bluescale
a = to_red(painting)
b = to_green(painting)
c = to_blue(painting)
fig, ax = plt.subplots(2, 2)
ax[0,0].imshow(a)
ax[0, 1].imshow(b)
ax[1, 0].imshow(c)
ax[1, 1].imshow(d)
plt.show()

