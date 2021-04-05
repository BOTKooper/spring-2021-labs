import math

""" Task 5
Check if given array of N+5 elements is corted in given order (0=acs, 1=desc)
then mutate each array element to be equal iteself+index
"""


def is_sorted(arr, order):
    for i in range(0, len(arr) - 1):
        if order == 0:
            if arr[i] > arr[i + 1]:
                return False
        else:
            if arr[i] < arr[i + 1]:
                return False
    return True

def solve(arr, order):
    sorted = is_sorted(arr, order)
    if sorted == False:
        return arr
    for i in range(0, len(arr)):
        arr[i] += i
    return arr


N = int(input("Enter N: "))
Arr = list(map(float, input(
    "Type elements of the list in the single line (e.g. 1 5 ... 43 22): ").split()))
Order = int(input("Enter sorting order (0=acs, 1=desc): "))

if len(Arr) != N + 5:
    raise ValueError('Invalid length of the list')
if Order != 0 and Order != 1:
    raise ValueError('Invalid order given')

print(solve(Arr, Order))
