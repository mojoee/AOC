
with open ("day6/input.txt", "r") as myfile:
    data = myfile.read().splitlines()

part1 = False
times = []
distances = []
for line in data:
    if line.startswith("Time:"):
        chunks = line.split(' ')
        for chunk in chunks:
            if chunk.isnumeric():
                times.append(chunk)
    if line.startswith("Distance:"):
        chunks = line.split(' ')
        for chunk in chunks:
            if chunk.isnumeric():
                distances.append(chunk)

if part1 == True:
    possibilities = 1
    for time, distance in zip(times, distances):
        poss = 0
        for i in range(time+1):
            traveled = (time-i)*i
            if traveled > distance:
                poss += 1

        if poss > 0:
            possibilities *= poss

    print(possibilities)    

times = int("".join(times))
distances = int("".join(distances))
possibilities = 1

start = float("-inf")
stop = float("inf")
for i in range(times+1):
    traveled = (times-i)*i
    if traveled > distances and start==float("-inf"):
        start = i
        break
for i in range(times, 0, -1):
    traveled = (times-i)*i
    if traveled > distances and stop == float("inf"):
        stop = i
        break

result = stop-start+1
print(start)
print(stop)
print("result:", result)