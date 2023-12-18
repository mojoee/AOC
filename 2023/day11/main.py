import numpy as np
from collections import defaultdict
with open("day11/input.txt") as file:
    data = file.read().splitlines()

print(data)
arr = np.array(data) 
print(arr)
r = len(data)
c = len(data[0])

universe = np.zeros((r, c))
galaxies = []
for i, row in enumerate(arr):
    for j, char in enumerate(row):
        if char=="#":
            galaxies.append((i, j))

for galaxy in galaxies:
    universe[galaxy[0]][galaxy[1]]=1
print(universe)

# adjust the map
n = 999999
counter = 0
for i, row in enumerate(universe):
    if 1. not in row:
        counter += n
        universe = np.insert(universe, i, 0, axis=0)
        new_galaxies = []
        for galaxy in galaxies:
            if galaxy[0] > (i+counter-n):
                new_galaxies.append((galaxy[0]+n, galaxy[1]))
            else:
                new_galaxies.append(galaxy)
        galaxies = new_galaxies
counter = 0
for j, column in enumerate(universe.T):
    if 1. not in column:
        counter += n
        universe = np.insert(universe, j, 0, axis=1)
        new_galaxies = []
        for galaxy in galaxies:
            if galaxy[1] > (j+counter-n):
                new_galaxies.append((galaxy[0], galaxy[1]+n))
            else:
                new_galaxies.append(galaxy)
        galaxies = new_galaxies

# update galaxies    
# galaxies = []
# for i, row in enumerate(universe):
#     for j, char in enumerate(row):
#         if char==1.:
#             galaxies.append((i, j))
print(galaxies)
print(universe)
distances = defaultdict(lambda: float('inf'))
for i, galaxy in enumerate(galaxies):
    for j, galaxy2 in enumerate(galaxies):
        # exclude own distance
        if i==j:
            continue
        distance = abs(galaxy[0]-galaxy2[0])+abs(galaxy[1]-galaxy2[1])
        if (j, i) in distances.keys():
            continue
        distances[i, j] = distance

print(sum(distances.values()))