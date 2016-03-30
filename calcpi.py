# Challenge no 6 easy

import decimal, math

def main():
    pass

def prec(n):
    decimal.getcontext().prec = n+2
    calc_pi(n)

def calc_pi(n):
    # calculating pi to an accuracy of n decimal places
    delta = math.pow(10,-n)
    actualpi = 4 * (4 * (math.atan(1/2)) - (math.atan(1/239)))
    arctan = 0
    i = 1
    while abs(actualpi - pie) < delta:
        term = ((-1)**(i + 1)) / (2 * (i - 1) + 1)
        arctan += term
        pie = 4 * arctan
        i += 1
        return pie
    print('After {} iterations, computed pi to {}th decimal precision.'.format(i, n))
    print(pie)
        
if __name__ == '__main__':
    main()
