# Challenge 35 Easy
# https://www.reddit.com/r/dailyprogrammer/comments/rr4y2/432012_challenge_35_easy/

import math


def trinum(n):
    if (math.sqrt((8 * n) + 1) - 1) % 2 == 0:
        z = (math.sqrt((8 * n) + 1) - 1) / 2
        print(z, n)
        return z, n
    else:
        trinum(n-1)

def triconstruct(z, n):
    for i in range(z, 0, -1):
        for j in range(n-i+1, n+1):
            print(j, end=' ')
        n -= i
        print('\n')
