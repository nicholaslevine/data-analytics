import numpy as np
import matplotlib.pyplot as plt
import os

painting = os.path.join(os.path.abspath(os.path.dirname(__file__)), "painting.png")
img = plt.imread(painting)
def center(image):
    shape = image.shape
    return ((int(shape[0]-1)/2), int((shape[1]-1)/2))

def radial_distance(image):
    # mapping an array with distance from center
    shape = image.shape
    c = center(image)
    w, h = shape[0], shape[1]
    y_indices, x_indices = np.ogrid[:w, :h]
    # a = np.linspace(0, 1, w*h).reshape(w, h, 1)

    center_x, center_y = c[0], c[1]
    d = np.abs(np.sqrt(np.abs(y_indices - center_y) ** 2 + np.abs(x_indices - center_x) ** 2)-1).reshape(w, h, 1)
    # d = np.abs(np.abs(a-0.5)*2 - 1)
    return d
rd = radial_distance(img)
print(rd)
def scale(a, tmin = 0.0, tmax = 1.0):
    # scaling each value to the max and min values
    max_distance = np.max(a)
    min_distance = np.min(a)
    if (max_distance == min_distance):
        return "cannot be the same number"
    scale_factor =  (tmax-tmin) / (max_distance - min_distance)
    return a * scale_factor
factor = scale(rd)
def radial_fade(image, scaled_array):
    return image * scaled_array
x = radial_fade(img, factor)
plt.imshow(x)
plt.show()
