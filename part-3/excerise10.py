import numpy as np
import matplotlib.pyplot as plt
def subfigures(arr):
    fig, ax = plt.subplots(1, 2)
    xvals = arr[:, 0]
    yvals = arr[:, 1]
    ax[0].plot(xvals, yvals, label="line")
    ax[0].set_title("First subfigure")
    ax[0].set_xlabel("x-axis")
    ax[0].set_ylabel("y-axis")
    ax[1].scatter(xvals, yvals, label="scatter plot")
    ax[1].set_title("second subfigure")
    ax[1].set_xlabel("x-axis")
    ax[1].set_ylabel("y-axis")
    fig.suptitle("first figure", fontsize=16, fontweight = "bold")
    plt.show()
subfigures(np.array([[1, 2], [4, 5], [3, 4]]))