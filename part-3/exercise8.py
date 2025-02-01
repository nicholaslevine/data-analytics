import numpy as np
def almost_meeting_lines(a1, b1, a2, b2):
    a = np.array([[a1, -1], [a2, -1]])
    b = np.array([-b1, -b2])
    return (np.linalg.lstsq(a, b)[0], np.linalg.lstsq(a, b)[0] == np.linalg.solve(a, b)[0])
print(almost_meeting_lines(1, 0, -1, 2))