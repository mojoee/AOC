with open("day12/test.txt") as file:
    data = file.read().splitlines()

for row in data:
    string, numbers = row.split(' ')
    if string.startswith("."):
        print("starts with .")
    elif string.startswith("?"):
        