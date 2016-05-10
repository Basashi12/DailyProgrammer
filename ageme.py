# Challenge 20 Medium
# https://www.reddit.com/r/dailyprogrammer/comments/qnkpp/382012_challenge_20_intermediate/
# create a program that will take user input and tell them their age in months, days, hours, and minutes

def ageme():
    # accept input in years
    y = int(input('How old are you in years? '))
    # calculate age in M, D, H, M
    months = y * 12
    days = y * 365
    hours = days * 24
    minutes = hours * 60
    # print formatted output
    print('You are {} months old.'.format(months))
    print('You are {} days old.'.format(days))
    print('You are {} hours hold.'.format(hours))
    print('You are {} minutes hold.'.format(minutes))
