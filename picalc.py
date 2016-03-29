# Challenge no 6 easy

import decimal

def main():
    pass

# pi / 4 = arctan (1)

def at(n):
    arctan = 0
    for x in range(1, n+1):
        term = ((-1)**(x+1)) / (2*(x-1) + 1)
        arctan += term
    pie = arctan * 4
    return pie

        
if __name__ == '__main__':
    main()
