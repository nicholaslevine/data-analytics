__version__ = "1.0"
__author__ = "Nicholas Levine"

import math

def hypotenuse(a: float, b: float) -> float:
    return math.sqrt(a**2 + b**2)


def area(a:float, b: float) -> float:
    return 0.5*a*b