# Challenge # 12 intermediate
# Create a program which will factor a number

import math

def main():
    pass

def factoring(num):
    onum = num
    factors = []
    ceil = math.floor(num / 2)
    i = 2
    for i in range(2, ceil+1):
        if num % i == 0:
            factors.append(i)
            num = (num/i)
            i = i
            print('Printing {}'.format(i))
        else:
            i += 1
    if factors:
        print('{} are the factors of {}.'.format(factors, onum))
    else:        
        print('{} is prime!'.format(onum))

if __name__ == '__main__':
    main()

