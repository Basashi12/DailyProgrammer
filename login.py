# Challenge no. 5 easy

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
