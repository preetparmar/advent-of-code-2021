# Importing Libary
from collections import Counter

# Importing Data
with open('day_03/data.txt') as input:
    input_values = [x for x in input.read().split()]

""" Part 1 """
def find_gamma_rate(input_values):
    length = len(input_values[0])
    gamma_rate_binary = ''
    for ix in range(length):
        mode = Counter(map(lambda x: x[ix], input_values)).most_common()[0][0]
        gamma_rate_binary += mode
    return gamma_rate_binary

def find_epsilon_rate(gamma_rate_binary):
    return ''.join('1' if x == '0' else '0' for x in gamma_rate_binary)

def get_power_consumption(gamma_rate_binary, epsilon_rate_binary):
    return int(gamma_rate_binary, 2) * int(epsilon_rate_binary, 2)

gamma_rate_binary = find_gamma_rate(input_values)
epsilon_rate_binary = find_epsilon_rate(gamma_rate_binary)
solution_1 = get_power_consumption(gamma_rate_binary, epsilon_rate_binary)
print(solution_1)

""" Part 2 """
def find_mode(values, criterion):
    most_common = Counter(values).most_common()
    if criterion == 'most':
        if len(most_common) > 1 and most_common[0][1] == most_common [1][1]:
            return '1'
        else:
            return most_common[0][0]
    elif criterion == 'least':
        if len(most_common) > 1 and most_common[0][1] == most_common [1][1]:
            return '0'
        else:
            return most_common[-1][0]

def find_binary_value(input_values, ix=0, result='', criterion='most'):
    if ix == len(input_values[0]):
        return result
    bit_values = list(map(lambda x: x[ix], input_values))
    mode = find_mode(bit_values, criterion)
    new_list = list(filter(lambda x: x[ix] == mode, input_values))
    result += mode
    ix += 1
    return find_binary_value(new_list, ix, result, criterion)

def find_oxygen_generator_rating(o2_rating_binary, co2_rating_binary):
    return int(o2_rating_binary, 2) * int(co2_rating_binary, 2)

o2_rating_binary = find_binary_value(input_values, criterion='most')
co2_rating_binary = find_binary_value(input_values, criterion='least')
solution_2 = find_oxygen_generator_rating(o2_rating_binary, co2_rating_binary)
print(solution_2)