# Challenge 15 Easy

def main():
    pass

def justify(text):
    maxlen = len(max(open(text, 'r'), key=len))
    print(maxlen)
    side = input('Which margin should the text justify to? ').upper()
    if side == 'L':
        with open(text, 'r') as readfile:
            with open('Output.txt', 'w') as writefile:
                for line in readfile:
                    newline = line.ljust(maxlen)    # somehow Ljust won't work
                    writefile.write(newline)
    elif side == 'R':
        with open(text, 'r') as readfile:
            with open('Output.txt', 'w') as writefile:
                for line in readfile:
                    newline = line.rjust(maxlen)
                    writefile.write(newline)
    else:
        print('Input Error')

