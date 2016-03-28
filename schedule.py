import sys

def main():
    pass

events = {}

add_event():
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
    V = input('Please enter which event you would like to delete: ')
    global events
    events.pop(keys=V)

list_event():
    global events
    events.sort()
    for e in events:
        print('Event: {0} \n Time: {1}'.format(e[0], e[1]))


if __name__ = '__main__':
    main()


