# Challenge 25 Easy
# https://www.reddit.com/r/dailyprogrammer/comments/qxuug/3152012_challenge_25_easy/

# Enter votes as dict { 'Candidate':votes }

def votecount(votes):
    totalvotes = 0
    for num in votes.values():
        totalvotes += num
    print(totalvotes)
    for num in votes.values():        
        if num / totalvotes > .5:
            print('We have a winner!')
            print(list(votes.keys())[list(votes.values()).index(num)])
            break
        else:
            print('No winner, yet')
