def tri(h):
    option = input('Would you like the triangle (n)ormal, (u)pside down, or (r)ight justified? ')
    if option.lower() == 'n':
        i = 0
        while i < h:
            print('@' * (2**i))
            i +=1
    elif option.lower() == 'u':
        i = h - 1
        while i >= 0:
            print('@' * (2**i))
            i -= 1
    elif option.lower() == 'r':
        width = 2**(h-1)
        i = 0
        while i < h:
            ats = '@' * (2**i)
            lineout = ats.rjust(width)
            print(lineout)
            i += 1
    else:
        print('Invalid input')
