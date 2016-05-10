# Challenge No 5 medium
# https://www.reddit.com/r/dailyprogrammer/comments/pnhtj/2132012_challenge_5_intermediate/
# write a program that can find the amount of anagrams within a .txt file


def main():
    pass

def read_words():
    # function to read in file - os.chdir() for correct dir
    fname = input('filename: ')
    # wordlist will be used by find_anagrams
    global wordlist
    wordlist = []
    tf = open(fname)
    for word in tf.read().split():
        wordlist.append(word.lower())
    wordlist = list(set(wordlist)) # removes duplicates
    return wordlist
    
def find_anagrams(wordlist):
    anagrams = []
    for w in wordlist:
        for z in wordlist:
            if len(w) != len(z): # filtering out words with diff len
                continue
            elif sorted(w) != sorted(z): # filtering out words composed of different letters
                continue
            elif w == z: # deleting same words - will happen once per loop
                continue
            else:
                anagrams.extend([w, z]) # adding all other words
    anagrams = list(set(anagrams)) # remvoving duplicate words - not sure if necessary
    print(len(anagrams)) #generates a weird number
    print(anagrams)

if __name__ == '__main__':
    main()
