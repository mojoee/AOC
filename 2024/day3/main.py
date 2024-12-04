import re

with open('2024/day3/test2.txt') as f:
    lines = f.readlines()

matches = re.findall('mul\(\d{1,3},\d{1,3}\)', ''.join(lines))
print(matches)
result = 0
for match in matches:
    a,b = re.findall(r'\d+', match)
    result+= int(a)*int(b)
print(result)


result = 0
parts = re.split("don't()", ''.join(lines))
matches = re.findall('mul\(\d{1,3},\d{1,3}\)', parts[0])
for match in matches:
    a, b = re.findall(r'\d+', match)
    result += int(a) * int(b)
print(result)

for part in parts[1:]:
    if part=='':
        continue
    if not 'do()' in part:
        continue
    subparts = re.split("do()", part)
    matches = re.findall('mul\(\d{1,3},\d{1,3}\)', subparts[1])
    for match in matches:
        a, b = re.findall(r'\d+', match)
        result += int(a) * int(b)

print(result)