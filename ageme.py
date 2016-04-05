# Challenge 20 Medium

def ageme():
    y = int(input('How old are you in years? '))
    months = y * 12
    days = y * 365
    hours = days * 24
    minutes = hours * 60
    print('You are {} months old.'.format(months))
    print('You are {} days old.'.format(days))
    print('You are {} hours hold.'.format(hours))
    print('You are {} minutes hold.'.format(minutes))
