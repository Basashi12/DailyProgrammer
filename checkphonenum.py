# Challenge 10 Easy
# https://www.reddit.com/r/dailyprogrammer/comments/pv98f/2182012_challenge_10_easy/
# Validate given numbers as real telephone numbers

import re

def main():
    pass

# nos is a list of numbers to be checked
nos = '1234567890', '123-456-7890', '123.456.7890', '(123)456-7890', '(123) 456-7890', '456-7890', '123-45-6789', '123:4567890', '123/456-7890', '555-1313', '212 664 7665'

# patterns are regex patterns for valid numbers
patterns = r'\d{10}', r'\d{3}-\d{3}-\d{4}', r'\d{3}\.\d{3}\.\d{4}', r'\(\d{3}\)\d{3}-\d{4}', r'\(\d{3}\)\s\d{3}-\d{4}', r'\d{3}-\d{4}', r'\d{3}\s\d{3}\s\d{4}'

def validate(nos):
    # initialize list for valid numbers
    valnum = []
    for num in nos:
        for pat in patterns:
            pattern = re.compile(pat)
            if pattern.match(num):  # re.match returns match (which is True) or None.  Not a boolean.
                print ('{} is a validated phone number.'.format(num))
                # if number checks out, add to valnum list
                valnum.append(num)
            else:
                pass
        if num not in valnum:
            print('{} is not a validated phone number.'.format(num))
    # summary of output
    print('{} out of {} phone number(s) have been validated by the system.'.format(len(valnum), len(nos)))
            
    
if __name__ == '__main__':
    main()
