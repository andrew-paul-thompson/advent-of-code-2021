with open('input/day6.txt', 'r', encoding='utf8') as file:
    fish_list = [int(value) for value in file.read().split(',')]

population = [0,0,0,0,0,0,0,0,0]
for fish in fish_list:
    population[fish] += 1

for day in range(1, 257):
    population = population[1:] + population[:1]
    population[6] += population[8]
    if day == 80:
        print(sum(population))
print(sum(population))
