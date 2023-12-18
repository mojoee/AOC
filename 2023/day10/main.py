import numpy
with open("day10/input.txt") as file:
    data = file.read().splitlines()

print(data)
arr = numpy.array(data) 
print(arr)

# find S
for i, row in enumerate(arr):
    for j, char in enumerate(row):
        if char == "S":
            print(i, j)

# 25, 77
# look for a piece close by:
print(arr[24:26][26:28])
distance = 0
start_coords = (25, 77)
next_coords = (24, 77)
not_finished = True
while not_finished:
    direction = arr[next_coords[0]][next_coords[1]]
    sodNorthSouth = next_coords[0]-start_coords[0]
    sodEastWest = next_coords[1]-start_coords[1]
    start_coords = next_coords
    # connect north and south
    if direction == "|":
        next_coords = (next_coords[0]+sodNorthSouth, next_coords[1])
    # connect north and south
    if direction == "-":
        next_coords = (next_coords[0], next_coords[1]+sodEastWest)
    # connect south and east
    elif direction == "F":
        next_coords = (next_coords[0]-sodEastWest, next_coords[1]-sodNorthSouth)
    # connect north and east
    elif direction == "L":
        next_coords = (next_coords[0]+sodEastWest, next_coords[1]+sodNorthSouth)
    # connect south and west
    elif direction == "7":
        # if sodEastWest == 1:
        #     next_coords = (next_coords[0]+1, next_coords[1])
        # if sodNorthSouth == -1:
        #     next_coords = (next_coords[0], next_coords[1]-1)
        next_coords = (next_coords[0]+sodEastWest, next_coords[1]+sodNorthSouth)
    # connect north and west
    elif direction == "J":
        next_coords = (next_coords[0]-sodEastWest, next_coords[1]-sodNorthSouth)
    elif direction == "S":
        not_finished = False
    distance += 1
print(distance/2)