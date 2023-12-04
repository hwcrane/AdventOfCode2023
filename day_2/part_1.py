import sys

bag = {'blue': 14, 'red': 12, 'green': 13}

with open(sys.argv[1]) as f:
    input = [line.strip().split(': ')[1] for line in f.readlines()]


total = 0

for i, line in enumerate(input):
    possible = True
    rounds = line.split('; ')
    for round in rounds:
        grabs = round.split(', ')
        for grab in grabs:
            n, colour = grab.split()
            if bag[colour] < int(n):
                possible = False
    if possible:
        total += i + 1
print(total)
