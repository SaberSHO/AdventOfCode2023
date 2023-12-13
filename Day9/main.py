import numpy as np
import regex as re
import math as math
from collections import defaultdict
from itertools import cycle

sequences = []
with open('./Day9/sampleinput.txt') as f:
    lines = f.read().strip().split('\n')
    for line in lines:
        sequences.append([int(i) for i in line.split()])


def calcDiff(s):
    s_new = []
    for i in range(0,len(s)-1):
        s_new.append(s[i+1]-s[i])
    return s_new

def calcNextVal(s):
    for i,e in reversed(list(enumerate(s))):
        nextVal = e[-1]
        s[i-1].append(s[i-1][-1]+nextVal)
    return e
    
sum = 0
for seq in sequences:
    fullseq = []
    while 1:
        fullseq.append(seq)
        new_s = calcDiff(seq)
        #print(new_s)
        if all(ele == new_s[0] for ele in new_s):
            fullseq.append(new_s)
            break
        else:
            seq = new_s
    #print(fullseq)
    nextVal = calcNextVal(fullseq)[-1]
    #print(nextVal)
    sum = sum+nextVal

print(sum)

def calcPrevVal(s):
    for i,e in reversed(list(enumerate(s))):
        prevVal = e[0]
        s[i-1].insert(0,s[i-1][0]-prevVal)
    return e

sum = 0
for seq in sequences:
    fullseq = []
    while 1:
        fullseq.append(seq)
        new_s = calcDiff(seq)
        #print(new_s)
        if all(ele == new_s[0] for ele in new_s):
            fullseq.append(new_s)
            break
        else:
            seq = new_s
    #print(fullseq)
    nextVal = calcPrevVal(fullseq)[0]
    print(nextVal)
    #sum = sum+nextVal
print(sum)