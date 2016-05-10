# Challenge 25 Intermediate
# https://www.reddit.com/r/dailyprogrammer/comments/qxvu2/3152012_challenge_25_intermediate/
# Accept CMD argument for base 10 number and return binary number

import sys

def main():
    num = int(sys.argv[1])
    bi(num)

def bi(n):
    # bin outputs '0b', need to truncate
    print(str(bin(n))[2:])

if __name__ == '__main__':
    main()
