import math
def solve_quadratic(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    d = math.sqrt(b*b - 4*a*c)
    x1 = (-b + d)/(2*a)
    x2 = (-b - d)/(2*a)
    print(f"({x1}, {x2})")
print(solve_quadratic(1, -3, 2))
print(solve_quadratic(1, 2, 1))