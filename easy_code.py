#  Challenge No. 3 Easy
#  https://www.reddit.com/r/dailyprogrammer/comments/pkwb1/2112012_challenge_3_intermediate/

import codecs

def main():
    pass

def start():
    print('Welcome to the not so secret coder, using a basic Casesar Cipher.')
    print('Would you like to encode or decode a message?')
    ri = input('Enter E to encode and D to decode: ')
    if ri == 'E':
        encode()
    elif ri == 'D':
        decode()
    else:
        print('Invalid input.\n')
        start()

def encode():
    print('Please enter the message you would like to encode: ')
    phrase = input('> ')
    print('Encoding the message...\n')
    scrambled = codecs.encode(phrase, 'rot_13')
    print(scrambled)

def decode():
    print('Please enter the encoded message to decode: ')
    garble = input('> ')
    print('Decoding the message...\n')
    unscrambled = codecs.decode(garble, 'rot_13')
    print(unscrambled)

if __name__ == '__main__':
    main()
