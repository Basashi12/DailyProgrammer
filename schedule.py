# Challenge from:
# https://www.reddit.com/r/dailyprogrammer/comments/pihtx/intermediate_challenge_1/

import sys

def main():
    pass

def init_schedule():
    events = {}
    question = input('''What would you like to do?\nInput a to add an event
                \nInput d to delete an event
                \nInput l to list events
                \nInput q to quit\n''')
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

def add_event():
    # Adds event to calendar, must be integer
    V = input('Please enter an event description: ')
    t = int(input('Please enter the hour at which the event takes place: '))
    if t < 0:
        raise ValueError
        init_schedule()
    elif t > 23:
        raise ValueError
        init_schedule()
    else:
        global events
        events[t] = V
    init_schedule()

def delete_event():
    # Deletes event from calendar, using event name as key
    V = input('Please enter which event you would like to delete: ')
    global events
    del events[value=V]
    init_schedule()

def list_event():
    # Prints out all events saved into global events dict
    global events
    events.sort()
    for e in events:
        print('Event: {0} \n Time: {1}'.format(e[0], e[1]))
    init_schedule()


if __name__ == '__main__':
    main()



