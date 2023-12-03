import regex as re
import numpy as np

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
print(matrix)

file = open("./Day3/input.txt",'r')
sum = 0
regex = '(\d+)'
special_characters = "!@#$%^&*()-+?_=,<>/"


lineIndex = 0
while True:
    line = file.readline()
    if not line:
        break
    match = re.finditer(regex,line)
    for m in match:
        print(str(m.span()) + str(m.group()))
        position = (lineIndex,m.start())
        print (position)
        alladjacent = adj_finder(matrix,position,m.end()-m.start())
        print(alladjacent)
        if(any(matrix[adjacent] in special_characters for adjacent in alladjacent)):
            sum = sum + int(m.group())
            print('yes! new sum = ' + str(sum))
    lineIndex += 1

print(sum)



