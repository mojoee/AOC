import re

# Read the corrupted memory
with open('2024/day3/input.txt') as f:
    lines = f.readlines()

# Combine all lines into a single string
memory = ''.join(lines)

# Initialize variables
result = 0
enabled = True  # At the start, mul is enabled

# Tokenize the memory into meaningful chunks
tokens = re.split(r'(do\(\)|don\'t\(\))', memory)

# Iterate over the tokens
for token in tokens:
    token = token.strip()
    
    if token == 'do()':
        enabled = True  # Enable future mul instructions
    elif token == "don't()":
        enabled = False  # Disable future mul instructions
    elif enabled:  # Process `mul` instructions only if enabled
        matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', token)
        for a, b in matches:
            result += int(a) * int(b)

# Print the final result
print(result)
