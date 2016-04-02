# Challenge # 12 intermediate

import math

def main():
    pass

def factoring(num):
    onum = num
    factors = []
    ceil = math.floor(num / 2)
    i = 2
    while i in range(2, ceil+1):
        if num % i == 0:
            factors.append(i)
            num = (num/i)
            i = i
        else:
            i += 1
    print('{} are the factors of {}'.format(factors, onum))

if __name__ == '__main__':
    main()

