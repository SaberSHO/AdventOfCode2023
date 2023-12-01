import regex as re
from word2number import w2n

file = open("./Day1/input.txt",'r')

sum = 0
regex = '(?:zero|one|two|three|four|five|six|seven|eight|nine)|\d'

while True:
    line = file.readline()
    if not line:
        break
    
    
    listofnumbers = re.findall(regex,line, overlapped=True)
    stringlistofnumbers = ''
    for word in listofnumbers:
        stringlistofnumbers = stringlistofnumbers + str(w2n.word_to_num(word))

                                

    firstnumber = stringlistofnumbers[0]
    lastnumber = stringlistofnumbers[-1]
    finalnumber = int(str(firstnumber)+str(lastnumber))
    
    print(line + '   ' + str(listofnumbers) + '   ' + firstnumber + lastnumber)

    sum = sum + finalnumber
print (sum)
