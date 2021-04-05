import math


""" Task 1
Calculate amount of positive bits of the given N (convert from decimal to binary on the first place)
"""

def solve(n):
    bin_str = bin(n)[2:]
    counter = 0
    for i in bin_str:
        if i == '1':
            counter+=1
    return counter



N = int(input("Enter N: "))

print(solve(N))
