import random, string

def main():
    pass

def create_pw():
    qty = int(input('How many passwords would you like to generate? '))
    print('Algorithm will generate {} passwords.'.format(qty))
    length = int(input('How long should the passwords be? '))
    print('The passwords will be {} letters long.'.format(length))
    pw_list = []
    chars = string.ascii_letters + string.digits + string.punctuation
    for _ in range(qty):
        pw_list.append(''.join(random.sample(chars, length)))
    print(pw_list)

if __name__ == '__main__':
    main()

