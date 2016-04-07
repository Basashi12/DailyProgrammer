def tetra(n):
    t = 0
    i = 1
    while t < n:
        t = (i * (i + 1) * (i + 2)) / 6
        i += 1
    else:
        print(i-1) # i += 1 an extra time

def base(n):
    t = (n * (n + 1) * (n + 2)) / 6
    return t
