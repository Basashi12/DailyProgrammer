# Challenge 21 Easy
# https://www.reddit.com/r/dailyprogrammer/comments/qp3ub/392012_challenge_21_easy/
# Input: a number
# Output : the next higher number that uses the same set of digits.


# If there are duplicate digits, nums contains same number, same index combos

import itertools

def findnextperm(n):
    num = str(n)
    nums = []
    for perms in itertools.permutations(num):
        nums.append(int(''.join(perms)))
    snums = list(sorted(set(nums))) # set gets rid of duplicates
    place = snums.index(int(num))
    print(snums[place+1])

# A challenge in making this work for# numbers w/ duplicate digits
