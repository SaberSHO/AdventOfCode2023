import regex as re

file = open("./Day2/input.txt",'r')

sum = 0

regexgameid = 'Game (\d+)'
regexred = '(\d+) red'
regexblue = '(\d+) blue'
regexgreen = '(\d+) green'

power = 0

while True:
    line = file.readline()
    if not line:
        break
    
    redarray = []
    greenarray = []
    bluearray = []
    
    gameidsplit = line.split(':')
    gameid = (re.findall(regexgameid,gameidsplit[0]))[0]
    gamesinid = gameidsplit[1].split(';')
    for game in gamesinid:
        redmatch = re.findall(regexred, game)
        if redmatch:
            redarray.append(int(redmatch[0]))
        bluematch = re.findall(regexblue, game)
        if bluematch:
            bluearray.append(int(bluematch[0]))
        greenmatch = re.findall(regexgreen, game)
        if greenmatch:
            greenarray.append(int(greenmatch[0]))

    minred = max(redarray)
    minblue = max(bluearray)
    mingreen = max(greenarray)
    power = power + (int(minred) * int(minblue) * int(mingreen))

print('Sum: ' + str(power))

