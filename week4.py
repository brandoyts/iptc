def getSquare():
    print("\n\nCompute the area of a square")
    length = int(input("Please enter the length of a side: "))
    area = length * length
    print(f"The area of the square will be {length} * {length} = {area}")


def getRectangle():
    print("\n\nCompute the area of a rectangle")
    width = int(input("Please enter the width of a rectangle: "))
    length = int(input("Please enter the length of a reactange: "))
    area = width * length
    print(f"The area of the rectangle will be {width} * {length} = {area}")


def getTriangle():
    print("\n\nCompute the area of a triangle")
    base = int(input("Please enter the base of a triangle: "))
    height = int(input("Please enter the height of a triangle: "))
    area = (base * height) / 2
    print(f"The area of the triangle will be ({base} * {height}) / 2 = {area}")


# **AREA OF A SQUARE
getSquare()

# **AREA OF A RECTANGE
getRectangle()

# **AREA OF A TRIANGLE
getTriangle()
