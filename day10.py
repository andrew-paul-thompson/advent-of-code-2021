matching = {')': '(', ']': '[', '}': '{', '>': '<',
            '(': ')', '[': ']', '{': '}', '<': '>'}


def get_first_illegal_character(line):
    stack = []
    for char in line:
        if char in '([{<':
            stack.append(char)
        else:
            match = matching[char]
            if stack[-1] != match:
                return char
            stack.pop()


def get_corrupted_score(line):
    score = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    return score.get(get_first_illegal_character(line), 0)


def get_autocomplete_string(line):
    if get_first_illegal_character(line):
        return ''
    stack = []

    for char in line:
        if char in '([{<':
            stack.append(char)
        else:
            match = matching[char]
            stack.pop()
    s = ''
    while stack:
        s += matching[stack.pop()]
    return s


def get_autocomplete_score(line):
    s = get_autocomplete_string(line)
    score = {')': 1, ']': 2, '}': 3, '>': 4}
    total = 0
    for c in s:
        total *= 5
        total += score.get(c, 0)
    return total


with open('input/day10.txt', 'r', encoding='utf8') as file:
    lines = file.read().splitlines()

print(sum(get_corrupted_score(line) for line in lines))
autocomplete_scores = [value for value in sorted(
    [get_autocomplete_score(line) for line in lines]) if value > 0]
print(autocomplete_scores[len(autocomplete_scores)//2])
