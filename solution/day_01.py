# Importing data
with open('./resources/day_01.txt') as input:
    input_values = [int(x) for x in input.read().split()]

# Part 1 solution
part_1_result = [i2 > i1 for i1, i2 in zip(input_values, input_values[1:])]
sum(part_1_result)

# Part 2 solution
grouped_list = []

start_ix = 0
end_ix = 3
while end_ix <= len(input_values):
    grouped_list.append(sum(input_values[start_ix:end_ix]))
    start_ix += 1
    end_ix += 1

part_2_result = [i2 > i1 for i1, i2 in zip(grouped_list, grouped_list[1:])]
sum(part_2_result)
