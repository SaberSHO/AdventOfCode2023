import numpy as np
import regex as re
import math as math
from collections import defaultdict
from itertools import cycle

with open('./Day8/input.txt') as f:
    lines = f.read().strip().split('\n')
    directionline = lines[0]
    networklist = [line.split('\n') for line in lines][2:]

network = defaultdict()
for networkline in networklist:
    network[networkline[0][:3]] = [networkline[0][7:10],networkline[0][12:15]]

directions = []
for char in directionline:
    if char == 'L':
        directions.append(0)
    else:
        if char == 'R':
            directions.append(1)
        else:
            print("How did we get here?")

dircycle = cycle(directions)

# Parsing out of the way, lets follow a pat
#nextnode = 'AAA'
#steps = 0
#
#while 1:
#    nextnode = network.get(nextnode)[next(dircycle)]
#    steps +=1
#    if nextnode == 'ZZZ':
#        break

#print(steps)

#steps = -1
#nextnodes = {key: val for key,val in network.items() if key.endswith('A')}
#while 1:
#    tempdict = defaultdict()
#    dirtemp = next(dircycle)
#    for node in nextnodes.items():
#        tempdict[node[0]] = network.get(node[0])[dirtemp]
#    steps +=1
#    found = {key: val for key,val in tempdict.items() if key.endswith('Z')}
#    if len(found) == len(tempdict):
#        break
#    nextnodes = {key:val for key,val in network.items() if key in tempdict.values()}
#    print(steps)    

#print(steps)

allsteps = []
steps = -1
nextnodes = ['AAA'] #[key for key,val in network.items() if key.endswith('A')]
visitednodes = defaultdict()

for nextnode in nextnodes:
    tempcycle = cycle(directions)
    steps = 0
    currentstart = nextnode
    visitednodes[currentstart] = []
    while 1:
        print(nextnode)
        nextnode = network.get(nextnode)[next(tempcycle)]
        steps +=1
        visitednodes[currentstart] = visitednodes[currentstart].append(nextnode) 
        if nextnode.endswith('Z'):
           break
    print(steps)    

print(listofnodes)
#stepsarr = np.array([step for step in allsteps])
#multiple = np.lcm.reduce(stepsarr)
#print(multiple)