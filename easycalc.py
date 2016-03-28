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
    marketcap = input('Enter market capitalization of the firm you would like to analyze: ')
    earnings = input('Enter an estimate for net profit this year: ')
    bv = input('Enter the book value of the firm: ')
    sales = input('Enter sales/revenue figure for this FY: ')
    calculate()

def calculate():
    choice = input('What ratio would you like to compute?\n(1) PER, (2) PBR, or (3) PS?')

    if choice == '1' or 'PER':
        print(PER(marketcap, earnings))
    elif choice == '2' or 'PBR':
        print(PBR(marketcap, bv))
    elif choice == '3' or 'PS':
        print(PS(marketcap, sales))
    else:
        print('Invalid input')
        calculate()

if __name__ == '__main__':
    get_input()
