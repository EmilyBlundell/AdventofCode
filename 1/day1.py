elfcals = open('elfcalories.txt')
elfcals = elfcals.readlines()

length = len(elfcals)

prev_total = 0

new_total = 0

top_scores = [0, 0, 0]

for line in elfcals:

    if line != '\n':

        if elfcals.index(line) != length-1:

            new_total += int(line[0:(len(line)-1)])

        else:

            new_total += int(line)
    else:

        top_scores.append(new_total)

        if new_total > min(top_scores):

            top_scores.remove(min(top_scores))

        else:

            top_scores.remove(new_total)

        new_total = 0

top_elf = max(top_scores)

total_top3 = sum(top_scores)

print(top_elf)

print(total_top3)
