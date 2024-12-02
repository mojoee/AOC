import numpy as np

with open("day13/input.txt") as file:
    data = file.read().splitlines()

print(data)


particular_value = ""
result = []
temp_list = []
for i in data:
    if i == particular_value:
        temp_list.append(i)
        result.append(temp_list)
        temp_list = []
    else:
        temp_list.append(i)
result.append(temp_list)
print("The list after splitting by a value : " + str(result))
value = 0


for pattern in result:
    r = len(pattern)
    c = len(pattern[0])
    nppattern = np.zeros((r,c))
    for i, row in enumerate(pattern):
        for j, ch in enumerate(row):
            if ch=="#":
                nppattern[i,j] = 1
            elif ch==".":
                nppattern[i,j] = 0
            else:
                print("character not known")
    print(nppattern)
    symmetry = True
    # check for horizontal sym
    pattern=nppattern
    for i, row in enumerate(pattern[:-1]):
        if np.array_equal(row, pattern[1+i]):
            print(f"found horizontal symmetry line at {i}")
            for j in range(1, max(i, pattern.shape[0]-i)):
                if i+j+1 >= pattern.shape[0]:
                    continue
                elif np.array_equal(pattern[i-j], pattern[i+j+1]):
                    continue
                elif i-j < 0:
                    break
                else:
                    print("Symmetry broken")
                    symmetry = False
                    break
            if symmetry:
                value+=100*(i+1)
            symmetry = True  
    # check for vertical sym
    symmetry = True
    for i, column in enumerate(pattern.T[:-1]):
        if np.array_equal(column, pattern.T[1+i]):
            print(f"found vertical symm line at {i}")
            for j in range(1, pattern.shape[1]):
                if i+j+1 >= len(pattern.T):
                    continue
                elif np.array_equal(pattern.T[i-j], pattern.T[i+j+1]):
                    continue
                elif i-j < 0:
                    value+=1
                else:
                    print("Symmetry broken")
                    symmetry = False
            if symmetry:
                value+=i+1
            symmetry = True  
            
                    
print(value)
