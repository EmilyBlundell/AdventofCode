strat_guide = open('2/strategyguide.txt')
sg = strat_guide.readlines()

p1 = ['X', 'Y', 'Z']
p2 = ['A', 'B', 'C']

total_score = 0

for line in sg:

    me = p1.index(line[2])
    elf = p2.index(line[0])
    difference = me-elf

    total_score += (me+1)

    if difference == -1 or difference == 2:

        total_score += 6

    elif difference == 0:

        total_score += 3

print(total_score)
