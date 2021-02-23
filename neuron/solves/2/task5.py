import math

N = 13

""" Task 2
Calculate n! (n=N+5)
"""


def solve(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact


n = N + 5

print("Manually: ", solve(n))
print("math.factorial: ", math.factorial(n))
