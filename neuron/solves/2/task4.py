import math

N = 13

SENTENCE = "Програміст — фахівець, що займається програмуванням, виконує розробку програмного забезпечення" \
    + " (в простіших випадках — окремих програм) для програмованих пристроїв, які, як правило містять один процесор чи більше"


""" Task 3
Swap Nth and 20-Nth words in the given sentence

Note: I don't want to play with Regex, so it would swap world with symbols like comma and dash too
"""


def solve(arr):
    res = arr.copy()
    tmp = res[N-1]
    res[N-1] = res[20 - N - 1]
    res[20 - N - 1] = tmp
    return " ".join(res)


Arr = list(map(str, SENTENCE.split()))

print(solve(Arr))
