# Challenge no 6 easy
# https://www.reddit.com/r/dailyprogrammer/comments/pp53w/2142012_challenge_6_easy/
# Calculate pi to 30 decimals
import math
from decimal import *

def main():
    pass

def prec(n):
    # sets the decimal precision to at least n, using decimal module
    decimal.getcontext().prec = n+5
    
def calc_pi(n):
    # pi100 is pi to 100 decimals
    pi100 = Decimal(3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679)
    # calculating pi to an accuracy of n decimal places
    # .64 is approximation of precision
    delta = Decimal(.64 * math.pow(10,-(n+1)))
    arctan = 0 # initializing variables
    i = 0
    pie = 0
    while abs(Decimal(pi100 - pie)) > delta:
        term = Decimal(math.pow(-1, i)) / Decimal((2 * i) + 1)
        arctan += Decimal(term)
        pie = Decimal(4 * arctan)
        i += 1
        if i % 1000000 ==0:
            print(i, pie)
    print('After {} iterations, computed pi to {}th decimal precision.'.format(i, n))
    print(pie)

if __name__ == '__main__':
    main()
