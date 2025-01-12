arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1, 11):
    def multiply(x):
        return x*i
    newArr = map(multiply, arr)
    strArr = map(str, newArr)
    print("  ".join(strArr))