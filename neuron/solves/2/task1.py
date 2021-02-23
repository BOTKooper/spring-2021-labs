import math

""" Task 1
Tell user if point is in the restricted areas
"""


def ExtendedCircle(x, y):
    # Checking for range
    if x > 1 or y > 1 or x < -1 or y < -1:
        return False

    # Maybe we are in the circle itself
    if(math.sqrt(x**2 + Y**2) <= 1):
        return True

    # Top-right non-circle segment
    if x >= 0 and Y >= 0:
        return True

    # Bottom-left non-circle segment
    if x <= 0 and Y <= 0:
        return True


def SquareMinusCircle(x, y):
    # Checking for range
    if x > 3 or y > 3 or x < -3 or y < -3:
        return False

    # is point in the circle itself?
    if(math.sqrt(x**2 + y**2) <= 9):
        return False

    return True


def TwoEllipses(x, y):
    a1, b1 = [2, 1]  # semiaxises for horizontal ellipse
    a2, b2 = [1, 2]  # semiaxises for vertical ellipse

    def isXYInEllipse(x, y, a, b):
        # taken from https://coderoad.ru/43442357/Как-определить-находится-ли-точка-внутри-эллипса-который-находится-внутри#43442461
        return (x**2) / (a**2) + ((y**2)/b**2) <= 1 # since center of both ellipses is {0,0} we could reuse '1'

    return isXYInEllipse(x, y, a1, b1) or isXYInEllipse(x, y, a2, b2)


X = float(input("Enter X coord: "))
Y = float(input("Enter Y coord: "))

print()

print("Extended circle:", ExtendedCircle(X, Y))
print("Square minus circle:", SquareMinusCircle(X, Y))
print("Two Ellipses:", TwoEllipses(X, Y))
