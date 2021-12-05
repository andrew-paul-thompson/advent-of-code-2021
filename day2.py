with open('input/day2.txt', 'r', encoding='utf8') as file:
    commands = file.readlines()

# Part 1
depth, position = 0, 0
for command in commands:
    direction, amount = command.split(' ')
    amount = int(amount)
    if direction == 'forward':
        position += amount
    elif direction == 'down':
        depth += amount
    elif direction == 'up':
        depth -= amount
print(depth * position)

# Part 2
depth, position, aim = 0, 0, 0
for command in commands:
    direction, amount = command.split(' ')
    amount = int(amount)
    if direction == 'down':
        aim += amount
    elif direction == 'up':
        aim -= amount
    elif direction == 'forward':
        position += amount
        depth += aim * amount
print(depth * position)