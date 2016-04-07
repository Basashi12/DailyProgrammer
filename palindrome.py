# Challenge 29 Easy
# https://www.reddit.com/r/dailyprogrammer/comments/r8a70/3222012_challenge_29_easy/ 

def pal(test):
    f = list(str(test))
    b = f[::-1]
    if f == b:
        print('{} is a palindrome!'.format(test))
    else:        
        print('{} is not a palindrome.'.format(test))
