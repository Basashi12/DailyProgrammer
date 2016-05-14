# Challenge 15 Easy
# https://www.reddit.com/r/dailyprogrammer/comments/q4c34/2242012_challenge_15_easy/
# Write a program to left or right justify a text file

# Somehow could not get ljust to work.  Used lstrip instead.

def justify(text):
    maxlen = len(max(open(text, 'r'), key=len))
    print(maxlen)
    side = input('Which margin should the text justify to? ').upper()
    if side == 'L':
        with open(text, 'r') as readfile:
            with open('Output.txt', 'w') as writefile:
                for line in readfile:
                    writefile.write(line.lstrip())
    elif side == 'R':
        with open(text, 'r') as readfile:
            with open('Output.txt', 'w') as writefile:
                for line in readfile:
                    newline = line.rjust(maxlen)
                    writefile.write(newline)
    else:
        print('Input Error')

