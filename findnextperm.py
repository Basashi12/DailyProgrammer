# Challenge 21 Easy

# Had a bit of a challenge in making this work for
# numbers which had duplicate digits

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
