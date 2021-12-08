from itertools import permutations

with open('input/day8.txt', 'r', encoding='utf8') as file:
    lines = file.read().splitlines()

digit_count = 0
for line in lines:
    patterns, value = [s.split(' ') for s in line.split(' | ')]
    for digit in value:
        if len(digit) in [2,3,4,7]:
            digit_count += 1
print(digit_count)

numbers = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9,
}

def decode(value, key):
    d = {'abcdefg'[i]:key[i] for i in range(7)}
    return ''.join(sorted([d[c] for c in value]))

total = 0
for line in lines:
    patterns, value = [s.split(' ') for s in line.split(' | ')]
    patterns = [''.join(sorted(pattern)) for pattern in patterns]
    keys = [''.join(key) for key in permutations('abcdefg')]
    for key in keys:
        if all(decode(pattern,key) in numbers for pattern in patterns):
            break
    answer = ''
    for digit in value:
        answer += str(numbers[decode(digit,key)])
    total += int(answer)
print(total)