import math

# DEFAULTS FOR VARIANT 13
DEF_A1 = 7
DEF_T = 2
DEF_Z = 4



""" Task 2
Multiply first Z elements of arithmetic progression with given a(1), t (diff) and Z (amount of elements)
"""

def solve(a1, t, z):
    mul = a1
    element = a1
    for i in range(1, z):
        element += t
        mul *= element
    return mul


flag = input("do you want to use defaults, or custom variables? (d/c): ")

if flag == 'd':
    print(solve(DEF_A1, DEF_T, DEF_Z))
elif flag == 'c':
    A1 = int(input("Enter a(1): "))
    T = int(input("Enter t: "))
    Z = int(input("Enter z: "))

    print(solve(A1, T, Z))
else:
    raise ValueError('Invalid choice')


