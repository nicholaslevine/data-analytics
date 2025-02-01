import numpy as np
def meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3):
    a = [[a1, b1, -1], [a2, b2, -1], [a3, b3, -1]]
    c = [-c1, -c2, -c3]
    return np.linalg.solve(a, c)
print(meeting_planes(-1, -1, 6, (-2/3), (1/3), 14/3, 3, 4, -4))