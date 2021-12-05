from typing import DefaultDict

def generate_points(line_start, line_end):
    points = [line_start]
    pos = line_start
    while pos != line_end:
        x = 1 if pos[0] < line_end[0] else -1 if pos[0] > line_end[0] else 0
        y = 1 if pos[1] < line_end[1] else -1 if pos[1] > line_end[1] else 0        
        pos = tuple((pos[0] + x, pos[1] + y))
        points.append(pos)
    return points

points = DefaultDict(int)
points_including_diagonals = DefaultDict(int)
with open('input/day5.txt', 'r', encoding='utf8') as file:
    for line in file:
        s1, s2 = line.split(' -> ')
        line_start = tuple(int(number) for number in s1.split(','))
        line_end = tuple(int(number) for number in s2.split(','))
        is_diagonal = line_start[0] != line_end[0] and line_start[1] != line_end[1]
        line_points = generate_points(line_start, line_end)
        for line_point in line_points:
            if not is_diagonal:
                points[line_point] += 1                
            points_including_diagonals[line_point] += 1

print(sum(value >= 2 for value in points.values()))
print(sum(value >= 2 for value in points_including_diagonals.values()))