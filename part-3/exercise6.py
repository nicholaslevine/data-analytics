import numpy as np
def meeting_lines(a1, b1, a2, b2):
    a = np.array([[a1, -1], [a2, -1]])
    b = np.array([-b1, -b2])
    return np.linalg.solve(a, b)
print(meeting_lines(1, 0, -1, 2))
