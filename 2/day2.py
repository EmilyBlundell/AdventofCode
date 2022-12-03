strat_guide = open('2/strategyguide.txt')
sg = strat_guide.readlines()

p1 = ['X', 'Z', 'Y']
p2 = ['A', 'C', 'B']

total_score = 0

for line in sg:

    me = p1.index(line[2])
    elf = p2.index(line[0])
    difference = me-elf

    if me == 1:

        me = 2

    elif me == 2:

        me = 1

    total_score+=(me+1)

    if difference == -1 or difference == 2:

        total_score += 6

    elif difference == 0:

        total_score += 3

print(total_score)
