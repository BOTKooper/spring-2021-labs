import math

""" Task 2
Calculate equation with this data
Notes: Beta is unused, should it be so through?
"""
a, x, Beta = 0.5, 3.4, 1.65


def solve(a, x, Beta):
    top = math.pi + math.atan(x**2 + a**5) - \
        math.sqrt(1+x*a) + math.asin(a - (0.5 * (10**-3)))

    bottom = 4.8*(10**2.6) - math.log(abs(x-a), 3) + 7 * \
        (math.exp(-x)) + math.log(x, math.exp(1)) ** 2 - math.tan(a*x)

    res = top / bottom
    return res

print(solve(a, x, Beta))
