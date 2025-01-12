def triple(x):
    return x * 3
def square(x):
    return x ** 2

for i in range(1, 11):
    if (triple(i) < square(i)):
        break
    print(f"triple({i})=={triple(i)} square(i)=={square(i)}")