# Challenge 34 Easy
# https://www.reddit.com/r/dailyprogrammer/comments/rmmn8/3312012_challenge_34_easy/
# Input list of 3 numbers
# Output sum square or two larger numbers

 def ss2(nlist):
    # nlist is input of 3 numbers
    nlist.remove(min(nlist))
    x = sum(i**2 for i in nlist)
    return x
