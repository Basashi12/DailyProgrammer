# Challenge 22 easy
# https://www.reddit.com/r/dailyprogrammer/comments/qr0hg/3102012_challenge_22_easy/
# Write a program that will compare two lists
# and append any elements in the second list that don't exist in the first

def listcomp(a, b):
    return = list(set(a + b))

# could have also done (set(a)).union(set(b))
