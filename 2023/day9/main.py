def findZeroRow(line, rows=[]):
    difference = []
    for i in range(len(line)-1):
        difference.append(line[i+1] - line[i])
    rows.append(difference)
    if all(v == 0 for v in difference):
        return rows
    else:
        return findZeroRow(difference, rows)

with open("day9/input.txt") as file:
    data = file.read().splitlines()

total = 0
for line in data:
    line = [int(x) for x in line.split(' ')]
    results = findZeroRow(line, [line])
    for i in range(len(results)-1, 0, -1):
        results[i-1].insert(0, results[i-1][0]-results[i][0])
        #results[i-1].append(results[i-1][-1]+results[i][-1])
    total += results[0][0]
print(total)

