# Challenge 35 Easy
# https://www.reddit.com/r/dailyprogrammer/comments/rr4y2/432012_challenge_35_easy/
import math


def trinum(n):
    z = (math.sqrt((8 * n) + 1) - 1 / 2)
    if z is int:
        return z, n
    else:
        trinum(n-1)

def triconstruct(z, n):
    
