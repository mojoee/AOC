LUT = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

def get_first_number(text):
    for i, letter in enumerate(text):
        for key in LUT.keys():
            if key in text[:i]:
                return str(LUT[key])
        for key in LUT.keys():
            if key[::-1] in text[:i]:
                return str(LUT[key])
        if letter.isnumeric():
            return letter


with open ("input.txt", "r") as myfile:
    data = myfile.read().splitlines()


print(data)
result = []
for obs in data:
    number = ""

    number += get_first_number(obs)
    number += get_first_number(obs[::-1])
    result.append(int(number))
    print(number)
    
print(sum(result))
