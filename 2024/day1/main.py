from collections import Counter


part1=False

list1 = []
list2 = []
with open('day1/myinput.txt') as f:
    lines = f.readlines()
    for line in lines:
        a, b = line.split()
        list1.append(int(a))
        list2.append(int(b))
if part1:
    list1.sort()
    list2.sort()
    result = 0
    for i in range(len(list1)):
        diff = abs(list1[i] - list2[i])
        result+=diff
    print(result)

resultp2 = 0
scores = Counter(list2)
for n in list1:
    resultp2 += n * scores[n]

print(resultp2)

