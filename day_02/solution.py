# Importing data
with open('day_02/data.txt') as input:
    _instructions = [x.split() for x in input.read().split('\n')]
    input_values = [(_ins[0], int(_ins[1])) for _ins in _instructions]


# Part 1
pos_horizontal = 0
depth = 0

for instruction in input_values:
    if instruction[0] == 'forward':
        pos_horizontal += instruction[1]
    elif instruction[0] == 'up':
        depth -= instruction[1]
    else:
        depth += instruction[1]

part_1_answer = pos_horizontal * depth
print(part_1_answer)

# Part 2 Solution
pos_horizontal = 0
depth = 0
aim = 0

for instruction in input_values:
    if instruction[0] == 'forward':
        pos_horizontal += instruction[1]
        depth += aim * instruction[1]
    elif instruction[0] == 'up':
        aim -= instruction[1]
    else:
        aim += instruction[1]

part_2_answer = pos_horizontal * depth
print(part_2_answer)