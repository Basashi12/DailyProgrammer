# Challenge No 7 Easy - wasn't that easy

def main():
    pass

# Dict to encode
mc = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ' ':'/'}

# Reversing dict to decode
rmc = dict(list(zip(mc.values(), mc.keys())))

def inquire():
    ri = input('Would you like to decode or encode a message in Morse code? ').lower()
    if ri == 'encode':
        encode()
    elif ri == 'decode':
        decode()
    else:
        print('Try again.')
        inquire()

def decode():
    phrase = input('Enter phrase to decode: ')
    coded = phrase.split()
    decoded = ''
    for morse in coded:
        bit = str(rmc.get(morse))
        decoded += bit
    print(decoded)

def encode():
    ph = input('Enter phrase to encode: ').upper()
    english = list(ph)
    encoded = ''
    for alpha in english:
        bit = str(mc.get(alpha)) + ' '
        encoded += bit
    print(encoded)        
        
if __name__ == '__main__':
    main()
