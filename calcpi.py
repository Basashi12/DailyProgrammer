# Challenge no 6 easy

import decimal, math

def main():
    pass

def prec(n):
    # sets the decimal precision to at least n, using decimal module
    decimal.getcontext().prec = n+5
    
def calc_pi(n):
    # calculating pi to an accuracy of n decimal places
    delta = math.pow(10,-n)
    actualpi = 4 * (4 * (math.atan(1/5)) - (math.atan(1/239)))
    arctan = 0 # initializing variables
    i = 0
    pie = 0
    while abs(actualpi - pie) > delta:
        term = math.pow(-1, i) / (2 * (i - 1) + 1)
        arctan += term
        pie = 4 * arctan
        i += 1
    print('After {} iterations, computed pi to {}th decimal precision.'.format(i, n))
    print(pie)
        
if __name__ == '__main__':
    main()
