import numpy as np
import regex as re
import math as math

with open('./Day6/sampleinput.txt') as f:
    lines = f.read().strip().split('\n')
    line = [line.split(': ')[1] for line in lines]
    time = list(map(int,re.findall('\d+',line[0])))
    distance = list(map(int,re.findall('\d+',line[1])))

# x = hold button
# y = total time
# distance(x,y) = x*(y-x) = xy - x2
def distancefunc(x,y):
    distance = int(x*y - pow(x,2))
    return distance

# part1
winners = []
for t,d in zip(time, distance):
    y = t
    winning = 0
    for x in range(0,y):
        disttest = distancefunc(x,y)
        if disttest > d:
            winning += 1
    winners.append(winning)

print(math.prod(winners))

# part2
t = time2 = int("".join(map(str,time)))
print(time2)
d =distance2 = int("".join(map(str,distance)))
print(distance2)

# BRUTE FORCE METHOD
winning = 0
for x in range(0,time2):
    disttest = distancefunc(x,time2)
    if disttest > distance2:
        winning += 1
print(winning)

#LETS BE SMART
## this doenst work, will look at later

b2m4ac = (t**2) - (4*-1*d)
sol1 = (-t-math.sqrt(b2m4ac))/(2)
sol2 = (-t+math.sqrt(b2m4ac))/(2)
print(sol1)
print(sol2)

print(distancefunc(math.floor(sol2),9))