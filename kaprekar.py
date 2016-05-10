# Challenge 39 Intermediate
# Find whether a number is kaprekar or not

def kaprekar(n):
    # 0 and negative numbers are False
    if n <= 0:
        return False
    elif n == 1:
        return True
    elif 2 <= n <=4:
        return False
    else:
        sq = n**2
        if len(str(n)) == 1:
            split = 1
        else:
            split = len(str(sq))//2
        lhalf = str(sq)[:split]
        rhalf = str(sq)[split:]
        if n == int(lhalf) + int(rhalf):
            return True
        else:
            return False

# Cannot use import math because int('1.0') is NaN

