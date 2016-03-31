# Challenge No 9 Intermediate

def main():
    pass

def f_r():
    fn = input('Please input filename: ')
    sstring = input('Please input string to search: ')
    rstring = input('Please input string to replace: ')
    with open(fn, 'r') as f:
        filedata = f.read()
        filedata = filedata.replace(sstring, rstring)
    with open(fn, 'w') as f:
        f.write(filedata)

# To print line by line:
# with open('*.txt', 'r') as f:
#     for line in f:
#         print(line)

if __name__ == '__main__':
    main()
