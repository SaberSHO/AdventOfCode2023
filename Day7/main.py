import numpy as np
import regex as re
import math as math
from collections import defaultdict

with open('./Day7/input.txt') as f:
    lines = f.read().strip().split('\n')
    hands = [line.split(' ') for line in lines]

card_order_dict = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10,"J":1, "Q":12, "K":13, "A":14}
def subJoker(value_count):
    if value_count['J'] > 0:
        ##EDGE CASE OF NATURAL 5 OF A KIND OF J
        if sorted(value_count.values()) == [5]:
            return value_count
        tempJ = value_count['J']
        del value_count['J']
        value_count[max(value_count,key=value_count.get)] += tempJ
        return value_count
    else:
        del value_count['J']
        return value_count

def check_five_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    value_counts = subJoker(value_counts)
    if sorted(value_counts.values()) == [5]:
        return True
    return False

def check_four_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    value_counts = subJoker(value_counts)
    if sorted(value_counts.values()) == [1,4]:
        return True
    return False

def check_full_house(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    value_counts = subJoker(value_counts)
    if sorted(value_counts.values()) == [2,3]:
        return True
    return False


def check_three_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    value_counts = subJoker(value_counts)
    if set(value_counts.values()) == set([3,1]):
        return True
    else:
        return False

def check_two_pairs(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    value_counts = subJoker(value_counts)
    if sorted(value_counts.values())==[1,2,2]:
        return True
    else:
        return False

def check_one_pairs(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    value_counts = subJoker(value_counts)
    if 2 in value_counts.values():
        return True
    else:
        return False
    
def getStrength(hand):
    if check_five_of_a_kind(hand):
        return 6
    if check_four_of_a_kind(hand):
        return 5
    if check_full_house(hand):
        return 4
    if check_three_of_a_kind(hand):
        return 3
    if check_two_pairs(hand):
        return 2
    if check_one_pairs(hand):
        return 1
    else:
        return 0

for hand in hands:
    print(hand)
    ##evaluate type and calculate strength and append it to list
    strength = getStrength(hand[0])
    hand.append(strength)

## Sort by rank order
# First sort by the last card in the hand, then the 4th, 3rd, 2nd, 1st. As Python list.sort() always maintain order, we are sorting the hand rank ascending (ignoring strength for now)
# finally sort by the hand strength. again, list ordering saves us here by keeping the hand strength order
hands.sort(key=lambda x: card_order_dict[x[0][4]])
hands.sort(key=lambda x: card_order_dict[x[0][3]])
hands.sort(key=lambda x: card_order_dict[x[0][2]])
hands.sort(key=lambda x: card_order_dict[x[0][1]])
hands.sort(key=lambda x: card_order_dict[x[0][0]])
hands.sort(key=lambda x: x[2])

print(hands)

totalwinnings = 0
for i in range(0,len(hands)):
    totalwinnings += int(hands[i][1]) * (i+1)

print(totalwinnings)