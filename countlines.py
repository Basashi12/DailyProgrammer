# Challenge #37 Easy
# https://www.reddit.com/r/dailyprogrammer/comments/rzdwq/482012_challenge_37_easy/

def count(filename):
    count = 0
    wordcount = 0
    for line in open(filename).readlines(): count += 1
    for words in open(filename).read().split(): wordcount += 1
    return count, wordcount
