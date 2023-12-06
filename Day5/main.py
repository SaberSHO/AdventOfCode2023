import numpy as np

def lookupmap (source,maplist):
    for m in maplist:
        if source in range(m[1],m[1]+m[2]):
           return m[0] + (source - m[1])        
    return source

with open('./Day5/sampleinput.txt') as f:
    input = f.read().strip().split('\n')
    cleaninput = [i for i in input if i]

splitlist = []
sublist = []

separators = ('seed-to-soil map:', 'soil-to-fertilizer map:','fertilizer-to-water map:','water-to-light map:','light-to-temperature map:','temperature-to-humidity map:','humidity-to-location map:')

for x in cleaninput[1:]:
    if x in separators:
        if sublist:
            splitlist.append(sublist)
        sublist = []
    else:
        sublist.append(x)
splitlist.append(sublist)

seeds = list(map(int,cleaninput[0].split(': ')[1].split()))
s2s = [i.split() for i in splitlist[0]]
seed2soil = [[int(j) for j in i] for i in s2s]
s2f = [i.split() for i in splitlist[1]]
soil2fertilizer= [[int(j) for j in i] for i in s2f]
f2w = [i.split() for i in splitlist[2]]
fertilizer2water = [[int(j) for j in i] for i in f2w]
w2l = [i.split() for i in splitlist[3]]
water2light= [[int(j) for j in i] for i in w2l]
l2t = [i.split() for i in splitlist[4]]
light2temp= [[int(j) for j in i] for i in l2t]
t2h = [i.split() for i in splitlist[5]]
temp2humidity = [[int(j) for j in i] for i in t2h]
h2l = [i.split() for i in splitlist[6]]
humidity2location= [[int(j) for j in i] for i in h2l]

locations = []
for seed in seeds:
    soil = lookupmap(seed,seed2soil)
    fertilizer = lookupmap(soil,soil2fertilizer)
    water = lookupmap(fertilizer,fertilizer2water)
    light = lookupmap(water, water2light)
    temp = lookupmap(light,light2temp)
    humidity = lookupmap(temp,temp2humidity)
    location = lookupmap(humidity,humidity2location)

    locations.append(location)
    
print(min(locations))


def lookupmapranges (sources,maplist):
    newranges = []
    for source in sources:
        for m in maplist:
            if source[0] in range(m[1],m[1]+m[2]):
                if source[-1] in range(m[1],m[1]+m[2]):
                    newrange = range(m[0] + source[0] - m[1], m[0] + source[0] - m[1] + len(source))
                    print(newrange)
                    newranges.append(range(m[0] + source[0] - m[1], m[0] + source[0] - m[1] + len(source)))
                else:
                    #uh oh, we have to split a range, first get the beginning chunk
                    newranges.append(range(m[0] + source[0] - m[1], m[0] + m[2]))
                    newranges.append(range(source[-1] - m[2],source[-1] + 1))
    if len(newranges) == 0:
        newranges.append(range(source[0],source[-1]+1))
    print(newranges)
    return newranges

#seedstemp = range(55,68)
seedstemp = []
for s in range(0,len(seeds),2):
    seedstemp.append(range(seeds[s],seeds[s]+seeds[s+1]))
soilranges = []
fertilizerranges = []
waterranges = []
lightranges = []
tempranges = []
humidityranges = []
locationranges = []

for seedrange in seedstemp:
    soilranges += lookupmapranges([seedrange],seed2soil)
    fertilizerranges += lookupmapranges(soilranges,soil2fertilizer)
    waterranges += lookupmapranges(fertilizerranges,fertilizer2water)
    lightranges += lookupmapranges(waterranges,water2light)
    tempranges += lookupmapranges(lightranges,light2temp)
    humidityranges += lookupmapranges(tempranges,temp2humidity)
    locationranges += lookupmapranges(humidityranges,humidity2location)

print(locationranges)
#### HAHAHA, this might work, but its killing my computer! need to find more efficient solution
#seedstemp = []
#locations2 = []
#for s in range(0,len(seeds),2):
#    seedstemp.append(i for i in range(seeds[s],seeds[s]+seeds[s+1]))
#
#seeds2 = (j for i in seedstemp for j in i)
#
#for seed in seeds2:
#    soil = lookupmap(seed,seed2soil)
#    fertilizer = lookupmap(soil,soil2fertilizer)
#    water = lookupmap(fertilizer,fertilizer2water)
#    light = lookupmap(water, water2light)
#    temp = lookupmap(light,light2temp)
#    humidity = lookupmap(temp,temp2humidity)
#    location = lookupmap(humidity,humidity2location)
#
#    locations2.append(location)
#    
#print(min(locations2))

##### Lets work backwards, find minimum location range and work backwards.
### DEST START, SOURCE START, RANGE
# max the source can be to minimize the dest

#minlocation = list(range(0,min([locs[0] for locs in humidity2location])+1))
#minhumidity = list(range(0,min([locs[0] for locs in temp2humidity])+1))
#mintemp = list(range(0,min([locs[0] for locs in light2temp])+1))
#minlight = list(range(0,min([locs[0] for locs in water2light])+1))
#minwater = list(range(0,min([locs[0] for locs in fertilizer2water])+1))
#minfertilizer = list(range(0,min([locs[0] for locs in soil2fertilizer])+1))
#minsoil = list(range(0,min([locs[0] for locs in seed2soil])+1))

#locationmaxrange = min([(i[0],i[1]+i[2]-1) for i in humidity2location]) #for each line in h2l, return the dest start and the source start + range, then mimize on dest start
#humiditymaxrange = min([(i[0],i[1]+i[2]-1) for i in temp2humidity])
#tempmaxrange = min([(i[0],i[1]+i[2]-1) for i in light2temp])
#lightmaxrange = min([(i[0],i[1]+i[2]-1) for i in water2light])
#watermaxrange = min([(i[0],i[1]+i[2]-1) for i in fertilizer2water])
#fertilizermaxrange = min([(i[0],i[1]+i[2]-1) for i in soil2fertilizer])
#soilmaxrange = min([(i[0],i[1]+i[2]-1) for i in seed2soil])
###
#location = lookupmap(695457243, humidity2location)

###
#seedstemp = []
#for s in range(0,len(seeds),2):
#    seedstemp.append(i for i in range(seeds[s],seeds[s]+seeds[s+1]))


#possibleseeds = []
#for seed in seeds:
#    if seed in range(soilmaxrange[0],soilmaxrange[1]):
#        possibleseeds.append(seed)


#locations = []
#for seed in seedstemp[1]:
#    soil = lookupmap(seed,seed2soil)
#    fertilizer = lookupmap(soil,soil2fertilizer)
#    water = lookupmap(fertilizer,fertilizer2water)
#    light = lookupmap(water, water2light)
#    temp = lookupmap(light,light2temp)
#    humidity = lookupmap(temp,temp2humidity)
#    location = lookupmap(humidity,humidity2location)
#
#    locations.append(location)
#    
#print(min(locations))
