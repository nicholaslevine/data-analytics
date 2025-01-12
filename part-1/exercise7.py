import math
while True: 
    shape = input("Choose a shape (triangle, rectangle, circle): ")
    if (shape == "triangle"):
        base = float(input("Give base of the triangle: "))
        height = float(input("Give height of the triangle: "))
        print(f"The area is {base*height/2}")
    elif (shape == "rectangle"):
        width = float(input("Give width of the rectangle: "))
        height = float(input("Give height of the rectangle: "))
        print(f"The area is {width*height}")
    elif (shape == "circle"):
        radius = float(input("Give radius of the circle: "))
        print(f"The area is {radius*radius*math.pi}")
    elif (shape == ""):
        break
    else:
        print("Unknown shape")
