import math

N = 13
MAGIC = N + 9

""" Task 3
We are given with a list of N+10 numbers (N=13), We should swap 0th and N+10th elements

Example test: 
    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
        ->
    [23, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 1]
"""


def solve(arr):

    newArr = [arr[MAGIC]] + arr[1:MAGIC] + [arr[0]]

    return newArr


Arr = list(map(int, input(
    "Type elements of the list in the single line (e.g. 1 5 ... 43 22): ").split()))

if len(Arr) != 23:
    raise ValueError('Invalid array length')


print(solve(Arr))
