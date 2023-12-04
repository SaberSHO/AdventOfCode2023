import numpy as np

with open('./Day4/input.txt') as f:
    cards = f.read().strip().split('\n')
    cards = [card.split(': ')[1] for card in cards]
    cards = [card.split(' | ') for card in cards]

points = 0
totalrewards = [1] * len(cards)

for card in range(len(cards)):
    matches = 0
    winning = cards[card][0].split()
    my = cards[card][1].split()
    matches = set(winning) & set(my)
        
    if len(matches)>0:
        points += int(np.power(2,len(matches)-1))
        for reward in range(card, card+len(matches)):
            if reward+1 < len(cards):
                totalrewards[reward+1] += totalrewards[card]

totalrewardssum = sum(totalrewards)        
print(points)
print(totalrewardssum)
