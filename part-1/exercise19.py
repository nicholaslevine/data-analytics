from functools import reduce
def find_sum(sum, current):
    sum + current

def sum_equation(arr):
    sum = reduce(lambda x, y: x + y, arr)
    strings = list(map(str, arr))
    equation = " + ".join(strings)
    return f"{equation} = {sum}"
print(sum_equation([1, 5, 7]))