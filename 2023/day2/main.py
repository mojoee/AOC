with open ("day2/input.txt", "r") as myfile:
    data = myfile.read().splitlines()



result = 0
for i, obs in enumerate(data):
    obs = obs.split(':')[1]
    maxValues = {"red": float('-inf'), "green": float('-inf'), "blue": float('-inf')}
    for game in obs.split(';'):
        for draw in game.split(','):
            draw = draw.strip()
            number, color = draw.split(' ')
            number = int(number)
            if number > maxValues[color]:
                maxValues[color] = number
    
    result += maxValues["red"]*maxValues["blue"]*maxValues["green"]

print(result)