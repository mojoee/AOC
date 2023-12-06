import math

with open ("day5/input.txt", "r") as myfile:
    data = myfile.read().splitlines()

def pairwise(t):
    it = iter(t)
    return zip(it,it)

counter = -1
# get the mappings
mappingNames = ["seed2soil", "soil2fertilizer", "fertilizer2water", 
            "water2light", "light2temperature", "temperature2humidity", 
            "humidity2location"]
mappings = [[], [], [], [], [], [], []]
lvl2 = True
for line in data:
    if line.startswith("seeds:"):
        seedNumbers = line.split(' ')[1:]
        if lvl2:
            seedNumbers = pairwise(seedNumbers)
    elif line == '':
        counter += 1
    elif line[0].isnumeric():
        destinationStart, sourceStart, n = [int(x) for x in line.split(' ')]
        mapvalue = destinationStart-sourceStart
        end = sourceStart + n - 1
        mappings[counter].append((sourceStart, end, mapvalue))

minNumber = float('inf')
seedchosen = 0
a,b = 180532143, 331672682
#a=3416930225
#b=56865175
for n in range(a, b):
    for mapping in mappings:
        for triple in mapping:
            if n >= triple[0] and n <= triple[1]:
                n += triple[2]
                break
    if n < minNumber:
        minNumber = n
        chosen = triple[0]
        chosen2 = triple[1]
        chosen3 = triple[2]



print(minNumber)
print(chosen, chosen2)