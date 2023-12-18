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
x_coordinates = []
y_coordinates = []
while not_finished:
    x_coordinates.append(start_coords[0])
    y_coordinates.append(start_coords[1])
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
    # arr[next_coords[0]][next_coords[1]] = 1
print(distance/2)


# part 2

def shoelace_formula(x_coords, y_coords):
    """
    Calculate the area of a polygon using the Shoelace Formula.

    Parameters:
    - x_coords: List of x-coordinates of vertices.
    - y_coords: List of y-coordinates of vertices.

    Returns:
    - Area of the polygon.
    """
    n = len(x_coords)

    # Check if the number of x-coordinates is equal to the number of y-coordinates
    if n != len(y_coords):
        raise ValueError("Number of x-coordinates must be equal to the number of y-coordinates.")

    # Apply the Shoelace Formula
    area = 0.5 * abs(sum(x_coords[i] * y_coords[(i + 1) % n] - x_coords[(i + 1) % n] * y_coords[i] for i in range(n)))

    return area

area = shoelace_formula(x_coordinates, y_coordinates)
print("Area of the polygon:", area)
interiorPoints = area - distance/2 + 1
print(interiorPoints)