# Difficult challenge no. 2

import time

def main():
    pass

def timer():
    print('Timer will start when you press enter.')
    input('Press enter to continue: ')
    t0 = time.time()
    print('Timer has started.')
    print('Timer will stop when you press enter.')
    input('Press enter to continue: ')
    print('Timer has stopped.')
    t1 = time.time()
    print(t1 - t0)

if __name__ == '__main__':
    main()   
