# Challenge 9 Easy

def ui():
    ri = input('What should the program sort, strings or numbers? ')
    if ri == 'strings':
        ssort()
    elif ri == 'numbers':
        nsort()
    else:
        print('Invalid input')

def ssort():
    ri = input('Please enter strings to sort: ').split(',')
    if type(ri) != tuple:
        ssort = list(ri)
        sortage = sorted(ssort)
        print(sortage)
    elif type(ri) == list:
        sortage = sorted(ri)
        print(sortage)
    else:
        print('Invalid input')

def nsort():
    ri = (input('Please enter numbers to sort: ')).split(',')
    if type(ri) == tuple:
        nsort = list(ri)
        sortage = sorted(nsort, key=int)
        print(sortage)
    elif type(ri) == list:
        sortage = sorted(ri, key=int)
        print(sortage)
    else:
        print('Invalid input')
