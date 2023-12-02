import regex as re

file = open("./Day2/input.txt",'r')

sum = 0

maxred = 12
maxgreen = 13
maxblue = 14

regexgameid = 'Game (\d+)'
regexred = '(\d+) red'
regexblue = '(\d+) blue'
regexgreen = '(\d+) green'

while True:
    line = file.readline()
    if not line:
        break
    
    red = 0
    blue = 0
    green = 0
    possible = []
    gameidsplit = line.split(':')
    gameid = (re.findall(regexgameid,gameidsplit[0]))[0]
    gamesinid = gameidsplit[1].split(';')
    for game in gamesinid:
        redmatch = re.findall(regexred, game)
        if redmatch:
            red = redmatch[0]
        bluematch = re.findall(regexblue, game)
        if bluematch:
            blue = bluematch[0]
        greenmatch = re.findall(regexgreen, game)
        if greenmatch:
            green = greenmatch[0]

        if (int(red) <= maxred and int(blue) <= maxblue and int(green) <= maxgreen):
            possible.append(True)
        else:
            possible.append(False)

    if (all(possible)):
        print('Game '+ str(gameid)+ ' is possible')
        sum = sum + int(gameid)
    else:
        print('Game '+ str(gameid)+ ' is NOT possible')

print('Sum: ' + str(sum))

