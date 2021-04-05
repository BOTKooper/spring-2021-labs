""" Task 3
Calculate sum of elements in geometrical progression which are greaten than given value.
Values given: a(1), t, alim
"""

# DEFAULTS FOR VARIANT 13
DEF_A1 = 70.0
DEF_ALIM = 2.0
DEF_T = 0.4


def solve(a1, t, alim):
    if t >= 1:
        raise ValueError('Invalid T')
    sum = a1
    element = a1
    while True:
        element *= t
        if element > alim:
            sum += element
        else:
            break
    return sum


flag = input("do you want to use defaults, or custom variables? (d/c): ")

if flag == 'd':
    print(solve(DEF_A1, DEF_T, DEF_ALIM))
elif flag == 'c':
    A1 = float(input("Enter a(1): "))
    ALIM = float(input("Enter alim: "))
    T = float(input("Enter t: "))

    print(solve(A1, T, ALIM))
else:
    raise ValueError('Invalid choice')
