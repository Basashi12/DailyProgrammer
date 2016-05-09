# Challenge 27 Easy
# https://www.reddit.com/r/dailyprogrammer/comments/r0r3h/3172012_challenge_27_easy/
# Accepts a year as input and outputs the century the year belongs
# and whether or not the year is a leap year. 

def century():
    n = int(input('Enter year: '))
    if n % 100 == 0:
        print('Century: {}'.format(int(n/100)))
    else:
        print('Century: {}'.format(int((n//100)+1)))
    leapyear = False
    if n % 4 != 0:
        leapyear = False
    elif n % 100 != 0:
        leapyear = True
    elif n % 400 != 0:
        leapyear = False
    else:
        leapyear = True

    if leapyear == True:
        print('Leap year: Yes')
    else:
        print('Leap year: No')

