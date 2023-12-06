import numpy as np

def lookupmap (source,maplist):
    for m in maplist:
        if source in range(m[1],m[1]+m[2]):
           return m[0] + (source - m[1])        
    return source

with open('./Day5/input.txt') as f:
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
    for m in maplist:
        source_start = m[1]
        source_end = m[1]+m[2]
        destination_start = m[0]

        tempranges = []
        while sources:
            tempsource = sources.pop()
            left = (tempsource[0],min(tempsource[-1],source_start))
            mid = (max(tempsource[0],source_start),min(source_end,tempsource[-1]))
            right = (max(source_end, tempsource[0]),tempsource[-1])

            if left[-1] > left[0]:
                tempranges.append(left)
            if mid[-1] > mid[0]:
                newranges.append((mid[0]-source_start+destination_start,mid[1]-source_start+destination_start))
            if right[-1] > right[0]:
                tempranges.append(right)
        sources = tempranges
    return newranges + tempranges

seedstemp = []
for s in range(0,len(seeds),2):
    seedstemp.append((seeds[s],seeds[s]+seeds[s+1]))
soilranges = []
fertilizerranges = []
waterranges = []
lightranges = []
tempranges = []
humidityranges = []
locationranges = []
result= []

for seedrange in seedstemp:
#    print('Seed Range' + str(seedrange))
    soilranges += lookupmapranges([seedrange],seed2soil)
#   print('Soil Ranges' + str(soilranges))
    fertilizerranges += lookupmapranges(soilranges,soil2fertilizer)
#    print('Fertilizer Ranges' + str(fertilizerranges))
    waterranges += lookupmapranges(fertilizerranges,fertilizer2water)
#    print('Water Ranges' + str(waterranges))
    lightranges += lookupmapranges(waterranges,water2light)
#    print('Light Ranges' + str(lightranges))
    tempranges += lookupmapranges(lightranges,light2temp)
#    print('Temp Ranges' + str(tempranges))
    humidityranges += lookupmapranges(tempranges,temp2humidity)
#    print('Humidity Ranges' + str(humidityranges))
    locationranges += lookupmapranges(humidityranges,humidity2location)
#    print('Location Ranges' + str(locationranges))

print(min([x[0] for x in locationranges]))

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
