# Challenge 39 Easy
# https://www.reddit.com/r/dailyprogrammer/comments/s6bas/4122012_challenge_39_easy/
# Takes parameter n
# Prints number on each line, except
# if n % 3, print Fizz, n % 5 Buzz, both, FizzBuzz

def nprint(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
