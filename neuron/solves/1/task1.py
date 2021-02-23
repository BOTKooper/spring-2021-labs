import math

""" Task 1
Calculate surface of the triangle with this sides
"""
TRIANGLE_SIDES = [7, 12, 15]


def solve(a, b, c):
    P = a + b + c
    p = P / 2
    S = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return S


print(solve(TRIANGLE_SIDES[0], TRIANGLE_SIDES[1], TRIANGLE_SIDES[2]))
