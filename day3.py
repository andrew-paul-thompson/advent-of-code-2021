with open('input/day3.txt', 'r', encoding='utf8') as file:
    values = [value.strip() for value in file.readlines()]

# Part 1
gamma = ''
for i in range(len(values[0])):
    bits = [value[i] for value in values]
    zeroes, ones = bits.count('0'), bits.count('1')
    gamma += '1' if ones > zeroes else '0'
epsilon = ''.join('0' if bit == '1' else '1' for bit in gamma)
print(int(gamma,2) * int(epsilon,2))

# Part 2
oxygen_values = values.copy()
for i in range(len(values[0])):
    bits = [value[i] for value in oxygen_values]
    zeroes, ones = bits.count('0'), bits.count('1')
    most_common = '1' if ones >= zeroes else '0'
    oxygen_values = [value for value in oxygen_values if value[i] == most_common]
    if len(oxygen_values) == 1:
        oxygen = oxygen_values[0]
        break

co2_values = values.copy()
for i in range(len(co2_values[0])):
    bits = [value[i] for value in co2_values]
    zeroes, ones = bits.count('0'), bits.count('1')
    most_common = '1' if ones >= zeroes else '0'
    co2_values = [value for value in co2_values if value[i] != most_common]
    if len(co2_values) == 1:
        co2 = co2_values[0]
        break

print(int(oxygen,2) * int(co2,2))