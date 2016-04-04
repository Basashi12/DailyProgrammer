# Challenge 14 Difficult

import numpy as np

# Unable to get multithreading (unnessary with only a million numbers)

def main():
    pass

z = np.random.randint(0,100, 1000000)

y = np.sort(z)

# %prun can be used to compare quicksort, mergesort, heapsort in np

if __name__ == '__main__':
    main()
