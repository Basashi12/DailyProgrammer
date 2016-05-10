# Challenge #37 Easy
# https://www.reddit.com/r/dailyprogrammer/comments/rzdwq/482012_challenge_37_easy/
# input : a file as an argument
# output: counts the total number of lines.
# for bonus, also count the number of words in the file. 

def count(filename):
    # initialize var
    lcount = 0
    wcount = 0
    for line in open(filename).readlines(): lcount += 1
    for words in open(filename).read().split(): wcount += 1
    return lcount, wcount
