# Challenge 14 medium

# Could have sped up calculation by using n//2 instead of n
# Experienced some issues in x.remove(y) errors

def main():
    pass

def sundaram(n):
    primes = [2] # 2 is prime.  Sundaram finds only odd primes.
    fsieve = []
    ssieve = []
    x = list(range(1, n+1))
    for i in range(1, n+1):
        for j in range(i, n+1):     # j from i to n+1
            # compute all i + j + 2*i*j
            z = (i + j + 2 * i * j)
            if z <= n:
                fsieve.append(z)
    fsieve = list(set(fsieve))
    # fsieve * 2 + 1 not prime
    for y in fsieve:    
        x.remove(y)
    for num in x:
        if 2 * num + 1 <= n:
            primes.append(2 * num + 1)
    print('Printing primes up to {}.'.format(n))
    print(primes)
   
if __name__ == '__main__':
    main()
