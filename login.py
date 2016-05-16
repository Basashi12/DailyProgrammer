# Challenge no. 5 easy
# https://www.reddit.com/r/dailyprogrammer/comments/pnhyn/2122012_challenge_5_easy/
# Create a program which is password protected,
# and wont open unless the correct user and password is given.

import csv

def main():
    pass

def get_userpw():
    with open('pw_file.csv', mode='r') as readfile:
        reader = csv.reader(readfile)
        mydict = {rows[0]:rows[1] for rows in reader}
    trylogin()

def trylogin():
    user = input('Enter your user name: ')
    if user not in mydict.keys():
        print('Username not found!')
        trylogin()
    else:
        pw = input('Enter your password: ')
        if pw != mydict[user]:
            print('Sorry wrong password!')
            trylogin()
        else:
            print('You now have successfully logged in.  Please change your password.')

if __name__ == '__main__':
    get_userpw()
