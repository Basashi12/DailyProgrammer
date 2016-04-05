# Challenge 23 Easy
# https://www.reddit.com/r/dailyprogrammer/comments/quli5/3132012_challenge_23_easy/
# Your task is to write the function that splits a list in two halves
# If the input list has an odd number, the middle item can go to any of the list

def split(a):
    h = len(a)//2
    b = a[:h]
    c = a[h:]
    return b, c
