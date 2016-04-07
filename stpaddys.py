# Challenge 27 Intermediate
# https://www.reddit.com/r/dailyprogrammer/comments/r0r46/3172012_challenge_27_intermediate/
# Borrows from my daywindow.py program.

import calendar

def stpatrick():
    print("Please input what year you would like to know St. Patrick's day for: ")
    year = int(input('Please input a year in 4 digits: '))
    youbi = calendar.weekday(year, 3, 17)
    if youbi is 0:
        print('Monday')
    elif youbi is 1:
        print('Tuesday')
    elif youbi is 2:
        print('Wednesday')
    elif youbi is 3:
        print('Thursday')
    elif youbi is 4:
        print('Friday')
    elif youbi is 5:
        print('Saturday')
    elif youbi is 6:
        print('Sunday')
    else:
        print('Something went wrong')

def stpatrickcent():
    sat = 0
    for year in range(2001, 2099):
        youbi = calendar.weekday(year, 3, 17)
        if youbi is 5:
            sat += 1
        else:
            continue
    print("This century, St. Patrick's Day falls on a Saturday {} times.".format(sat))        
