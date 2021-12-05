import re

class BingoCard:
    
    def __init__(self, numbers):
        self.numbers = numbers.copy()
        self.marked = [[False]*5 for _ in range(5)]
    
    def __repr__(self):
        return '\n'.join([' '.join([str(number) for number in line]) for line in self.numbers])
    
    def mark(self, mark_number):
        for line_number, line in enumerate(self.numbers):
            for index, number in enumerate(line):
                if number == mark_number:
                    self.marked[line_number][index] = True
                    return
    
    def is_bingo(self):
        for i in range(5):
            if all(self.marked[i]) or all(self.marked[j][i] for j in range(5)):
                return True
        return False

    
    def score(self, drawn_number):
        unmarked_sum = 0
        for i in range(5):
            for j in range(5):
                unmarked_sum += self.numbers[i][j] if not self.marked[i][j] else 0
        return unmarked_sum * drawn_number

cards = []
r = r'([0-9]+[ ]*)'
with open('input/day4.txt', 'r', encoding='utf8') as file:
    drawn_numbers = [int(number) for number in file.readline().split(',')]
    file.readline() # skip line
    numbers = []
    for line in file:
        if line == '\n':
            cards.append(BingoCard(numbers))
            numbers = []
        else:
            numbers.append([int(m.strip()) for m in re.findall(r,line)])
    cards.append(BingoCard(numbers))

# Part 1
for drawn_number in drawn_numbers:
    for card in cards:
        card.mark(drawn_number)
    winners = [card for card in cards if card.is_bingo()]
    if winners:
        winner = winners[0]
        print(winner.score(drawn_number))
        break

# Part 2
for drawn_number in drawn_numbers:
    drawn_number = int(drawn_number)
    for card in cards:
        card.mark(drawn_number)
    if len(cards) == 1:
        last_card = cards[0]
    cards = [card for card in cards if not card.is_bingo()]
    if len(cards) == 0:
        print(last_card.score(drawn_number))
        break