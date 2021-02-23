import math


""" Task 2
Solve equation with given {x, a}
"""


def solve(x, a):
    # We'll divide by smth*a, so we could potentially divide by 0
    if a == 0:
        return math.nan

    y = 0

    if x > 0:
        y = (x - 8 * (a**3)) / (x**2 + 4 * (a**2))
    else:
        y = -a * math.sqrt((1 - x**2) / (4 * (a**2)))

    return y


X = float(input("Enter x: "))
A = float(input("Enter a: "))

print(solve(X, A))
