import regex as re
import numpy as np
from collections import defaultdict

def adj_finder(matrix, position, distance):
    adj = []
    
    for dx in range(-1, 2):
        for dy in range(-1, 1+distance):
            rangeX = range(0, matrix.shape[0])  # X bounds
            rangeY = range(0, matrix.shape[1])  # Y bounds
            
            (newX, newY) = (position[0]+dx, position[1]+dy)  # adjacent cell
            
            if (newX in rangeX) and (newY in rangeY) and (dx, dy) != (0, 0):
                adj.append((newX, newY))
    
    return adj


file = open("./Day3/input.txt",'r')
matrix =  np.matrix([list(singleline.strip()) for singleline in file])

file = open("./Day3/input.txt",'r')

sum = 0
regex = '(\d+)'
special_characters = "*"
arrayOfPossibles = []
lineIndex = 0

while True:
    line = file.readline()
    if not line:
        break
    match = re.finditer(regex,line)
    for m in match:
        position = (lineIndex,m.start())
        alladjacent = adj_finder(matrix,position,m.end()-m.start())
        for adjacent in alladjacent:
            if matrix[adjacent] == '*':
                arrayOfPossibles.append([(m.group()),str(adjacent)])
    lineIndex += 1
    
totals = defaultdict(list)
for v,k in arrayOfPossibles:
    print('K = ' + str(k)+ '   V = '+ str(v))
    totals[k] += [int(v)]


for k in totals:
    if len(totals[k]) > 1:
        sum = sum + np.prod(totals[k])

print(sum)



