# Challenge # 12 intermediate
# Create a program which will factor a number

import math

def main():
    pass

def factoring(num):
    onum = num
    factors = []
    i = 2
    while i <= onum//2:
        if num % i:
            i += 1
        else:
            factors.append(i)
            num = (num/i)
    if factors:
        print('{} are the factors of {}.'.format(factors, onum))
    else:        
        print('{} is prime!'.format(onum))

if __name__ == '__main__':
    main()

