def count_increases(a):
    increases = 0
    for i, v in enumerate(a):
        if i >= 1:
            if v > a[i-1]:
                increases += 1
    return increases

with open('input/day1.txt', 'r', encoding='utf8') as file:
    depths = [int(line) for line in file.readlines()]

# Part 1
print(count_increases(depths))

# Part 2
windows = [sum(depths[i:i+3]) for i in range(len(depths))]
print(count_increases(windows))