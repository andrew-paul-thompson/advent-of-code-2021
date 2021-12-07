def fuel(n):
    return n * (n + 1) // 2

with open('input/day7.txt', 'r', encoding='utf8') as file:
    crabs=[int(n) for n in file.read().split(',')]

print(min(sum([abs(crab-i) for crab in crabs]) for i in range(max(crabs))))
print(min(sum([fuel(abs(crab-i)) for crab in crabs]) for i in range(max(crabs))))