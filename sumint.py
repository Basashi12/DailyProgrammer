# Challenge 30 Easy
# https://www.reddit.com/r/dailyprogrammer/comments/reago/3262012_challenge_30_easy/

from itertools import combinations

def sumin(intlist, tgt):
    ss = combinations(intlist, 2)
    sol = []
    for a, b in ss:
        if a + b == tgt:
            sol.append([a,b])
        else:
            continue
    if sol:
        print('{} hit the target {}.'.format(sol, tgt))
    else:
        print('No two integers in the list sum to the target {}.'.format(tgt))
