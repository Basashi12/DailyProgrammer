# Challenge 11 Easy
# https://www.reddit.com/r/dailyprogrammer/comments/pwons/2192012_challenge_11_easy/
# Takes year, month, and date as inputs
# Returns what day of the week that falls on

import calendar

def main():
    pass

# Python has a built in calendar module
def day():
    print('Please input what date you would like to know the day of the week for: ')
    year = int(input('Please input a year in 4 digits: '))
    month = int(input('Please input which month: '))
    date = int(input('Please input which date: '))
    youbi = calendar.weekday(year, month, date)
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


if __name__ == '__main__':
    main()
