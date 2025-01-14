from triangle import hypotenuse, area

def main():
    side_a = 3.0
    side_b = 4.0

    hyp = hypotenuse(side_a, side_b)
    print(f"The hypotenuse of the triangle with sides {side_a} and {side_b} is {hyp:.2f}")

    tri_area = area(side_a, side_b)
    print(f"The area of the triangle with sides {side_a} and {side_b} is {tri_area:.2f}")

if __name__ == "__main__":
    main()