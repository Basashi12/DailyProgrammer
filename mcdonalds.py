# Challenge 23 Intermediate
# https://www.reddit.com/r/dailyprogrammer/comments/qulnf/3132012_challenge_23_intermediate/
# Find all McNugget Numbers - numbers which are the sum of McNugget combinations

def nugget(x):
    mnn = []
    q = [6, 9, 20]
    # try all numbers from 1 to x
    sample = list(range(1, x+1))
    # brute force calculation
    for i in sample:
        # floor divide i by 6 with "buffer" of 2
        n = (i // 6) + 2
        for j in range(0,n):
            for k in range(0,n):
                for l in range(0,n):
                    if j + k + l <= n:
                        y = 6 * j + 9 * k + 20 * l
                        if y == i:
                            mnn.append(i)
                        else:
                            continue
                    else:
                        continue
    print('Printing list of all non-McNugget numbers')
    print(list((set(sample) - set(mnn))))

# Simple multiplication faster in line 18 than using sum, zip, lambda
