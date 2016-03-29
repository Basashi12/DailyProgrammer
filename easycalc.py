# https://www.reddit.com/r/dailyprogrammer/comments/pjbj8/easy_challenge_2/
# let's calculate financial ratios

def main():
    pass

def PBR(marketcap, bv):
    return marketcap / bv

def PER(marketcap, earnings):
    return marketcap / earnings

def PS(marketcap, sales):
    return marketcap / sales

def get_input():
    global MC, EE, BOOK, REV
    MC = int(input('Enter market capitalization of the firm you would like to analyze: '))
    EE = int(input('Enter an estimate for net profit this year: '))
    BOOK = int(input('Enter the book value of the firm: '))
    REV = int(input('Enter sales/revenue figure for this FY: '))
    calc()

def calc():
    choice = input('What ratio would you like to compute?\n(1) PER, (2) PBR, or (3) PS? ')

    if choice == '1' or choice == 'PER':  # if/elif statements need separate 'or' - cannot say choice == '1' or 'PER'
        print('Price earnings ratio is: ', PER(MC, EE))
    elif choice == '2' or choice == 'PBR':
        print('Price to book ratio is: ', PBR(MC, BOOK))
    elif choice == '3' or choice == 'PS':
        print('Price to sales ratio is: ', PS(MC, REV))
    else:
        print('Invalid input')
        calc()

if __name__ == '__main__':
    get_input()
