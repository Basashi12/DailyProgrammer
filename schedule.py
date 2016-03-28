# Challenge from:
# https://www.reddit.com/r/dailyprogrammer/comments/pihtx/intermediate_challenge_1/

import sys

def main():
    pass

events = {} # a dict

init_schedule():
    question = input('''What would you like to do? /n Input a to add an event
                /n Input d to delete an event
                /n Input l to list events
                /n Input q to quit''')
    if question == 'a':
        add_event()
    elif question == 'd':
        delete_event()
    elif question == 'l':
        list_event()
    elif question == 'q':
        sys.exit()
    else:
        print('Not a valid response')
        init_schedule()

add_event():
    # Adds event to calendar, must be integer
    V = input('Please enter an event description: ')
    t = input('Please enter at what hour the event takes place: ')
        if t != int:
            t = input('Please enter an integer: ')
            if t != int or t > 23 or t < 0:
                raise ValueError
            else:
                continue
    global events
    events.append([V, t])

delete_event():
    # Delets event from calendar, using event name as key
    V = input('Please enter which event you would like to delete: ')
    global events
    events.pop(keys=V)

list_event():
    # Prints out all events saved into global events dict
    global events
    events.sort()
    for e in events:
        print('Event: {0} \n Time: {1}'.format(e[0], e[1]))


if __name__ == '__main__':
    main()



